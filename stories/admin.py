
from django.contrib import admin
from .models import Story, Genre

class StoryAdmin(admin.ModelAdmin):
    readonly_fields = ('release_date', 'total_score')    # date burya
    list_display = ['title', 'story', 'total_score' ]
    fields = [
        ('title', ('story_parent')),
        ('story'),
        ('author'),
        ('release_date', 'total_score'),
    ]
    search_fields = ['title', 'story']
    list_filter = ('release_date',)

class GenreAdmin(admin.ModelAdmin):
    fields = [ ('name') ]


admin.site.register(Story, StoryAdmin)
admin.site.register(Genre)

