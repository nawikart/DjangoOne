from django.shortcuts import render, redirect
from django.contrib import messages
from . import models as m

# Create your views here.
def index(request):
    if request.method == 'POST':
        try:
            bill = m.Bill()
            bill.description = request.POST['html_description']
            bill.amount = request.POST['html_amount']
            bill.user_id = request.session['user_id']
            bill.save()
        except:
            messages.error(request, 'invalid input')


    context = {
        'all_bills': m.Bill.objects.filter(user_id=request.session['user_id'])
    }    
    return render(request, 'bill_tracker/index.html', context = context)


def edit(request, id):
    bill = m.Bill.objects.get(id=id)

    if request.method == 'POST':
        try:
            bill.description = request.POST['html_description']
            bill.amount = request.POST['html_amount']
            bill.save()
            return redirect('bill_tracker:index')
        except:
            messages.error(request, 'invalid input')

    context = {
        'bill': bill
    } 

    return render(request, 'bill_tracker/edit.html', context = context)


def delete(request, id):
    bill = m.Bill.objects.get(id=id)
    bill.delete()
    return redirect('bill_tracker:index')