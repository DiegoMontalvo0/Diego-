from django.contrib import admin

# Register your models here.

from .models import Team,Player,position,Technical
@admin.register(position)
class positionAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    #list_display_links = ("name", "price")
    
    search_fields = ["name"]
    list_filter = ["name"]
    #list_per_page = 

@admin.register(Technical)
class TecnicAdmin(admin.ModelAdmin):
    list_display = ['name','Surname','Date','Nationality','Role']
    #list_display_links = ("name", "price")
    list_editable = ["Role","Nationality"]
    search_fields = ["name"]
    list_filter = ["name"]
    #list_per_page = 1

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name','Surname','show_Photo','Date','Position','Number','Headline','Team']
    #list_display_links = ("name", "price")
    list_editable = ["Headline","Team"]
    search_fields = ["name"]
    list_filter = ["name"]
    #list_per_page = 

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name','show_flag','show_Shield','Technical']
    #list_display_links = ("name", "price")
    
    search_fields = ["name"]
    list_filter = ["name"]
    #list_per_page = 

