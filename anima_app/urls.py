from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import ContactView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

app_name = 'anima_app'
sitemaps = {
    'static':StaticViewSitemap #add StaticSitemap to the dictionary
}

urlpatterns = [
    path('', views.home, name='home'),
    path('Anima_MedTours/About-Us', views.about, name='about'),
    path('Anima_MedTours/Our-Services', views.services, name='services'),
    path('Anima_MedTours/Contact-Us', ContactView.as_view(), name="contact"),
    path('Anima_MedTours/Success', views.success, name='success'),
    path('Anima_MedTours/sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]