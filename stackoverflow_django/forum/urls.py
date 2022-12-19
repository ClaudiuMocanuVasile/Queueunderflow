from django.urls import path, include

from forum import views

urlpatterns = [
    path('trending-questions/', views.LatestProductsList.as_view()),
]