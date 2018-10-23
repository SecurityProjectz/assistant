from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'metrics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'landing/$',views.landing ,name='landing'),
    url(r'guage/$',views.guage ,name='guage'),
]
