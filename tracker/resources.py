from import_export import resources, fields
from tracker.models import Transaction, Customer
from import_export.widgets import ForeignKeyWidget

class TransactionResource(resources.ModelResource):
    customer = fields.Field(
        column_name='customer',
        attribute='customer',
        widget=ForeignKeyWidget(Customer, field='name')
    )

    def after_init_instance(self, instance, new, row, **kwargs):
        instance.user = kwargs.get('user')

    class Meta:
        model = Transaction
        fields = (
            'amount',
            'type',
            'date',
            'customer',
            'account',
        )
        import_id_fields = (
            'amount',
            'type',
            'date',
            'customer',
            'account',    
        )