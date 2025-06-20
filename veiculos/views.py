from django.shortcuts import render
from .models import Veiculo
from .forms import VeiculoForm
from django.shortcuts import redirect

def home(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'veiculos/home.html', {'veiculos': veiculos})


def cadastrar_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VeiculoForm()
    return render(request, 'veiculos/cadastrar.html', {'form': form})