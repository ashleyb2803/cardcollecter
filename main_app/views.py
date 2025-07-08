from django.shortcuts import render
# temporary baby step
from django.http import HttpResponse


# Create your views here.
def home(request):
  return render(request, 'home.html',)
   

def about(request):
  return render(request, 'about.html')

def card_index(request):
  cards= [
      {'name': 'Card 1', 'description': 'A sample card'},
        {'name': 'Card 2', 'description': 'Another sample card'},
    ]
  return render(request, 'cards/index.html', {'cards': cards})


