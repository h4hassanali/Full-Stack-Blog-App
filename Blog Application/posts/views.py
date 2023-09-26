from django.shortcuts import render
from posts.models import post
# Create your views here.
def index(request):
    posts = post.objects.all()
    return render(request,'index.html',{'posts':posts})

def post1(request,pk):
    pst = post.objects.get(id=pk)
    return render(request,'post.html',{'post':pst})