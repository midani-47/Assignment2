from django.contrib import admin
from .models import Post
from .models import Journey, Comment

class blogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, blogAdmin)
admin.site.register(Journey)
admin.site.register(Comment)






