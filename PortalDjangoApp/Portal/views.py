from django import template as template_engine
from django.http import Http404
from django.http import HttpResponse

from .models import NewsHeading


def get_news_context(domain=None):
    if domain:
        if domain == "tecmundo":
            all_news = NewsHeading.objects.filter(
                read_more__startswith="https://www.tecmundo.com.br"
            )
            domain = 'TecMundo'
        else:
            raise Http404("Domain not supported at this time!")
    else:
        all_news = NewsHeading.objects.all()
    return {"all_news": all_news, "filtered": domain}


def index(request):
    template = template_engine.loader.get_template("Portal/index.html")
    return HttpResponse(template.render(get_news_context(), request))


def list_domain(request, domain):
    template = template_engine.loader.get_template("Portal/index.html")
    return HttpResponse(template.render(get_news_context(domain), request))
