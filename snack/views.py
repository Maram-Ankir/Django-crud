from django.views.generic import ListView, DetailView,CreateView,DeleteView,UpdateView
from .models import Snack
from django.urls import reverse_lazy

# Create your views here.

# Read
class SnackListView(ListView):
    template_name='snack_list.html'
    model =Snack

class SnackDetailsView(DetailView):
    template_name='snack_detail.html'
    model =Snack

class SnackCreateView(CreateView):
    model =Snack
    template_name='snack_create.html'
    fields=['title','purchaser','description']

class SnackUpdateView(UpdateView):
    model = Snack
    template_name='snack_update.html'
    fields=['title','purchaser','description']

class SnackDeleteView(DeleteView):
    model =Snack
    template_name='snack_delete.html'
    success_url= reverse_lazy('snack_list')
