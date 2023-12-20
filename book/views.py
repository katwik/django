from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def book_month(request):
    return HttpResponse("This would be the book of the month page")