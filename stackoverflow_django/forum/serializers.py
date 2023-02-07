from rest_framework import serializers

from .models import *

class  CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            "id",
            "comment",
            "get_absolute_url",
            "queue_user",
            "category",
            "slug",
            "date_posted",
            "downvotes",
            "upvotes",
            
        )

class AnswerSerializer(serializers.ModelSerializer):
    answer_comments = CommentSerializer(many = True)

    class Meta:
        model = Answer
        fields = (
            "id",
            "question",
            "queue_user",
            "answer",
            "date_posted",
            "answer_comments",
            
        )

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many = True)

    class Meta:
        model = Question
        fields = (
            "id",
            "question",
            "description",
            "get_absolute_url",
            "queue_user",
            "category",
            "slug",
            "date_posted",
            "answers",
            
        )



class CategorySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many = True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            #"community",
            "slug",
            "get_absolute_url",
            "questions"
        )

class QueueUserSerializer(serializers.ModelSerializer):
    #questions = QuestionSerializer(many = True)
    #answers = AnswerSerializer(many = True)

    class Meta:
        model = QueueUser
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "description",
            "score",
            "birthday",
            "email",
            "slug",
             "date_registered",
            "get_absolute_url",
            #"questions",
            #"answers"
        )

# class CommunitySerializer(serializers.ModelSerializer):
#     categories = CategorySerializer(many = True)

#     class Meta:
#         model = Community
#         fields = {
#             "id",
#             "name",
#             "get_absolute_url",
#         }