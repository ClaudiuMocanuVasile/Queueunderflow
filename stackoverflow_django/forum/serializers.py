from rest_framework import serializers

from .models import *

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            "id",
            "question",
            "queue_user",
            "answer",
            "date_posted"
            
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
            "answers"
            
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
    questions = QuestionSerializer(many = True)

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
            "get_absolute_url",
            "questions",
            "date_registered"
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