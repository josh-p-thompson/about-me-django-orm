from django.shortcuts import render
from django.http import HttpResponse
import markdown
from .models import About, Project

# Create your views here.
def index(request):
    print('---------- rendering About')
    cards = []
    for about in About.objects.all(): 
        cards.append({
            'title': about.title,
            'sub_title_1': about.sub_title_1,
            'sub_title_2': about.sub_title_2,
            'content_1': about.content_1,
            'content_2': about.content_2,
        })
    context = {
        'title': 'about',
        'path': '/', 
        'cards': cards,
        'pages': pages(),
    }
    return render(request, 'index.html', context)

def projects(request):
    print('---------- rendering Projects')
    cards = []
    for project in Project.objects.all(): 
        cards.append({
            'title': project.title,
            'sub_title': project.sub_title,
            'link': project.link,
            'image': project.image,
        })
    context = {
        'title': 'projects',
        'path': 'projects', 
        'cards': cards,
        'pages': pages(),
    }
    return render(request, 'projects.html', context)

def pages(): 
    return [
        {'title': 'about', 'path': '/'}, 
        {'title': 'projects', 'path': 'projects'}, 
    ]

def markdown_convert(text): 
    md = markdown.Markdown(extensions=["markdown.extensions.meta", "markdown.extensions.attr_list", "markdown.extensions.extra"])
    data = text
    return md.convert(text)
