from django.shortcuts import render
from .forms import ProcessForm,JokesForm
from django.http import JsonResponse
from django.http import HttpResponse
import requests
from django.conf import settings

# Create your views here.

def get(request):
    name = request.GET.get('name','None')
    return JsonResponse({'greeting':f'Hello {name}'})


def post(request):
    if request.method == 'POST': 
        form = ProcessForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            age = request.POST['age']
            salary = request.POST['salary']
            return HttpResponse(f"{name} is {age} years old and earns {salary} every month")
            
    else:
        form =  ProcessForm()    
    return render(request,'core/form.html',{'form':form})      


def fetch_jokes(request):
    if request.method == 'POST':
        form = JokesForm(request.POST)
        if form.is_valid():
            count = request.POST['count']
            jokes = []
            for _ in range(int(count)):
                api_url = 'https://api.api-ninjas.com/v1/jokes'
                response = requests.get(api_url, headers={'X-Api-Key': settings.API_NINJAS_KEY})
                if response.status_code == requests.codes.ok:
                    jokes.extend(response.json())
                else:
                    return HttpResponse(f"Error: {response.status_code} - {response.text}", status=response.status_code)
            return render(request, 'core/jokes_display.html', {'jokes': jokes})
    else:
        form = JokesForm()
    return render(request,'core/jokes_form.html',{'form':form})
