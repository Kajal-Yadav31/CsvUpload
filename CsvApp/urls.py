from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('upload/', views.uploadCsvfile, name="upload"),
    path('analyze/<int:upload_id>/', views.analysingfile, name="analyze"),
    path('datasets/', views.dataset_list, name='dataset_list'),

]
