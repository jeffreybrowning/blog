from django.contrib.syndication.views import Feed
from blog.models import Entry

class Posts(Feed):
    title = "Art to Code"
    link = '/feed/'
    description = "Latest posts"

    def items(self):
        return Entry.objects.published()[:5]

