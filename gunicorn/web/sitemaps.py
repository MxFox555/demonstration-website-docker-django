from django.contrib.sitemaps import Sitemap
from django.urls import reverse, reverse_lazy

class Static_Sitemap(Sitemap):

    priority = 0.8
    changefreq = 'yearly'
    protocol = 'https'

    def items(self):
        return ['landing', 'pricing', 'contact', 'signup', 'login']

    def location(self, item):
        return reverse_lazy(item)