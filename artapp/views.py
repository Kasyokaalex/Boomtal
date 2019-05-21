from django.shortcuts import render
from . models import Art
from django.shortcuts import reverse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

# Create your views here.
class ArtListView(ListView):
    model = Art
    template_name = 'artapp/index.html'
    context_object_name = 'arts'
    ordering = ['genre']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Art.objects.filter(genre_icontains=query) | Art.objects.filter(file_icontains=query)
        else:
            return Art.objects.all()


class ArtCreateView(CreateView):
    model = Art
    fields = '__all__'

class ArtDeleteView(DeleteView):
    model = Art
    success_url = '/hindex'

class ArtUpdateView(UpdateView):
    model = Art
    fields = '__all__'



