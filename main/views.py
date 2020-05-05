from django.shortcuts import render,redirect

from main.models import Blog


# Create your views here.
def home(request):
    allblog = Blog.objects.all()

    context = {
        'blogs': allblog
    }
    return render(request,'index.html',context )

def addblog(request):
    if request.method == 'GET':
        return render(request,'addblog.html')
    elif request.method == 'POST':
        blogimage = request.POST['image']
        blogtitle = request.POST['title']
        blogbody = request.POST['body']

        blog = Blog(image=blogimage, title=blogtitle, body=blogbody)
        blog.save()

        return redirect('/')
