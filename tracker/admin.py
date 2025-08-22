from django.contrib import admin
from tracker.models import Customer, Transaction

# Register your models here.
admin.site.register(Transaction)
admin.site.register(Customer)