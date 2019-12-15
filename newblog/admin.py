from django.contrib import admin


from .models import Article, ArticleComment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','article_title', 'slug','article_author','published_date','status_choice')
    list_filter = ('status_choice','created_date','published_date','article_author')
    search_fields = ('article_title','description')
    prepopulated_fields = {'slug':('description',)}
    raw_id_fields = ('article_author',)
    date_hierarchy = 'published_date'
    ordering = ['status_choice', 'published_date']


class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('id','article','name', 'body','created')
    list_filter = ('name','created')



admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleComment,ArticleCommentAdmin)
