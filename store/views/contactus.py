from django.shortcuts import render

def contactus(request):
    return render(request,template_name="store/contactus.html")