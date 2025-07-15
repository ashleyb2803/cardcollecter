from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
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
    # Get all wrestlers associated with this card (M:M relationship)
    associated_wrestlers = card.wrestlers.all()
    print(card)
    return render(request, 'cards/detail.html', {
        'card': card, 
        'wrestler_form': wrestler_form,
        'associated_wrestlers': associated_wrestlers
    })


# New wrestler list views
def wrestler_index(request):
    """Display all wrestlers"""
    wrestlers = Wrestler.objects.all().order_by('name')
    return render(request, 'wrestlers/wrestler_index.html', {'wrestlers': wrestlers})


def wrestler_detail(request, wrestler_id):
    """Display details for a specific wrestler"""
    wrestler = get_object_or_404(Wrestler, id=wrestler_id)
    # Get all cards associated with this wrestler (M:M relationship)
    wrestler_cards = wrestler.cards.all()
    return render(request, 'wrestlers/wrestler_detail.html', {
        'wrestler': wrestler,
        'wrestler_cards': wrestler_cards
    })


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
        new_wrestler.save()  # Save the wrestler first
        # Now add the card to the wrestler's cards (M:M relationship)
        card = get_object_or_404(Card, id=card_id)
        new_wrestler.cards.add(card)
    return redirect('card-detail', card_id=card_id)


def wrestler_update(request, wrestler_id):
    wrestler = get_object_or_404(Wrestler, id=wrestler_id)
    
    if request.method == 'POST':
        form = WrestlerForm(request.POST, instance=wrestler)
        if form.is_valid():
            form.save()
            # Since we have M:M relationship, we need to redirect differently
            # Let's redirect to the wrestler detail page instead
            return redirect('wrestler-detail', wrestler_id=wrestler.id)
    else:
        form = WrestlerForm(instance=wrestler)
    
    return render(request, 'wrestlers/update.html', {
        'form': form,
        'wrestler': wrestler
    })


def wrestler_delete(request, wrestler_id):
    wrestler = get_object_or_404(Wrestler, id=wrestler_id)
    
    if request.method == 'POST':
        wrestler.delete()
        # Redirect to wrestler index since we no longer have a single card association
        return redirect('wrestler_index')
    
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