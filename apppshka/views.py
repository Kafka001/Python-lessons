#-*- coding:utf-8 -*-

from django.shortcuts import render, get_object_or_404
from models import App_new
from forms import NewForm
from forms import CommentsForm
from models import Comments
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    o = App_new.objects.all()
    return render(request, 'apppshka/index1.html', {'all': o})

def page(request, id):
    p = get_object_or_404(App_new, pk=id)
    form_comment=CommentsForm()
    com = Comments.objects.filter(page=p)

    if request.method=="POST":
        form_comment = CommentsForm(request.POST)
        if form_comment.is_valid():
            Comments.objects.create(**{'comment_content':request.POST.get('comment_content'),
                                       'comment_author':request.POST.get('comment_author'), 'page': p})
            return HttpResponseRedirect('/')
    return render(request, 'apppshka/page.html', {'page': p, 'form_comment':form_comment, 'comments':com})

def about(request):
    return render(request, 'apppshka/about.html')

def comments(request):
    form = NewForm()
    if request.method=="POST":
        form = NewForm(request.POST)
        if form.is_valid():
            App_new.objects.create(**{'field1':request.POST.get('field1'), 'field2':request.POST.get('field2')})
            return HttpResponseRedirect('/')
    return render(request, 'apppshka/comments.html', locals())

# def comments_visitors(request):
#     form_comment = CommentsForm()
#     if request.method=="POST":
#         form_comment = CommentsForm(request.POST)
#         if form_comment.is_valid():
#             Comments.objects.create(**{'comment_content':request.POST.get('comment_content'), 'comment_author':request.POST.get('comment_author')})
#             return HttpResponseRedirect('/')
#     return render(request, 'apppshka/page.html', locals())


def contact(request):
    return render(request,'apppshka/contact.html')

def project_discr(request):
    return render(request,'apppshka/project_discr.html')