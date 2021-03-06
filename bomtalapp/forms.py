from django import forms
from . models import Album, Song, User


class AlbumForm(forms.ModelForm):

	class Meta:
		model = Album
		fields = ('name', 'genre', 'cover')


class SongForm(forms.ModelForm):

	class Meta:
		model = Song
		fields = ('song_name', 'song_file')


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

