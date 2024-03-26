from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):        # 처음 들어가는 request는 불변. 다음 매개변수 pk는 urls.py와 같은 변수명으로!
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # print(request.GET)   # GET에 QueryDict 형태로 데이터가 들어가 있다. 작성자가 작성한title과 content가 들어가 있음.

    title = request.POST.get('title')
    content = request.POST.get('content')

    # #첫번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()


    # 두번째 방법
    article = Article(title=title, content=content)
    # 유효성 검증을 위해 save를 뒤로 빼준다.
    article.save()
    # post로 작성을 마쳤다면, redirect로 사용자를 다른 페이지로 보내줘야 한다. 
    # return render(request, 'articles/create.html')
    return redirect('articles:detail', article.pk)
    # 파이썬이기 때문에 url 태그는 못 씀. 
    # save가 된 이후에는 id가 부여된 인스턴스가 되어서 article.pk로 불러낼 수 있음.
    # 지금 막 작성이 완료된 객체의 id. 

    # #세번째 방법
    # Article.objects.create(title=title, content=content)
    # return render(request, 'articles/create.html')

def delete(request, pk):
    # 몇번 글을 삭제할지 -> 조회 먼저 필요
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk) #수정 대상 조회
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html')

def update(request):

    # 몇 번 게시글 수정? -> 조회
    article = Article.objects.get(pk=pk)
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 두번째 방법
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)
