from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView
from . import views
from models import Entry

urlpatterns = patterns('',
    url(r'^$', views.blog_index, name="index"),
    url(r'^about-me/', views.about_me, name="about_me"),
    url(r'^archive/', views.archive_index, name="archive"),
    url(r'^tags/(?P<tag>\S+)$', views.tag_index, name="tag_index"),
    url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
)