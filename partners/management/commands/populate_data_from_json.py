import json
from django.core.management.base import BaseCommand
from partners.models import Client, EtatPayement, CaPerMonth, Reglement, ProductBought

class Command(BaseCommand):
    help = 'Populate the database from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        json_file = options['json_file']

        # Load data from JSON file
        with open(json_file, 'r') as file:
            data = json.load(file)

        # Get client instance
        client = Client.objects.get(id=data['client'])

        # Create or update EtatPayement instance
        EtatPayement.objects.update_or_create(
            client=client,
            defaults={
                'chiffreAffaire': data['etat_payement']['chiffreAffaire'],
                'montantPayed': data['etat_payement']['montantPayed'],
                'montantSolde': data['etat_payement']['montantSolde'],
                'montantAnnule': data['etat_payement']['montantAnnule']
            }
        )

        # Create or update CaPerMonth instances
        for month, montant in data['ca_per_month'].items():
            CaPerMonth.objects.update_or_create(
                client=client,
                month=month,
                defaults={'montant': montant}
            )

        # Create Reglement instances
        for reglement in data['reglements']:
            Reglement.objects.update_or_create(
                client=client,
                montant=reglement['montant'],
                dateReglement=reglement['dateReglement'],
                defaults={'modeReglement': reglement['codeReglement']}
            )

        # Create ProductBought instances
        for product in data['products_bought']:
            ProductBought.objects.update_or_create(
                client=client,
                codeBl=product['codeBl'],
                dateBon=product['dateBl'],
                ProduitReference=', '.join(product['num_series']),
                ProduitName=product['reference_name'],
                defaults={
                    'quantity_bought': product['quantity'],
                    'unitprice': 0,  # Adjust if you have a specific unit price
                    'quantity_sold': 0,
                    'numSeries': ', '.join(product['num_series']),
                    'quantity_stucked': product['quantity']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
