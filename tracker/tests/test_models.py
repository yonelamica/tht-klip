import pytest
from tracker.models import Transaction


@pytest.mark.django_db
def test_queryset_get_credit_method(transactions):
    qs = Transaction.objects.get_income()
    assert qs.count() > 0
    assert all(
        [transaction.type == 'credit' for transaction in qs]
    )

@pytest.mark.django_db
def test_queryset_get_debit_method(transactions):
    qs = Transaction.objects.get_expenses()
    assert qs.count() > 0
    assert all(
        [transaction.type == 'debit' for transaction in qs]
    )

@pytest.mark.django_db
def test_queryset_get_total_credit_method(transactions):
    total_credits = Transaction.objects.get_total_credits()
    assert total_income == sum(t.amount for t in transactions if t.type == 'credit')

@pytest.mark.django_db
def test_queryset_get_total_debit_method(transactions):
    total_debits = Transaction.objects.get_total_debits()
    assert total_debits == sum(t.amount for t in transactions if t.type == 'debit')