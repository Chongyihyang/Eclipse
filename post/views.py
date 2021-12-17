from django.shortcuts import *
from.models import *
import secrets
from PIL import Image as img
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

def home(request):
    print(str(request.user))
    return render(request, 'post/home.html', {
        'post_title':list(Post.objects.all().values()[::-1]),
        'uu':str(request.user),
        })

def addPost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            title=request.POST.get('title')
            description=request.POST.get('description')
            images=request.FILES.getlist('images')
            videos=request.FILES.getlist('videos')

            if len(images)+len(videos) > 5 or title=='':
                return render(request, 'post/addPost.html') 
            form_obj=Post.objects.create(title=title,description=description,user=request.user)
            for images in images:
                pass
            for videos in videos:
                pass
            return redirect("/")
        else:
            return render(request, 'post/addPost.html')
    else:
        return redirect("/login")
        
def editpage(request, pk):
    user = str(Post.objects.get(pk=pk).user)
    print(user + "\n" + str(request.user))
    if str(request.user) == user:      
        if request.method=="POST":
            title=request.POST.get('title')
            description=request.POST.get('description')
            Post.objects.filter(pk=pk).update(title=title,description=description,user=request.user)
            return redirect("/")
        else:
            context = {
            'post':Post.objects.get(id=pk),
            }
            return render(request, 'post/edit.html', context)
    else:
        return redirect("/")

def detail(request,pk):
    form_obj = None
    user = str(Post.objects.get(pk=pk).user)
    if str(request.user) == user:      
        usercorrect = "yes"
    else:
        usercorrect = None
    print(f"usercore:{usercorrect}")
    print(f"BASE_DIR:{BASE_DIR}")
    commenta = None
    img = []
    vid = []
    lenimg = []
    listvid1 = []
    listvid2 = []
    nonetype = "yes"
    for i in Image.objects.filter(post_id=pk).values_list("image",flat=True):
        img.append(i)
    print(img)
    for i in Video.objects.filter(post_id=pk).values_list("video",flat=True):
        vid.append(i)
    for i in range(2,len(img)+len(vid)+1):
        lenimg.append(i)
    if img :
        listimg1 = img[0]
        listimg2 = img[1::]
    else:
        listimg1 = None
        listimg2 = None
    if vid and img == []:
        listvid1 = vid[0]
        listvid2 = vid[1::]
        print(1)
    elif vid and img != []:
        listvid1 = None
        listvid2 = vid
        print(2)
    elif vid is None:
        listvid1 = []
        listvid2 = []
        print("\n" + 3 + "\n")
    if img == [] and vid ==[]:
        nonetype = None
    if img == [] and vid !=[]:
        nonetype = "yes"
    print(nonetype)
    comments=Comment.objects.filter(post_id=pk)
    context = {
        'post':Post.objects.get(id=pk),
        'image1': listimg1,
        'img': listimg2,
        'video1':listvid1,
        'vid':listvid2,
        'lenimg': lenimg,
        'Nonetype':nonetype,
        'usercorrect':usercorrect,
        'uu':user,
        'comments':comments,
        }
    if request.user.is_authenticated:
        if request.method=='POST':
            commenta=request.POST.get('comment')
            if commenta == "":
                return HttpResponseRedirect(f'/post/{pk}')
            Comment.objects.create(post=Post.objects.get(pk=pk), 
            user=request.user, 
            comment=commenta)
            return HttpResponseRedirect(f'/post/{pk}')
    if nonetype is None:
        return render(request,'post/detailfree.html',context)
    else:
        return render(request,'post/detail.html',context)

def delete(request, pk):
    user = str(Post.objects.get(pk=pk).user)
    if str(request.user)== user:      
        usercorrect = "yes"
    else:
        usercorrect = None
    if usercorrect == "yes":
        Post.objects.filter(pk=pk).delete()
        Image.objects.filter(pk=pk).delete()
        
        Video.objects.filter(pk=pk).delete()
        Comment.objects.filter(pk=pk).delete()
    else:
        return redirect('/')
    return redirect("/")

def deletecomment(request, id):
    user = str(Comment.objects.get(id=id).user)
    if str(request.user)== user:      
        usercorrect = "yes"
    else:
        usercorrect = None
    if usercorrect == "yes":
        postid=Comment.objects.get(id=id).post_id
        Comment.objects.filter(id=id).delete()
        return HttpResponseRedirect(f'/post/{postid}')
    else:
        return redirect('/')
        
