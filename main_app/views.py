from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Card, Wrestler
from .forms import WrestlerForm


# Create your views here.
def home(request):
    return render(request, 'home.html',)


def about(request):
    return render(request, 'about.html')


def card_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})


def card_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    wrestler_form = WrestlerForm()
    print(card)
    return render(request, 'cards/detail.html', {'card': card, 'wrestler_form': wrestler_form})


class CardCreate(CreateView):
    model = Card
    fields = ['name', 'description']


class CardUpdate(UpdateView):
    model = Card
    fields = ['name', 'description']


class CardDelete(DeleteView):
    model = Card
    success_url = '/cards/'


def add_wrestler(request, card_id):
    form = WrestlerForm(request.POST)
    if form.is_valid():
        new_wrestler = form.save(commit=False)
        new_wrestler.card_id = card_id
        new_wrestler.save()
    return redirect('card-detail', card_id=card_id)


def wrestler_update(request, wrestler_id):
    wrestler = get_object_or_404(Wrestler, id=wrestler_id)
    
    if request.method == 'POST':
        form = WrestlerForm(request.POST, instance=wrestler)
        if form.is_valid():
            form.save()
            return redirect('card-detail', card_id=wrestler.card.id)
    else:
        form = WrestlerForm(instance=wrestler)
    
    return render(request, 'wrestlers/update.html', {
        'form': form,
        'wrestler': wrestler
    })


def wrestler_delete(request, wrestler_id):
    wrestler = get_object_or_404(Wrestler, id=wrestler_id)
    card_id = wrestler.card.id  # Store card_id before deleting
    
    if request.method == 'POST':
        wrestler.delete()
        return redirect('card-detail', card_id=card_id)
    
    return render(request, 'wrestlers/delete.html', {
        'wrestler': wrestler
    })