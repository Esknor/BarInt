from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# home_page = None

# def home_page():
def home_page(request):
    # return render(request, 'home/home.html')
    my_dict = {'key':'My dikt Key'}
    my_list = [1,2,3,4]
    categories = [{'id':0,'name':'Python'},{'id':1,'name':'Django'},{'id':2,'name':'Web'},{'id':4,'name':'Javascript'}]

    cities = [
    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
    ]

    return render(request, 'bar/index.html', {'first_name': 'Billi', 'last_name': 'Bons', 'my_dict':my_dict,'my_list':my_list,'name':'<script>alert("XSS");</script>','rowclass1':'border: red solid 7px;', 'rowclass2':'border: green solid 3px;','categories':categories,'cities':cities})

def home(request):
    return render(request, "bar/index.html", {})
