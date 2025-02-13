from django.shortcuts import render
from django import forms
from django.shortcuts import redirect
from django.urls import reverse

from . import util


import random
import markdown2


class CreateNewEntryForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50)
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={"rows":6, "cols":50}))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def getEntry(request, entry):
    content = util.get_entry(entry)
    content = markdownToHtml(content)
    if content:
        return render(request, "encyclopedia/entry.html", {
            "entry": entry,
            "content": content
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": entry,
            "content": None
        })
    
def searchEntries(request):
    query = request.GET.get('q', '').lower() # valor da consulta convertido para minúsculo
    entries = util.list_entries()
    
    for entry in entries:
        if query == entry.lower():
            return getEntry(request, entry)
        
    matchingEntries = []
    for entry in entries:
        if query in entry.lower():
            matchingEntries.append(entry)

    if matchingEntries:
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "entries": matchingEntries
        })
    else:
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "entries": []
        })
    
def createEntry(request):
    entries = util.list_entries()
    if request.method == "POST":
        form = CreateNewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if title.lower() in [entry.lower() for entry in entries]:
                return render(request, "encyclopedia/create.html", {
                    "form": form,
                    "error":"An entry with this title already exists!",
                    "title": title,
                    "content": content
                })
            else:
                util.save_entry(title, content)
                return redirect(reverse("entries:entry", args=[title]))
        else:
            return render(request, "encyclopedia/create.html", {
                "form": form
            })
    return render(request, "encyclopedia/create.html", {
        "form": CreateNewEntryForm()
    })


def editEntry(request, entry):
    if request.method == "POST":
        form = CreateNewEntryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"].strip()
            if content:
                util.save_entry(entry, content)
                return redirect(reverse("entries:entry", args=[entry]))
            else:
                form.add_error("content", "Please enter some content!")
    else:
        content = util.get_entry(entry)
        form = CreateNewEntryForm(initial={"title": entry, "content": content})

    return render(request, "encyclopedia/edit.html", {
        "form": form,
        "title": entry
    })

def randomEntry(request):
    entries = util.list_entries()
    if not entries:
        return redirect(reverse("entries:index"))
    entry = random.choice(entries)
    return redirect(reverse("entries:entry", args=[entry]))


def markdownToHtml(markdownContent):
    htmlContent = markdown2.markdown(markdownContent)
    return htmlContent
