from django.http import HttpResponse
from .forms import ProductForm,ClientForm
from django.shortcuts import render, redirect
from .models import Client

def index(request):
    return HttpResponse("clients home page")
# def index(request):
# #     return render(request, 'clients/index.html', {'message': 'Clients Home Page'})

def header(request):
    return render(request, 'header.html')

def info(request):
    return render(request, 'info.html')

def add(request):
    return render(request, 'add.html')

def addproduct(request):
    form = ProductForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Save the product or perform any other required action
            # For simplicity, let's just increment a counter in the session
            product_count = request.session.get('product_count', 0)
            product_count += 1
            request.session['product_count'] = product_count

            return redirect('index')  # Redirect to the home page or another appropriate view

    return render(request, 'product.html', {'form': form})





def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()

    return render(request, 'clients/add.html', {'form': form})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})


