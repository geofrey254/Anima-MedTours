from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
class StaticViewSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'
    def items(self):
        return ['anima_app:home', 'anima_app:about', 'anima_app:services', 'anima_app:contact']

    def location(self, item):
        return reverse(item)