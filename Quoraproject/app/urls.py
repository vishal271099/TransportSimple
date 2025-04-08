from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('', views.home, name='home'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
      path('like-answer/<int:pk>/', views.like_answer, name='like_answer'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)