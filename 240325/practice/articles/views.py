from django.shortcuts import render
from . import Article
# Create your views here.
def index(request):
    # 전체 게시글 조회해서 저장.
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'index.html')