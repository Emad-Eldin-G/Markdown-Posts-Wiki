from django.shortcuts import render
from markdown2 import Markdown, markdown
from . import util


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
    return render(request, "encyclopedia/New.html")

