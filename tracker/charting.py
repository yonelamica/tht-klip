import plotly.express as px
from django.db.models import Sum
from tracker.models import Customer


def plot_income_debits_bar_chart(qs):
    x_vals = ['Credit', 'Debit']

    # sum up the total credit and Debit
    total_credit = qs.filter(type='credit').aggregate(
        total=Sum('amount')
    )['total']
    total_debit = qs.filter(type='debit').aggregate(
        total=Sum('amount')
    )['total']

    fig = px.bar(x=x_vals, y=[total_credit, total_debit])

    return fig

def plot_customer_pie_chart(qs):
    count_per_customer = (
        qs.order_by('customer').values('customer')
        .annotate(total=Sum('amount'))
    )
    customer_pks = count_per_customer.values_list('customer', flat=True).order_by('customer')
    customer= Customer.objects.filter(pk__in=customer_pks).order_by('pk').values_list('name', flat=True)
    total_amounts = count_per_customer.order_by('customer').values_list('total', flat=True)

    fig = px.pie(values=total_amounts, names=customer)
    fig.update_layout(title_text="Total Amount per Customer")
    return fig