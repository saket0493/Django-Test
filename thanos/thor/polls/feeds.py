from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    title = "My blog"
    link = reverse_lazy("polls:post_list")
    description = "New posts of my blog."

    def items(self):
        return Post.published.all()[:0]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
