from django.db import models
from django.urls import reverse



class Card(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('card-detail', kwargs={'card_id': self.id})
    

class Wrestler(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, blank=True)
    debut_year = models.IntegerField()
    championships_won = models.IntegerField(default=0)
    signature_move = models.CharField(max_length=100, blank=True)

    # ForeignKey to Card model
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"
    
class Meta:
        ordering = ['name, description']


class Pack(models.Model):
    opened = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        status = "Opened" if self.opened else "Unopened"
        return f"Pack #{self.id} ({status})"
    
    def open_pack(self):
        """Open pack and return 5 random cards"""
        if self.opened:
            return []
        
       
        all_cards = list(Card.objects.all())
        if len(all_cards) < 5:
            drawn_cards = all_cards  
        else:
            drawn_cards = random.sample(all_cards, 5)
        
     
        self.opened = True
        self.save()
        
        return drawn_cards