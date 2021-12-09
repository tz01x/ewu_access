from django.contrib import admin

# Register your models here.

from .models import Post,Comments,Vote,Community

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Vote)
admin.site.register(Community)