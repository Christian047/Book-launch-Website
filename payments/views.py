from django.shortcuts import render,get_object_or_404,redirect
from .models import Payment, UserWallet
from django.conf import settings
from django.contrib.auth.decorators import login_required
from base.models import *
from django.contrib import messages




@login_required
def initiate_payment(request, pk):
    single_price = get_object_or_404(PricingPlan, pk=pk)
    single_price_int = int(single_price.pricing)
    
    if request.method == "POST":
        amount = request.POST['amount']
        email = request.POST['email']
        
        payment = Payment.objects.create(amount=amount, email=email, user=request.user, plan=single_price)
        
        context = {
            'payment': payment,
            'field_values': request.POST,
            'paystack_pub_key': settings.PAYSTACK_PUBLIC_KEY,
            'amount_value': payment.amount_value(),
            'single_price': single_price,
            'single_price_int': single_price_int
        }
        return render(request, 'make_payment.html', context)
    
    return render(request, 'payment/payment.html', {'single_price': single_price, 'single_price_int': single_price_int})




@login_required
def verify_payment(request, ref):
    try:
        payment = Payment.objects.get(ref=ref)
        verified = payment.verify_payment()

        if verified:
            user_wallet, created = UserWallet.objects.get_or_create(user=request.user)
            user_wallet.balance += payment.amount
            user_wallet.save()
            messages.success(request, 'Payment successful')
        else:
            messages.error(request, 'Payment verification failed.')
    except Exception as e:
        messages.error(request, f'Error: {e}')

    return redirect('home')