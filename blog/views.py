from django.views import generic
from django.shortcuts import render
#from endless_pagination.views import AjaxListView
from . import models

#class BlogIndex():
#    queryset = models.Entry.objects.published()
#    template_name = "blog/index.html"
#    page_template = 'blog/paginated.html'

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


class TagDetail(generic.DetailView):
    model = models.Tag
    template_name = "blog/tag.html"
    slug_url_kwarg = "tag"