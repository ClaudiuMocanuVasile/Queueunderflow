from django.db import models
from django.core.files import File
from django.contrib.auth.models import User

# My imports

from io import BytesIO
from PIL import Image
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.template.defaultfilters import slugify

# Create your models here.

# User derived from Django User table

class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('Username must be provided')
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            password = password,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(username = username, email = email, password = password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(username = username, email = email, password = password, **extra_fields)

class QueueUser(AbstractBaseUser,PermissionsMixin):
    # Foreign keys

    #queue_user = models.OneToOneField(User, on_delete = models.CASCADE)

    # Attributes
    
    username = models.CharField(unique = True, max_length = 25)
    password = models.CharField(max_length=128, verbose_name='password')
    first_name = models.CharField(max_length = 25, blank = True)  
    last_name = models.CharField(max_length = 25, blank = True)
    email = models.EmailField()
    #displayed_name = models.CharField(max_length = 12, null = True)
    birthday = models.DateField(null = True, blank = True)
    description = models.CharField(max_length = 255, null = True, blank = True)
    score = models.IntegerField(default = 0)
    date_registered = models.DateTimeField(auto_now_add = True)
    #subscription = models.BooleanField()
    profile_picture = models.ImageField(upload_to = 'uploads/', blank = True, null = True)
    thumbnail = models.ImageField(upload_to = 'uploads/', blank = True, null = True)

    # Utility
    
    slug = models.SlugField()

    is_staff = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_active = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_superuser = models.BooleanField(default=False) # this field we inherit from PermissionsMixin.

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('id', )

    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

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
    description = models.CharField(max_length = 65535, null = True, blank = True)
    upvotes = models.IntegerField(default = 0)
    downvotes = models.IntegerField(default = 0)
    date_posted = models.DateTimeField(auto_now_add = True)

    # Utility

    slug = models.SlugField(blank = True)

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
    upvotes = models.IntegerField(default = 0)
    downvotes = models.IntegerField(default = 0)
    date_posted = models.DateTimeField(auto_now_add = True)
    is_correct = models.BooleanField(default = False)

    # Utility

    class Meta:
        ordering = ('-question', '-date_posted', )

    def __str__(self):
        return self.answer


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