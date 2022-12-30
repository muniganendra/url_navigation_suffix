from django.shortcuts import render

# Create your views here.
def muni(request):
    return render(request,'muni.html')

def venkey(request):
    return render(request,'venkey.html')
