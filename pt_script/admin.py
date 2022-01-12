from django.contrib import admin
from .models import Invest, WhiteList, ConnectWallet
# Register your models here.

admin.site.register(Invest)
admin.site.register(WhiteList)
admin.site.register(ConnectWallet)
