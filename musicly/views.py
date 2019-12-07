from django.shortcuts import render
from .models import Music

singer = ''

def get_singer(s):
    singer = s

def music_list(request):
    musics = Music.objects.all()
    return render(request, 'musicly/music_list.html', {'musics':musics})

def musics_bySinger(request, singer):
    musics_bySinger = Music.objects.filter(music_singer = singer)
    return render(request, 'musicly/musics_bySinger.html', {'musics_bySinger':musics_bySinger})
