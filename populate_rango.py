import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/'},
        {'title':'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/'},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/'} ]
    
django_pages = [
    {'title':'Official Django Tutorial',
     'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
    {'title':'Django Rocks',
     'url':'http://www.djangorocks.com/'},
    {'title':'How to Tango with Django',
     'url':'http://www.tangowithdjango.com/'} ]

