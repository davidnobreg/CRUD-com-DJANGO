from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import ClienteForm
from .models import Cliente


def insert(request):
    clientes = Cliente.objects.filter(is_ativo=False)  
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente salvo com sucesso!")  
            return redirect('cliente-create')
         
    context = {
        'clientes': clientes,
        'form': form
    } 
    return render(request, 'cliente.html', context)

def update(request, id):
    cliente = get_object_or_404(Cliente, id=id)
        
    name =  request.POST.get('name')
    email =  request.POST.get('email')
    phone =  request.POST.get('phone')
    
    cliente.name = name
    cliente.email = email
    cliente.phone = phone
               
    cliente.save()
    messages.success(request, "Cliente atualizado com sucesso!")   
    return redirect('cliente-create')

def delete(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.is_ativo=True
    cliente.save()
    messages.success(request, "Cliente deletado com sucesso!")  
    return redirect('cliente-create')

