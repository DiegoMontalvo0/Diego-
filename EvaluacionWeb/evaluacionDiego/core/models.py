from django.db import models
from django.utils.html import format_html

# Create your models here.
class position(models.Model):
    name = models.CharField(max_length=25, verbose_name="Nombre de la posicion")
    description = models.TextField(max_length=25, verbose_name="Descripcion de la posicion")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Posicion'
        verbose_name_plural = 'Posiciones'
        db_table = 'Posicion'
        ordering = ['id']

class Technical(models.Model):
    name = models.CharField(max_length=25, verbose_name="Nombre")
    Surname = models.TextField(max_length=25, verbose_name="Apellido")
    Date = models.DateField(verbose_name="Fecha de nacimiento")
    Nationality = models.CharField(max_length=25, verbose_name="Nacionalidad")
    Role = models.CharField(max_length=25, verbose_name="Rol (técnico | asistente | médico | preparador)")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnicos'
        db_table = 'Tecnico'
        ordering = ['id']

class Team(models.Model):
    name = models.CharField(max_length=25, verbose_name="Nombre de equipo")
    flag = models.ImageField(upload_to='media', null=False, blank=True)
    Shield = models.ImageField(upload_to='media', null=False, blank=True)
    Technical = models.ForeignKey(Technical, on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        db_table = 'Equipo'
        ordering = ['id']
    def show_flag(self):
        return format_html('<img src={} width="100" /> ', self.flag.url)
    def show_Shield(self):
        return format_html('<img src={} width="100" /> ', self.Shield.url)
    
class Player(models.Model):
    name = models.CharField(max_length=25, verbose_name="Nombre")
    Surname = models.TextField(max_length=25, verbose_name="Apellido")
    Photo = models.ImageField(upload_to='media', null=False, blank=True)
    Date = models.DateField(verbose_name="Fecha de nacimiento")
    Position = models.ForeignKey(position, on_delete=models.CASCADE)
    Number = models.IntegerField(verbose_name="Numero de  camisa")
    Headline = models.CharField(max_length=25, verbose_name="Es titular")
    Team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        db_table = 'Jugador'
        ordering = ['id']
    def show_Photo(self):
        return format_html('<img src={} width="100" /> ', self.Photo.url)






