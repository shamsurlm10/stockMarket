from django.shortcuts import render, get_object_or_404, redirect
from .models import Stock
from .forms import StockForm  # Create a form for adding/editing stock data

def home(request):
    stocks = Stock.objects.all()
    return render(request, 'stocks/home.html', {'stocks': stocks})

def stock_detail(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, 'stocks/stock_detail.html', {'stock': stock})

def stock_create(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StockForm()
    return render(request, 'stocks/stock_form.html', {'form': form})

def stock_edit(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StockForm(instance=stock)
    return render(request, 'stocks/stock_form.html', {'form': form})

def stock_delete(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    stock.delete()
    return redirect('home')