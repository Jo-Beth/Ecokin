
from django.contrib import admin
from  .models  import Utilisateur
from django.contrib.auth.admin import UserAdmin
# Register your models here.

#Dans le cas ou il est mal enregistrer


@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Informations supplémentaires', {
        'fields': ('telephone', 'adresse', 'photo', 'role', ) } ),)
            
            
            
            

       
    
    

