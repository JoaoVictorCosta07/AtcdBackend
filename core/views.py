from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente

def home(request):
    if request.method == 'POST':
        nome = request.POST.get('name')
        e_mail = request.POST.get('email')
        whatsapp = request.POST.get('whatsapp')

        Cliente.objects.create(nome=nome, e_mail=e_mail, whatsapp=whatsapp)

        return HttpResponse('sucesso')

    return render(request, 'index.html')