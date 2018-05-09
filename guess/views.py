from django.shortcuts import render
from django.http import HttpResponse
import random

def hello(request):
    return HttpResponse("Hello world")

def guess(request):
    answer = random.randint(1, 5)
    if request.method == "GET":
        return render(request,template_name="index.html")
    if request.method == "POST":
        number = request.POST.get('number','')
        if int(number) == answer:
            message = "You Win!!"
        else:
            message = "Sorry You lose!. Try again"
        context = {
            "message": message
        }
        return render(request, template_name="index.html", context=context)
