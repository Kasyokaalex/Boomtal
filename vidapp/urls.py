from django.urls import path
from . import views

app_name='vidapp'

urlpatterns=[
    path('video', views.VidListView.as_view(), name='video'),
    path('add-video', views.VidCreateView.as_view(), name='add-video'),
    path('<int:pk>/update', views.VidUpdateView, name='update'),
    path('<int:pk>/delete', views.VidDeleteView, name='delete'),
]