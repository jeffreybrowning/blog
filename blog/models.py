from django.db import models
from django.core.urlresolvers import reverse

class EntryQuerySet(models.QuerySet): # for filtering published shit
    def published(self):
        return self.filter(publish=True)

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __unicode__(self):
        return self.slug

class Entry(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length= 50)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique = True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)

    objects = EntryQuerySet.as_manager() #this is handled by entryqueryset, and makes it so the collection obj is filterable, neato

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})

    @property 
    def get_prev(self):
        next = Entry.objects.filter(id__lt=self.id)
        if next:
            return next[0]
        return False

    @property
    def get_next(self):
        prev = Entry.objects.filter(id__gt=self.id)
        length = len(prev)
        if prev:
            return prev[length-1]
        return False

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]

