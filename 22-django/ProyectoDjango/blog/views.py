from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Category, Article

# Create your views here.

def list(request):
    # Obtener articulos
    articles = Article.objects.all()

    # Paginar los articulos
    paginator = Paginator(articles, 2)

    # Recoger numero de pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': page_articles
    })

def category(request, category_id):
    # category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category, id=category_id)
    # articles = Article.objects.filter(categories=category).all()

    return render(request, 'categories/category.html', {
        'category': category
    })

def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html', {
        'article': article
    })