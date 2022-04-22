from django.shortcuts import render
from clientapp.myPytube import getVideoData
# Create your views here.

def home(request):
    return render(request, 'index.html')

def download(request):
    url = request.GET['urlSearch']
    data = getVideoData(url)
    return render(request, 'download.html', {'data':data})