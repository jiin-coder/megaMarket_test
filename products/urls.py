from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('<int:id>/question/create/', views.question_create, name='question_create'),
]