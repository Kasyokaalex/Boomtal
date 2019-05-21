from django.urls import path
from . import views

app_name='artapp'

urlpatterns=[
    path('hindex', views.ArtListView.as_view(),name='hindex'),
    path('add-art', views.ArtCreateView.as_view(), name='add-art'),
    path('<int:pk>/update', views.ArtUpdateView.as_view(), name='updateart'),
    path('<int:pk>/delete', views.ArtDeleteView.as_view(), name='deleteart'),
]