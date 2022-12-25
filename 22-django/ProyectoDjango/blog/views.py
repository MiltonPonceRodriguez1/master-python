from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Category, Article
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='login')
def list(request):
    # Obtener articulos
    articles = Article.objects.all()

    # Paginar los articulos
    paginator = Paginator(articles, 4)

    # Recoger numero de pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': page_articles
    })

@login_required(login_url='login')
def category(request, category_id):
    # category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category, id=category_id)
    # articles = Article.objects.filter(categories=category).all()

    return render(request, 'categories/category.html', {
        'category': category
    })

@login_required(login_url='login')
def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html', {
        'article': article
    })

@csrf_exempt
def test(request):
    if request.method == 'POST':
        response = {
            'name': 'milton',
            'surname': 'ponce'
        }
    elif request.method == 'PUT':
        response = {
            'method': 'PUT',
            'surname': 'ponce'
        }
    elif request.method == 'DELETE':
        response = {
            'method': 'DELETE',
            'surname': 'ponce'
        }
    elif request.method == 'GET':
        response = {
            'method': 'GET',
            'name': 'milton'
        }
    else:
        response = {
            'error': 'NO ES NINGUNA HTTP REQUEST'
        }

    return JsonResponse(response)