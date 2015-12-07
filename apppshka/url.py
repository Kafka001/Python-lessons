#-*- coding:utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index_page"),
    url(r'^page/(?P<id>\d+)/$', views.page, name="inner_page"),
    # url (r'^page/$', views.comments_visitors, name="comments_visitors"),
    url(r'^about/$', views.about, name="about_page"),
    url(r'^comments/$', views.comments, name="comments_page"),
    url (r'^contact/$', views.contact, name="contact_page"),
    url (r'^project_discription/$', views.project_discr, name="project_discr"),

]
