from django.http.response import HttpResponse
from django.shortcuts import render
from markdown2 import Markdown
from . import util
from .forms import create_new
from . import forms


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    }) 

def entry_page(request, entry):
    body = util.get_entry(entry)
    markdowner = Markdown()

    return render(request, "encyclopedia/EntryPage.html", {
        "body": markdowner.convert(body),
        "title": entry,
        }) 

def new_page(request):

    form = create_new(request.POST)

    
    if request.method == "POST":
        form = create_new(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']

            util.save_entry(title, body)
            return HttpResponse("Saved Successfuly")
    
    return render(request, 'encyclopedia\New.html', {'form': form})


