# Generated by Django 4.2.5 on 2024-12-05 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCommande', models.DateField()),
                ('note', models.CharField(default='', max_length=255)),
                ('etatCommande', models.CharField(choices=[('en-attente', 'en-attente'), ('validé', 'validé'), ('annulé', 'annulé'), ('Livré', 'Livré')], default='en-attente', max_length=30)),
                ('client', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_commandes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Remises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeBl', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('dateBon', models.DateField()),
                ('percentage', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('montantBl', models.DecimalField(decimal_places=2, default=0, max_digits=150)),
                ('remise', models.DecimalField(decimal_places=2, default=0, max_digits=150)),
                ('client', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProduitEnCommande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('reference', models.CharField(max_length=100, null=True)),
                ('qty', models.IntegerField(default=0)),
                ('prixVente', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('commande', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produits_en_commandes', to='partners.commande')),
            ],
        ),
        migrations.CreateModel(
            name='ProductBought',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeBl', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('dateBon', models.DateField()),
                ('ProduitReference', models.TextField(default='')),
                ('ProduitName', models.TextField(default='')),
                ('quantity_bought', models.IntegerField(default=0)),
                ('unitprice', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('quantity_sold', models.IntegerField(default=0)),
                ('numSeries', models.TextField(default='')),
                ('quantity_stucked', models.IntegerField(default=0)),
                ('client', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateBon', models.DateField()),
                ('objet', models.CharField(default='', max_length=255)),
                ('message', models.TextField(default='')),
                ('reponse', models.TextField(default='')),
                ('etatFeedBack', models.CharField(choices=[('en-attente', 'en-attente'), ('en-cours', 'en-cours'), ('clos', 'clos')], default='en-attente', max_length=30)),
                ('client', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
