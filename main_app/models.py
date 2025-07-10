from django.db import models
from django.urls import reverse

class Card(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    
    
    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('card_detail', kwargs={'card_id': self.id})