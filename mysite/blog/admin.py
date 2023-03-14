from django.contrib import admin

from .models import Post
admin.site.register(Post)

from .models import Comentario
admin.site.register(Comentario)

# from Register your models here.
