from django.views.generic import ListView
from django.shortcuts import render
from .models import Post

#post_list=  ListView.as_view(model=Post)  : 아래와 동일하게 할수있으나, 너무 마법같고, 추후 커스터마이징이 안됨

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')  # q 포함되는 대상이 있으면 가져오고, 없으면 None 반환
    if q:
        qs = qs.filter(message__icontains=q)
    # instagram/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html',{'post_list':qs, 'q':q, } )

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")


def post_detail(request,pk):
    pass