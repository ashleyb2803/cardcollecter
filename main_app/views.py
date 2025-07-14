from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Card, Wrestler, Pack
from .forms import WrestlerForm
import random


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



def open_pack(request):
    """Simple pack opening view"""
    if request.method == 'POST':
        # Create and open a new pack
        pack = Pack.objects.create()
        drawn_cards = pack.open_pack()
        
        context = {
            'drawn_cards': drawn_cards,
            'pack': pack
        }
        
        return render(request, 'packs/pack_opened.html', context)
    
    return render(request, 'packs/open_pack.html')

def my_packs(request):
    """View all packs"""
    packs = Pack.objects.all().order_by('-created_at')
    return render(request, 'packs/my_packs.html', {'packs': packs})

def pack_detail(request, pack_id):
    """View what cards were in an opened pack"""
    pack = get_object_or_404(Pack, id=pack_id)
    
    if not pack.opened:
        messages.error(request, 'This pack has not been opened yet.')
        return redirect('my-packs')
    
    return render(request, 'packs/detail.html', {
        'pack': pack,
        'message': 'Pack was opened on ' + pack.created_at.strftime('%B %d, %Y')
    })
