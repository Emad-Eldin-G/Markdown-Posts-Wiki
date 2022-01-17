from turtle import title
from urllib import request, response
from django import forms
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from markdown2 import markdown
from random import choice, randint
from . import util


#Form <input>s for the new_page function
class create_new(forms.Form):
    title = forms.CharField(label="Title", max_length=30)
    body = forms.CharField(label="Body", max_length=500)


class search_bar(forms.Form):
    bar = forms.CharField(label="", min_length=1, max_length=30)



#--------------------------------------------------------------------



#Lists entries on HomePage

def index(request):

    entries= util.list_entries()

    form = search_bar(request.POST)
    entries= util.list_entries()

    if request.method == "POST":
        form = search_bar(request.POST)
 
        if form.is_valid():

            results = []
            search = form.cleaned_data["bar"]
            search = str(search)

            if search != "":

                for entry in entries:

                    if search == entry:
                        return HttpResponseRedirect('/wiki/' + entry)

                    if search.lower() in entry.lower():
                        results.append(entry)

                if results != []:
                    return render(request, "encyclopedia/SearchResults.html", {'entries': results, 
                    "Searchq": search,
                    'searchform': form}) 



            else:
                return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries(),
                'searchform': form
                })





    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        'searchform': form
    })



#-------------------------------------------------------------------- 



def entry(request, entry):

    content = util.get_entry(entry.strip())
    body = markdown(content)

    form = search_bar(request.POST)
    entries= util.list_entries()

    if request.method == "POST":
        form = search_bar(request.POST)
 
        if form.is_valid():

            results = []
            search = form.cleaned_data["bar"]
            search = str(search)

            if search != "":

                for entry in entries:

                    if search == entry:
                        return HttpResponseRedirect('/wiki/' + entry)

                    if search.lower() in entry.lower():
                        results.append(entry)

                if results != []:
                    return render(request, "encyclopedia/SearchResults.html", {'entries': results, 
                    "Searchq": search,
                    'searchform': form}) 



            else:
                return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries(),
                'searchform': form
                })


    return render(request, "encyclopedia/EntryPage.html", {
        "body": body,
        "title": entry,
        })


#--------------------------------------------------------------------


def edit(request, entry):

    content = util.get_entry(entry)

    form = search_bar(request.POST)
    entries= util.list_entries()

    if request.method == "POST":
        form = search_bar(request.POST)
 
        if form.is_valid():

            results = []
            search = form.cleaned_data["bar"]
            search = str(search)

            if search != "":

                for entry in entries:

                    if search == entry:
                        return HttpResponseRedirect('/wiki/' + entry)

                    if search.lower() in entry.lower():
                        results.append(entry)

                if results != []:
                    return render(request, "encyclopedia/SearchResults.html", {'entries': results, 
                    "Searchq": search,
                    'searchform': form}) 



            else:
                return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries(),
                'searchform': form
                })

    if request.method == "POST":

        Title = request.POST['TITLE']
        Body = request.POST['BODY']

        util.save_entry(Title, Body)

        return HttpResponseRedirect("/wiki/" + Title)
    
    return render(request, "encyclopedia/edit.html", { "title": entry, "body": content})

    

    


#--------------------------------------------------------------------

#We use HttpResponseRedirect instead of render 

def random_entry(request):

    entry = choice(util.list_entries())
    return HttpResponseRedirect("/wiki/" + entry)


#--------------------------------------------------------------------



#Function to create a new wikipedia entry
def new_page(request):

    form = create_new(request.POST)
    entries= util.list_entries()
    
    
    if request.method == "POST":
        form = create_new(request.POST)


        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]

            for entry in entries:

                #Checks if there are no matching entries to continue
                if title != entry:
                    util.save_entry(title, body)

                    new_entry = util.get_entry(title)

                    return render(request, 'encyclopedia/NewResponse.html', {"content": new_entry,
                    "title": title})

                else:
                    new_entry = util.get_entry(title)
                    return render(request, 'encyclopedia/NewResponseN.html', {"content": new_entry,
                    "title": title})


        else:
            return HttpResponse("Please try again")
    
    return render(request, 'encyclopedia/New.html', {'form': form})






