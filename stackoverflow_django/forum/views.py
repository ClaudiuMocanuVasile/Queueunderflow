from django.db.models import Q
from django.shortcuts import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Question, Category#, Community
from .serializers import QuestionSerializer, CategorySerializer

# Create your views here.

class QuestionsList(APIView):
    def get(self, request, format = None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many = True)
        return Response(serializer.data)

class CategoriesList(APIView):
    def get(self, request, format = None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug = category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format = None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class QuestionDetail(APIView):
    def get_object(self, category_slug, question_slug):
        try:
            return Question.objects.filter(category__slug = category_slug).get(slug = question_slug)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, question_slug, format = None):
        question = self.get_object(category_slug, question_slug)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        questions = Question.objects.filter(Q(question__icontains = query) | Q(description__icontains = query))
        serializer = QuestionSerializer(questions, many = True)
        return Response(serializer.data)
    else:
        return Response({"questions": {}})