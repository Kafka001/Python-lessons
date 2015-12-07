#-*- coding:utf-8 -*-

from django.contrib import admin

# Register your models here.
from apppshka.models import App_new
admin.site.register(App_new)
from apppshka.models import Comments
admin.site.register(Comments)