from django.views.generic import ListView, DetailView,CreateView,DeleteView,UpdateView
from .models import Snack
from django.urls import reverse_lazy

# Create your views here.

# Read
class SnackListView(ListView):
    model =Snack
    template_name='snack_list.html'

class SnackDetailsView(DetailView):
    model =Snack
    template_name='snack_detail.html'

class SnackCreateView(CreateView):
    model =Snack
    template_name='snack_create.html'
    fields=['title','purshaser','description']

class SnackUpdateView(UpdateView):
    model = Snack
    template_name='snack_update.html'
    fields=['title','purshaser','description']

class SnackDeleteView(DeleteView):
    model =Snack
    template_name='snack_delete.html'
    success_url= reverse_lazy('snack_list')
