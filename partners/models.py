from django.db import models
from wagtail.snippets.models import register_snippet
from django.contrib.auth.models import User
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class Remises(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    codeBl = models.CharField(max_length=25, default='', blank=True, null=True )
    dateBon =models.DateField()
    percentage =  models.DecimalField(max_digits=15, decimal_places=2, default=0)
    montantBl = models.DecimalField(max_digits=150, decimal_places=2, default=0)
    remise = models.DecimalField(max_digits=150, decimal_places=2, default=0)

class ProductBought(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    codeBl = models.CharField(max_length=25, default='', blank=True, null=True )
    dateBon =models.DateField()
    ProduitReference =  models.TextField(default='')
    ProduitName =  models.TextField(default='')
    quantity_bought = models.IntegerField(default=0)
    unitprice = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    quantity_sold = models.IntegerField(default=0)
    numSeries = models.TextField(default='')
    quantity_stucked = models.IntegerField(default=0)
    

            
class Commande(models.Model):
    etat_CHOICES = [
        ("en-attente", "en-attente"),
        ("validé", "validé"),     
        ("annulé", "annulé"),     
        ("Livré", "Livré"),     
    ]
    client = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name="mes_commandes")
    dateCommande =models.DateField()
    note = models.CharField(max_length=255, default='')
    etatCommande = models.CharField( max_length=30, choices=etat_CHOICES, default="en-attente") 

class ProduitEnCommande(models.Model):
    commande =  models.ForeignKey(Commande, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name="produits_en_commandes") 
    name= models.CharField(null=True ,max_length=100) 
    reference= models.CharField(null=True ,max_length=100)  
    qty = models.IntegerField(default= 0)
    prixVente = models.DecimalField(max_digits=15, decimal_places=2, default=0)

@register_snippet   
class FeedBack(models.Model):
    etat_CHOICES = [
        ("en-attente", "en-attente"),
        ("en-cours", "en-cours"),     
        ("clos", "clos"),     
    ]
    client = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    dateBon =models.DateField()
    objet = models.CharField(max_length=255, default='')
    message = models.TextField(default='')
    reponse = models.TextField(default='') 
    etatFeedBack = models.CharField( max_length=30, choices=etat_CHOICES, default="en-attente")