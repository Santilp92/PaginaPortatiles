from django.contrib import admin

# Register your models here.
from .models.user import User
from .models.portatil import Portatil
from .models.lista import Lista

admin.site.register(User)
admin.site.register(Lista)
admin.site.register(Portatil)