
from django.db import models
from django.conf import settings

class Story(models.Model):
    story_parent = models.ForeignKey('self',blank =True, null=True, related_name='sub_story')
    title = models.CharField(max_length=255)
    story = models.TextField(blank=False, null=True)
    release_date = models.DateTimeField(auto_now_add=True)
    total_score = models.PositiveIntegerField(default=0) # ManyToManyField('Genre', related_name='stories')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posted_stories')
    scored_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked_stories')
    genres = models.ManyToManyField('Genre', related_name='stories', blank=True)

    def __str__(self):  # Panelde title ın görünmesini sağlıyor.
        return self.title

    def avg_score(self):
        if not self.scored_users.count():
            return 0
        return self.total_score / self.scored_users.count()

    def genres_verbose(self):
        return ', '.join(self.genres.values_list('name', flat=True))

    class Meta:
        verbose_name_plural= 'Stories'

class Genre(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True, related_name = 'sub_genres')

    def __str__(self):
        return self.name
