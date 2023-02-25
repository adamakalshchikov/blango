from django.contrib import admin

from blog.models import Tag, Post, Comment
# Register your models here.

admin.site.register(Tag)
admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", ) }
    # exclude = ("slug",)
    list_display = ("slug", "published_at")

