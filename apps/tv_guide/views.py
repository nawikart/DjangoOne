import json, requests
from django.shortcuts import render, redirect
from django.contrib import messages
from . import models as m
import apps.user.models as mu
from pprint import pprint


ApiUrl = 'http://api.tvmaze.com'

def get_request(request, url):
    response = requests.get(url)
    return json.loads(response.text)

def _like(request, user_id, movie_id):
    like = m.Like()
    check = m.Like.objects.filter(user_id=user_id, movie_id=movie_id)
    if len(check) == 0:
        like.movie_id = movie_id
        like.user_id = user_id
        return like.save()

    return False

def _unlike(request, user_id, movie_id):
    like = m.Like.objects.filter(user_id=user_id, movie_id=movie_id)
    like = like.delete()
    return like    

def get_movie_ids_liked(request, user_id):
    ids = []
    for l in m.Like.objects.filter(user_id=user_id):
        ids.append(l.movie_id)

    return ids

def get_shows(request, query):
    url = '{}/search/shows?q={}'.format(ApiUrl, query)
    shows = []
    for data in get_request(request, url):
        try:
            movie = m.Movie.objects.get(url=data['show']['url'])
            pprint(movie.name)
        except:
            movie = m.Movie()
            movie.api_id = data['show']['id']
            movie.url = data['show']['url']
            movie.name = data['show']['name']
            if data['show']['image'] != None:
                movie.image = data['show']['image']['original']               
            movie.save()

        shows.append(movie)

    return shows


def index(request):
    if 'user_id' in request.session:
        context = {
            'shows': m.Movie.objects.filter(likes__user_id=request.session['user_id']),
            'movie_id_liked': get_movie_ids_liked(request, request.session['user_id'])
        }  
                    
        return render(request, 'tv_guide/index.html', context = context)
    
    return render(request, 'tv_guide/index.html')


def search(request):
    return redirect('tv_guide:result', query=request.POST['html_query'])

def result(request, query):
    shows = get_shows(request, query)
    pprint(shows)
    movie_id_liked = []
    
    if request.session:
        movie_id_liked = get_movie_ids_liked(request, request.session['user_id'])

    context = {
        'shows': shows,
        'movie_id_liked': movie_id_liked,
        'destination': (request.path).replace('/', '||')
    }  
    
    return render(request, 'tv_guide/index.html', context = context)

def unlike(request, id, destination):
    _unlike(request, request.session['user_id'], id)

    if destination != '_':
        return redirect(destination.replace('||', '/'))
    else:
        return redirect('tv_guide:index')

def like(request, id, destination):
    _like(request, request.session['user_id'], id)
    return redirect(destination.replace('||', '/'))    