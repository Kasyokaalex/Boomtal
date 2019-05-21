from django.urls import path
from . import views

app_name = 'bomtalapp'

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('homepage', views.homepage, name='homepage'),
    path('create_account', views.create_account, name='create_account'),
    path('index', views.index, name='index'),
    path('(?P<album_id>[0-9]+)/', views.detail, name='detail'),
    path('create_album/', views.create_album, name='create_album'),
    path('(?P<album_id>[0-9]+)/create_song', views.create_song, name='create_song'),
    path('(?P<album_id>[0-9]+)/delete_album', views.delete_album, name='delete_album'),
    path('(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/', views.delete_song, name='delete_song'),



]