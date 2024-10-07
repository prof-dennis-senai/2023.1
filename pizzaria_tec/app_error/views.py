from django.shortcuts import render

# Create your views here.
def erro_404(request):
    return render(request, '404.html')