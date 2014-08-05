from django.views import generic
from django.shortcuts import render
from . import models


def blog_index(request, 
               template = 'blog/index.html', 
               page_template = 'blog/paginated.html'):
    context = {'entries': models.Entry.objects.published(),
               'page_template': page_template}
    if request.is_ajax():
        template = page_template
    return render(request, template, context)

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "blog/entry.html"

def tag_index(request, tag, template = "blog/tag.html"):
    context = {'entries': models.Entry.objects.published().filter(tags__slug= tag),
               'tag': tag}
    return render(request, template, context)

def archive_index(request, template = "blog/archive.html"):
    context = {'entries': models.Entry.objects.published()}
    return render(request, template, context)

def about_me(request, template = "blog/about_me.html"):
    context = {'entries': models.Entry.objects.filter(slug='from_art_to_code')}

    return render(request, template, context)

