from django.urls import path, include

from forum import views

urlpatterns = [
    path('trending-questions/', views.LatestQuestionsList.as_view()),
    path('questions/search/', views.search),
    path('<slug:category_slug>/<slug:product_slug>/', views.QuestionDetail.as_view()),
    path('categories/', views.CategoryDetail.as_view())
]