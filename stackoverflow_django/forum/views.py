from django.db.models import Q
from django.shortcuts import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Question, Category#, Community
from .serializers import QuestionSerializer, CategorySerializer

# Create your views here.

class LatestQuestionsList(APIView):
    def get(self, request, fromat = None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many = True)
        return Response(serializer.data)

class QuestionDetail(APIView):
    def get_object(self, community_slug, category_slug, question_slug):
        try:
            return Question.objects.filter(community__slug = community_slug, category__slug = category_slug).get(slug = question_slug)
        except Question.DoesNotExist:
            raise Http404

    def geT(self, request, community_slug, category_slug, product_slug, format = None):
        question = self.get_object(community_slug, category_slug, product_slug)
        serializer = LatestQuestionsList(question)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, community_slug, category_slug):
        try:
            return Category.objects.filter(community__slug = community_slug).get(slug = category_slug)
        except Category.DoesNotExist:
            raise Http404
        
        def get(self, request, community_slug, category_slug, format = None):
            category = self.get_object(community_slug, category_slug)
            serializer = CategorySerializer(category)
            return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        questions = Question.objects.filter(Q(name__icontains = query) | Q(description__icontains = query))
        serializer = QuestionSerializer(questions, many = True)
        return Response(serializer.data)
    else:
        return Response({"questions": {}})