from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=255, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(default="null", verbose_name="Imagen", upload_to='articles')
    public = models.BooleanField(verbose_name="¿Publicado?")
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE, verbose_name="Usuario")
    categories = models.ManyToManyField(Category, verbose_name="Categorias", blank=True, related_name="articles") # related_name = nombre que se en lugar de category.article_set
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado el")

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
