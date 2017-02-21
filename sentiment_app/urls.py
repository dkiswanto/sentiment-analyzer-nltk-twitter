from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^articles/2003/$', views.special_case_2003),
    # url(r'^articles/([0-9]{4})/$', views.year_archive),
    # url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    # url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
    url(r'^$', views.index),
    url(r'^dataset$', views.dataset),
    url(r'^information$', views.information),

    # url(r'^about$', views.index),
]