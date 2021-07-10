from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import util

#Create your views here

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,title):
    page = util.get_entry(title)

    if page is None:
        # no page found
        return render(request,"encyclopedia/error.html",{
            "form:form"
        })

    #page found
    return render(request,"encyclopedia/titlepage.html",{
        'title': title,
        'content':page,
        'form':form
    })