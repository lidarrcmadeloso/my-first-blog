from django.contrib import admin

from .models import Post #add this to import the Post model



class PostAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'message','photo','name','facebook']

admin.site.register(Post,PostAdmin) #add this to register the Post model

