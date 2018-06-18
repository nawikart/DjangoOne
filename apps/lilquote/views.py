from django.shortcuts import render, redirect
from django.contrib import messages
from . import models as m
import apps.user.models as mu
from django.db.models import Q


def index(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            try:
                quote = m.Quote()
                quote.content = request.POST['html_content']
                quote.user_id = request.session['user_id']
                quote.save()
            except:
                messages.error(request, 'invalid input')

        context = {
            'all_quotes': m.Quote.objects.all()
        }    
        return render(request, 'lilquote/index.html', context = context)

    return redirect('user:index')


def delete(request, id):
    quote = m.Quote.objects.get(id=id)
    quote.delete()
    return redirect('lilquote:index')


def edit(request, id):
    quote = m.Quote.objects.get(id=id)

    if request.method == 'POST':
        quote.content = request.POST['html_content']
        quote.save()
        return redirect('lilquote:user_quotes', user_id=quote.user.id)

    context = {
        'quote': quote
    } 

    return render(request, 'lilquote/edit.html', context = context)


def user_quotes(request, user_id):
    context = {
        'all_quotes': m.Quote.objects.filter(user_id=user_id),
        'user': mu.User.objects.get(id=user_id)
    }    
    return render(request, 'lilquote/index.html', context = context)
    

def search(request):
    if request.method == 'POST':
        return redirect('lilquote:result', query=request.POST['html_query'])
    
    return render(request, 'lilquote/index.html')


def result(request, query):
    
    context = {
        'all_quotes': m.Quote.objects.filter(Q(user__email__contains=query) | Q(user__name__contains=query)),
        'query': query
    }

    return render(request, 'lilquote/index.html', context = context)    