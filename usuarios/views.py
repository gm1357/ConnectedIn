from django.shortcuts import render
from django.views.generic.base import View

class RegistrarUsuarioView(View):
    
    def get(self, request):
        return render(request, 'registrar.html')

    def post(self, request):
        return render(request, 'registrar.html')