from django.db.models import Q
from django.shortcuts import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import *
from .serializers import*

# Create your views here.

class QuestionsList(APIView):
    def get(self, request, format = None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many = True)
        return Response(serializer.data)

class QueueUsersList(APIView):
    def get(self, request, format = None):
        users = QueueUser.objects.all()
        serializer = QueueUserSerializer(users, many = True)
        return Response(serializer.data)

class AnswersList(APIView):
    def get(self, request, format = None):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many = True)
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

class QueueUserDetail(APIView):
    def get_object(self, user_slug):
        try:
            return QueueUser.objects.get(slug = user_slug)
        except QueueUser.DoesNotExist:
            raise Http404

    def get(self, request, user_slug, format = None):
        user = self.get_object(user_slug)
        serializer = QueueUserSerializer(user)
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
    print(request.data)

    if query:
        questions = Question.objects.filter(Q(question__icontains = query) | Q(description__icontains = query))
        serializer = QuestionSerializer(questions, many = True)
        return Response(serializer.data)
    else:
        return Response({"questions": {}})

@api_view(['POST'])
def ask(request):

    # Example request

    # {
    # "question" : "What's the difference between an interface and an abstract class in Java",
    # "category" : "2", // id of category of the question
    # "description" : "", // can be empty
    # "queue_user": "2", // 
    # "slug" : "" // is calculated below
    # }

    serializer = QuestionSerializer(data = request.data)
    if serializer.is_valid():
        print(serializer.validated_data)
        serializer.save()
        serializer._data['slug'] = "question_"+"0"*(10-len(str(serializer.data['id']))) + str(serializer.data['id'])
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def answer(request):

    # Example request

    # {
    # "question" : "17",
    # "answer" : "You can use the STL stack container class, which implements a stack on top of other container classes like vector, deque, etc.",
    # "queue_user": "2"
    # }

    serializer = AnswerSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def profile(request):
    token = request.data.get('token', '')
    user = Token.objects.get(key = token).user

    user = QueueUser.objects.get(id = user.id)
    serializer = QueueUserSerializer(user)
    return Response(serializer.data)