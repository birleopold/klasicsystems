from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact, Contact_us

def contact(request):
  if request.method == 'POST':
    product_id = request.POST['product_id']
    product_title = request.POST['product_title']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(product_id=product_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'you have inquired already')
        return redirect('home')

    contact = Contact(product_title=product_title, product_id=product_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('home')
  




def contact_us(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
        

    contact_us = Contact_us(name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact_us.save()

    messages.success(request, 'Your request has been submitted, we will get back to you soon')
    return redirect('home')
  return render(request, 'contact_us.html')

