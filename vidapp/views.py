from django.shortcuts import render
from . models import Video
from django.views.generic import  ListView,CreateView,UpdateView,DeleteView

# Create your views here.
class VidListView(ListView):
    model = Video
    template_name = 'vidapp/vindex.html'
    context_object_name = 'videos'
    ordering = ['genre']


    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Video.objects.filter(name_icontains=query) | Video.objects.filter(file_icontains=query)
        else:
            return Video.objects.all()

class VidCreateView(CreateView):
     model = Video
     fields = '__all__'


class VidUpdateView(UpdateView):
     model = Video
     fields = '__all__'


class VidDeleteView(DeleteView):
     model = Video
     success_url = '/vindex'
