from rest_framework import serializers

from .models import Category, Community, Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "id",
            "question",
            "description",
            "get_absolute_url",
            
        )