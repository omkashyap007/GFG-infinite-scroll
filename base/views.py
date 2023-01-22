from django.shortcuts import render
from base.models import Post
from django.http import JsonResponse
from django.core.paginator import Paginator
import json

def homePage(request):

    posts = Post.objects.all()
    paginator = Paginator(posts , 10)
    posts = paginator.page(1)
    context = {"posts" : posts}
    return render(request , "base/homePage.html" , context = context)

def convertPyToJS(objects):
    l = []
    for i in objects:
        l.append(
            { 
                "username" : i.user.username ,
                "title" : i.title , 
                "content" : i.content , 
                "id" : i.id , 
            }
        )
    return l

def postLoader(request):
    if request.method == "POST":
        posts = Post.objects.all()
        page_number = int(request.POST.get("page_number"))
        paginator = Paginator(posts , 10)
        if page_number <= paginator.num_pages: 
            posts = paginator.page(page_number)
            post_data = convertPyToJS(posts)
            data = {
                "new_page_number" : int(page_number) + 1 , 
                "data" : post_data , 
            }
            return JsonResponse(data , safe = False)
        return JsonResponse({
            "no_data" : "no_data" ,
        })