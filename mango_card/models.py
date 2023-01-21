from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class TypeMango(models.Model):
    Type_name = models.CharField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.Type_name


class GenreMango(models.Model):
    Genre_name = models.CharField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.Genre_name


class Mango(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/mango_photo', default='media/default')
    info = models.TextField(blank=True)
    released = models.DateField(auto_now=False, auto_now_add=False)
    type = models.ForeignKey(TypeMango, on_delete=models.PROTECT, null=True)
    genre = models.ManyToManyField(GenreMango, related_name='%(app_label)s_%(class)s_genre',)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    mango = models.ForeignKey(Mango, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()

    def __str__(self):
        return f"{self.author} - {self.mango.title}"
