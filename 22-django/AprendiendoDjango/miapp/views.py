from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages

# Create your views here.

# MVC: MODELO VISTA CONTROLADOR -> Acciones (metodos)
# MVT: MODELO TEMPLATE VISTA -> Acciones (metodos)

layout = """
    <h1>Sitio Web con Django | Milton Ponce</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/hola-mundo">Hola Mundo</a>
        </li>
        <li>
            <a href="/pagina-pruebas">Pagina de pruebas</a>
        </li>
        <li>
            <a href="/contacto-dos">Contacto</a>
        </li>
    </ul>
    <hr/>
"""

def index(request):
    """
    html = ""
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
    ""
    for x in range(2022, 2051):
        if x % 2 == 0:
            html += f"<li>{str(x)}</li>"

    html += "</ul>"
    """
    years = range(2022, 2051)

    nombre = 'Milton Ponce'
    lenguajes = ['JavaScript', 'Python', 'PHP', 'C']

    # return HttpResponse(layout+html)
    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un Dato que esta en la Vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': years
    })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect('contacto', nombre="Dokken", apellidos="Lee")

    return render(request, 'pagina.html', {
        'texto': 'Este es mi texto',
        'lista': ['uno', 'dos', 'tres']
    })

def contacto(request, nombre="", apellidos=""):
    html = ""

    if nombre and apellidos:
        html += "<p>El nombre completo es:</p>"
        html += f"<h3>{nombre} {apellidos}</h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()

    return HttpResponse(f"Articulo Creado: <strong>{articulo.title}</strong> - {articulo.content}")

def save_article(request):
    """ RECOGER DATOS GET
    if request.method == 'GET':

        if len(request.GET['title']) <= 5:
            return HttpResponse(f"El titulo {request.GET['title']} es muy pequeño")

        articulo = Article(
            title = request.GET['title'],
            content = request.GET['content'],
            public = request.GET['public']
        )

        articulo.save()

        return HttpResponse(f"Articulo Creado: <strong>{articulo.title}</strong> - {articulo.content}")
    else:
        return HttpResponse(f"<h2>No se ha podido crear el articulo</h2>")
    """
    if request.method == 'POST':

        if len(request.POST['title']) <= 5:
            return HttpResponse(f"El titulo {request.POST['title']} es muy pequeño")

        articulo = Article(
            title = request.POST['title'],
            content = request.POST['content'],
            public = request.POST['public']
        )

        articulo.save()

        return HttpResponse(f"Articulo Creado: <strong>{articulo.title}</strong> - {articulo.content}")
    else:
        return HttpResponse(f"<h2>No se ha podido crear el articulo</h2>")

def create_article(request):

    return render(request, 'create_article.html')

def create_full_article(request):

    if request.method == "POST":
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title = title,
                content = content,
                public = public
            )

            articulo.save()

            # Crear mensaje Flash (sesion que solo e muestra 1 vez)
            messages.success(request, f'Has creado correctamente el articulo {articulo.id}')

            return redirect('articulos')
            # return HttpResponse(articulo.title + ' - ' + articulo.content + ' - ' + str(articulo.public))
    else:
        formulario = FormArticle()

    return render(request, 'create_full_article.html', {
        'form': formulario
    })

def articulo(request):
    try:
        article = Article.objects.get(title='Dragon ball Z', public=True)
        response = f"Articulo: <br/> {article.id}-. {article.title}"
    except:
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse(response)

def editar_articulo(request, id):
    article = Article.objects.get(pk=id)

    article.title = "One Piece"
    article.content = "Animazo"
    article.public = False
    article.image = "zoro.png"

    article.save()

    return HttpResponse(f"Articulo {article.id} Editado: <strong>{article.title}</strong> - {article.content}")

def articulos(request):
    """
    articles = Article.objects.order_by('title') # OBTENER TODOS LOS REG DE LA DB ORDENADOS POR UN CAMPO ASC
    articles = Article.objects.order_by('-title') # OBTENER TODOS LOS REG DE LA DB ORDENADOS POR UN CAMPO DESC
    articles = Article.objects.order_by('title')[:4] # OBTENER REGS DE LA DB CON LIMITE
    articles = Article.objects.all() # OBTENER TODOS LOS REGS DE LA DB
    articles = Article.objects.filter(title="Bleach", id=4) #OBTENER LOS REGISTROS CON TITULO = Bleach AND ID = 4
    articles = Article.objects.filter(title__contains="articulo") #OBTENER LOS REGS CON EL LOCKUP CONTAINS, COMO EL LIKE DE SQL.
    articles = Article.objects.filter(title__exact="articulo") #OBTENER LOS REGS CON EL TITULO EXACTO AL STRING SENSIBLE A CAPS
    articles = Article.objects.filter(title__iexact="articulo") #OBTENER LOS REGS CON EL TITULO EXACTO AL STRING NO SENSIBLE A CAPS

        LOCKUPS >, >=, <, ,=
        >   -   CAMPO__gt   =   número
        >=  -   CAMPO__gte  =   número
        <   -   CAMPO__lt   =   número
        <=  -   CAMPO_lte   =   número

    articles = Article.objects.filter(id__gt=13, id__lt=18)
    articles = Article.objects.filter(id__gt=13, id__lte=18)
    articles = Article.objects.filter(id__gt=4, id__lte=16, title__contains="articulo")

    # EXCLUDE METHOD
    articles = Article.objects.filter(
        title="Articulo"
    ).exclude(
        public=False
    )

    articles = Article.objects.raw("SELECT * FROM miapp_article WHERE title = 'Dragon ball Z' AND public = 0") # CONSULTA SQL DIRECTA

    articles = Article.objects.filter(
        Q(title__contains="segundo") | Q(public=True)
    )

    articles = Article.objects.all().order_by('-id') # OBTENER TODOS LOS REGS DE LA DB
    """

    articles = Article.objects.filter(public=True).order_by('-id') # OBTENER TODOS LOS REGS DE LA DB

    return render(request, 'articulos.html', {
        'articulos': articles
    })

def borrar_articulo(request, id):
    article = Article.objects.get(pk=id)
    article.delete()

    return redirect('articulos')