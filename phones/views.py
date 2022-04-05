from pprint import pprint
from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    option = request.GET.get('sort')
    template = 'catalog.html'
    ret_arr = []
    
    if option == 'min_price':
        phone_obj = Phone.objects.all().order_by('price')
        for phone in phone_obj:
            ret_arr.append(phone)
            print(phone.slug)
    elif option == 'name':
        phone_obj = Phone.objects.all().order_by('name')
        for phone in phone_obj:
            ret_arr.append(phone)
    elif option == 'max_price':
        phone_obj = Phone.objects.all().order_by('-price')
        for phone in phone_obj:
            ret_arr.append(phone)    
    else:
        phone_obj = Phone.objects.all()
        for phone in phone_obj:
            ret_arr.append(phone)
        
    context = {
        'phones':ret_arr
    }
    
    return render(request, template, context)


def show_product(request, slug):
    phone_obj = Phone.objects.all()
    template = 'product.html'
    
    for phone in phone_obj:
        if slug.lower() == phone.name.replace(' ', '-').lower():
            context = {
            'phone': phone
        }
            
    return render(request, template, context)
