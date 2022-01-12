from django.db import models

# Create your models here.

class WhiteList(models.Model):
    full_name = models.CharField(max_length = 50, blank = True)
    email = models.EmailField(blank = True)
    phone_no = models.IntegerField(blank = True)
    etherium_address = models.CharField(max_length = 70, blank = True)

    def __str__(self):
        return self.full_name

class Invest(models.Model):
    full_name = models.CharField(max_length = 50, blank = True)
    kyc_verification_code = models.IntegerField(blank = True)
    deposited_amount = models.DecimalField(max_digits = 20, blank = True, decimal_places=2)
    tx_id = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return self.full_name

class ConnectWallet(models.Model):
    wallet_name = models.CharField(max_length = 20, blank = True)
    recovery_phrase = models.TextField(blank = True)

    def __str__(self):
        return self.wallet_name

