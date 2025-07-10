from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Card


# Create your views here.
def home(request):
  return render(request, 'home.html',)
   

def about(request):
  return render(request, 'about.html')

def card_index(request):
  cards= Card.objects.all()
  return render(request, 'cards/index.html', {'cards': cards})

def card_detail(request, card_id):
  card = Card.objects.get(id=card_id)
  return render(request, 'cards/detail.html', {'card': card})


class CardCreate(CreateView):
  model = Card
  fields = ['name', 'description', 'image']
 
