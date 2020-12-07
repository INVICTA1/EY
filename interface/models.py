from django.db import models
from django.utils import timezone


# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(default=timezone.now)


class Row(models.Model):
    file_id = models.ForeignKey(File, related_name="details",on_delete=models.CASCADE)
    bank_account = models.DecimalField(),
    incoming_saldo_asset = models.DecimalField(),
    incoming_saldo_liabilities = models.DecimalField(),
    turnover_credit = models.DecimalField(),
    turnover_debit = models.DecimalField(),
    outgoing_saldo_asset = models.DecimalField(),
    outgoing_saldo_liabilities = models.DecimalField(),
    class_type = models.CharField
