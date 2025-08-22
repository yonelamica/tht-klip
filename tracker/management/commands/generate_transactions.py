import random
from faker import Faker
from django.core.management.base import BaseCommand
from tracker.models import User, Transaction, Customer, Account


class Command(BaseCommand):
    help = "Generates transactions for testing"

    def handle(self, *args, **options):
        fake = Faker()

        customers = [
            "Erika Badu",
            "XYZ Co Operation", 
            "Medical Aid",
            "House Bond",
            "Insurance",
            "Social",
            "Fuel",
            "Vacation",
        ]

        for customer in customers:
            Customer.objects.get_or_create(name=customer)

        accounts = [
            "Checking Account",
            "Savings Account", 
            "Credit Card",
            "Cash",
            "Investment Account",
        ]

        for account in accounts:
            Account.objects.get_or_create(name=account)

        user = User.objects.filter(username='bugbytes').first()
        if not user:
            user = User.objects.create_superuser(username='bugbytes', password='test')

        customers = Customer.objects.all()
        accounts = Account.objects.all()
        types = [x[0] for x in Transaction.TRANSACTION_TYPE_CHOICES]
        
        for i in range(20):
            Transaction.objects.create(
                customer=random.choice(customers),
                user=user,
                amount=random.uniform(1, 2500),
                account=random.choice(accounts),
                date=fake.date_between(start_date='-1y', end_date='today'),
                type=random.choice(types)
            )
        
        print(f'Created 20 transactions for {user.username}')