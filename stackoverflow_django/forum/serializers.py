from rest_framework import serializers

from .models import Category, Question#, Community

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "id",
            "question",
            "description",
            "get_absolute_url",
            
        )

class CategorySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many = True)

    class Meta:
        model = Category
        fields = {
            "id",
            "name",
            #"community",
            "get_absolute_url",
        }

# class CommunitySerializer(serializers.ModelSerializer):
#     categories = CategorySerializer(many = True)

#     class Meta:
#         model = Community
#         fields = {
#             "id",
#             "name",
#             "get_absolute_url",
#         }