from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .forms import CreateOrderForm
from main.models import Book
from .models import Order
def create_order(request, book_id):
    book = Book.objects.get(id=book_id)
    print(request.POST) #POST contains the info user entered in the form
    order_form = CreateOrderForm(request.POST)
    if order_form.is_valid():
        print(order_form.cleaned_data)
        order_form.save()
        return redirect(book.get_absolute_url())
        # return render(request, 'order/order.html', {'form': order_form,
        #                                             'book':book})
       # order = Order.objects.create(**order_form.cleaned_data) #dictionary that contains all the filtered data we need
    order_form = CreateOrderForm()
    return render(request, 'order/order.html', {'form':order_form,
                                                'book': book})

