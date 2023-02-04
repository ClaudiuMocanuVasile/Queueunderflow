from django.db import models
from django.core.files import File
from django.contrib.auth.models import User

# My imports

from io import BytesIO
from PIL import Image

# Create your models here.

# User derived from Django User table

class QueueUser(models.Model):
    # Foreign keys

    queue_user = models.OneToOneField(User, on_delete = models.CASCADE)

    # Attributes
    
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    email = models.EmailField()
    displayed_name = models.CharField(max_length = 12)
    birthday = models.DateField()
    description = models.CharField(max_length = 255)
    score = models.IntegerField()
    date_registered = models.DateTimeField(auto_now_add = True)
    subscription = models.BooleanField()
    profile_picture = models.ImageField(upload_to = 'uploads/', blank = True, null = True)
    thumbnail = models.ImageField(upload_to = 'uploads/', blank = True, null = True)

    # Utility
    
    slug = models.SlugField()

    class Meta:
        ordering = ('displayed_name', )

    def __str__(self):
        return self.first_name + self.last_name

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.profile_picture.url
        return ''
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.profile_picture:
                self.thumbnail = self.make_thumbnail(self.profile_picture)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, profile_picture):
        img = Image.open(profile_picture)
        width_percent = (300/float(img.size[0]))
        h_size = int((float(img.size[1])*float(width_percent)))
        img.thumbnail((300, h_size))

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality = 85)

        thumbnail = File(thumb_io, name = profile_picture.name)

        return thumbnail

# class Community(models.Model):
#     # Attributes

#     name = models.CharField(max_length = 55)
#     date_created = models.DateTimeField(auto_now_add = True)
#     public = models.BooleanField()
#     premium = models.BooleanField()

#     # Utility

#     slug = models.SlugField()

#     class Meta:
#         ordering = ('name', )

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return f'/{self.slug}/'

class Category(models.Model):
    # Attributes

    name = models.CharField(max_length = 255)

    # Utility

    slug = models.SlugField()

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Question(models.Model):
    # Foreign keys

    category = models.ForeignKey(Category, related_name = 'questions', on_delete = models.SET_NULL, null = True, blank = True)
    queue_user = models.ForeignKey(QueueUser, related_name = 'queue_user_questions', on_delete = models.SET_NULL, null = True, blank = True)
    # community = models.ForeignKey(Community, related_name = 'community', on_delete = models.CASCADE, null = True, blank = True)

    # Attributes

    question = models.CharField(max_length = 255)
    description = models.CharField(max_length = 65535)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    date_posted = models.DateTimeField(auto_now_add = True)

    # Utility

    slug = models.SlugField()

    class Meta:
        ordering = ('-date_posted', )

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

class Answer(models.Model):
    # Foreign keys

    question = models.ForeignKey(Question, related_name = 'answers', on_delete = models.CASCADE, null = True)
    queue_user = models.ForeignKey(QueueUser, related_name = 'queue_user_answers', on_delete = models.SET_NULL, null = True)

    # Attributes

    answer = models.CharField(max_length = 65535)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    date_posted = models.DateTimeField(auto_now_add = True)
    is_correct = models.BooleanField()

    # Utility

    class Meta:
        ordering = ('-question', '-date_posted', )

    def __str__(self):
        return self.id


class Comment(models.Model):
    # Foreign keys

    question = models.ForeignKey(Question, related_name = 'question_comments', on_delete = models.CASCADE, null = True)
    answer = models.ForeignKey(Answer, related_name = 'answer_comments', on_delete = models.CASCADE, null = True)
    queue_user = models.ForeignKey(QueueUser, related_name = 'queue_user_comments', on_delete = models.SET_NULL, null = True)

    # Attributes

    comment = models.CharField(max_length = 65535)
    suggested_edit = models.BooleanField()
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    date_posted = models.DateTimeField(auto_now_add = True)

    # Utility

    class Meta:
        ordering = ('question', '-date_posted', )

    def __str__(self):
        return self.id