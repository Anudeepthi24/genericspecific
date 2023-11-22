from django.shortcuts import render

# Create your views here.
def gani(request):
    return render(request,'gani.html')

def ram(request):
    return render(request,'ram.html')