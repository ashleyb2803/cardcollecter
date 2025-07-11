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

    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"
    
class Meta:
        ordering = ['name, description']