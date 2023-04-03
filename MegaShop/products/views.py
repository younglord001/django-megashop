from django.shortcuts import render
from django.http import HttpResponse


def producthome(request):
    user='ritesh'
    return render(request, 'products/home.html', {'user': user,'product_num': 6})
    # return render(request, 'producthome.html',)

def signup(request):
    return render(request, 'products/signup.html')

def product_cat(request,product):
    if product in ["suit", "dress", "shirt", "shoes"]:
       return HttpResponse(f'this is the list of the our {product}')
    # if product =="suit" or product=="dress" or product=="shirt" or product=="shoes":
    #     return HttpResponse(f'this is the list of the our {product}') 
    else:
        return HttpResponse(f'{product}catogry won\'t exist') 
