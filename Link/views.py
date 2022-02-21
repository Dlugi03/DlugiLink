from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import DBLink
from .forms import LinkForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def submit_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
    
        link = str(request.POST['link-text'])
        if link is not None:
            db_link = DBLink()
            db_link.create_short_link(link_text=link)
    
        return render(request, "shortlink.html", {"short_link": str(db_link.short)})


def redirect_by_short(request, short_code):
    db_link = DBLink.objects.get(short=short_code)

    return HttpResponseRedirect(db_link.link)