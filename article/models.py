from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Meta():
    db_table = 'article'

class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_created_date = models.DateTimeField(default=timezone.now)
    article_published_date = models.DateTimeField(blank=True,null=True)
    article_likes = models.IntegerField(blank=True,null=True)

    def published(self):
        self.article_published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.article_title
    


