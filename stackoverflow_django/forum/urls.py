from django.urls import path, include

from forum import views

urlpatterns = [
    path('questions/', views.QuestionsList.as_view()),
    path('answers/', views.AnswersList.as_view()),
    path('categories/', views.CategoriesList.as_view()),
    path('comments/', views.CommentsList.as_view()),
    path('questions/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('queue_users/<id>/', views.QueueUserDetail.as_view()),
    path('search/', views.search),
    path('ask/', views.ask),
    path('answer/', views.answer),
    path('comment/', views.comment),
    path('profile/', views.profile),
    path('edit_profile/', views.edit_profile),
    path('queue_users/', views.QueueUsersList.as_view()),
    path('questions/<slug:category_slug>/<slug:question_slug>/', views.QuestionDetail.as_view()),
]