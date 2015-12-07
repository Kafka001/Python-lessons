#-*- coding:utf-8 -*-
from django import forms

class NewForm (forms.Form):
    field1=forms.CharField(max_length=200)
    field2=forms.CharField(widget=forms.Textarea)

class CommentsForm (forms.Form):
    comment_content=forms.CharField(widget=forms.Textarea)
    comment_author=forms.CharField(max_length=35)