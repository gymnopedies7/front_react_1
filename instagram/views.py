from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')  # q 포함되는 대상이 있으면 가져오고, 없으면 None 반환
    if q:
        qs = qs.filter(message__icontains=q)
    # instagram/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html',{'post_list':qs, 'q':q, } )

