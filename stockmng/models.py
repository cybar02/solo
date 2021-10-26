from django.db import models

# Create your models here.
#DB to add Designation; Price; Remaining
class Item(models.Model):
    designation = models.CharField(max_length=100, help_text="Nom de l'article")
    price = models.IntegerField(help_text='Prix en Ariary')
    remaining = models.IntegerField(help_text='Article Restant')
    deleteItem = models.BooleanField(default=False)
    def __str__(self):
        return self.designation