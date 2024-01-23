from django.shortcuts import render
from django.http import HttpResponse
from rango.models import *

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    context_dict['categories'] = category_list

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')

def details(request):
    return HttpResponse("Rango says here is the details page.")