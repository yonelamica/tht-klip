from django import forms
from tracker.models import Transaction, Customer


class TransactionForm(forms.ModelForm):
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        required=False,
       widget=forms.Select(attrs={'class': 'Select Existing Customer name','class': 'form-control'})

    )

    new_customer = forms.CharField(
        max_length=20,
        required=False,
        widget= forms.TextInput(attrs={'placeholder': 'Or Enter new customer name','class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        customer = cleaned_data.get('customer')
        new_customer = cleaned_data.get('new_customer')
        
        if not customer and not new_customer:
            raise forms.ValidationError("Either select existing customer or enter new customer name")
        
        if new_customer:
            customer, created = Customer.objects.get_or_create(name=new_customer)
            cleaned_data['customer'] = customer
            
        return cleaned_data


    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise forms.ValidationError("Amount must be a positive number")
        return amount

    class Meta:
        model = Transaction
        fields = (
            'type',
            'amount',
            'date',
            'customer',
            'account',
            
        )
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }