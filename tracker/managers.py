from django.db import models 


class TransactionQuerySet(models.QuerySet):
    def get_expenses(self):
        return self.filter(type='debit')
    
    def get_income(self):
        return self.filter(type='credit')
    
    def get_total_debits(self):
        return self.get_expenses().aggregate(
            total=models.Sum('amount')
        )['total'] or 0

    def get_total_credits(self):
        return self.get_income().aggregate(
            total=models.Sum('amount')
        )['total'] or 0