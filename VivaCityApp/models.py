from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class Destination(models.Model):
    imagen = models.ImageField(upload_to='static/destinations/images/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Otros campos que necesites

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    imagen = models.ImageField(upload_to='static/gallery/images/')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    aos_delay = models.IntegerField(default=150)

    def __str__(self):
        return self.title


class Testimonio(models.Model):
    contenido = models.TextField()
    nombre_usuario = models.CharField(max_length=255)
    imagen_usuario = models.ImageField(upload_to='static/testimonios/images/')

    def __str__(self):
        return self.nombre_usuario


class BlogPost(models.Model):
    imagen = models.ImageField(upload_to='static/blog/images/')
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class canton(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False)
    nombre_canton = models.CharField(max_length=225, null=True)

    class Meta:
        verbose_name = 'nombre_canton'
        verbose_name_plural = 'nombre_cantones'
        ordering = ['nombre_canton']

    def __str__(self):
        return self.nombre_canton


class lugar(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False)
    nombre_lugar = models.CharField(max_length=225, null=True)
    fotolugar = models.ImageField(upload_to='static/lugar/images', null=True)
    direccionlugar = models.URLField(null=True)
    infoLugar = models.TextField(max_length=225, null=True)
    hora_abre = models.TimeField(null=True)
    hora_cierre = models.TimeField(null=True)
    tipo_lugar = models.CharField(max_length=225, null=True)
    canton_id = models.ForeignKey(canton, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'lugar'
        verbose_name_plural = 'lugares'
        ordering = ['nombre_lugar']

    def __str__(self):
        return self.nombre_lugar


class evento(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False)
    nomEvento = models.CharField(max_length=225, null=True)
    fecha_inicio = models.DateTimeField(null=True)
    fecha_fin = models.DateTimeField(null=True)
    direccionEvento = models.URLField(null=True)
    infoEvento = models.TextField(max_length=225, null=True)
    fotoEvento = models.ImageField(
        upload_to='static/eventos/images', null=True)
    canton_id = models.ForeignKey(canton, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'evento'
        ordering = ['nomEvento']

    def __str__(self):
        return self.nomEvento


class hospedaje(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False)
    nombre_hospedaje = models.CharField(max_length=225, null=True)
    fotoHospedaje = models.ImageField(
        upload_to='static/hospedajes/images', null=True)
    direccionHospedaje = models.URLField(null=True)
    hora_abre = models.TimeField(null=True)
    hora_cierra = models.TimeField(null=True)
    infoHospedaje = models.TextField(null=True)
    precioNoche = models.DecimalField(
        max_digits=15, decimal_places=4, null=True)
    tipoHospedaje = models.CharField(max_length=225, null=True)
    categoria = models.CharField(max_length=225, null=True)
    canton_id = models.ForeignKey(canton, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'hospedaje'
        verbose_name_plural = 'hospedajes'
        ordering = ['nombre_hospedaje']

    def __str__(self):
        return self.nombre_hospedaje


class agenda(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    evento_id = models.ForeignKey(evento, on_delete=models.CASCADE)
