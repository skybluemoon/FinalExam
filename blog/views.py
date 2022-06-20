from django.shortcuts import render

# Create your views here.
def index(Req):
    context={

    }
    return render(req, "index.html", context=context)