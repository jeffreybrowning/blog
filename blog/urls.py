from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView
from . import views
from models import Entry

urlpatterns = patterns('',
#    url(r'^$', views.BlogIndex.as_view(), name="index"),
#    url(r'^$', ListView.as_view(model=Entry, 
#                                paginate_by=2, 
#                                template_name="blog/index.html"), name="index"),
    url(r'^$', views.blog_index, name="index"),
    url(r'^tags/(?P<tag>\S+)$', views.TagDetail.as_view(), name="tag_detail"),
    url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
)