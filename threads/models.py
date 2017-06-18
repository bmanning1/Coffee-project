from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings


class Subject(models.Model):
    # Forum Subject Model with Name and description
    name = models.CharField(max_length=255)
    description = HTMLField()

    def __unicode__(self):
        return self.name


class Thread(models.Model):
    # Subject Thread Model with Name, User, Subject and date created
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='threads')
    subject = models.ForeignKey(Subject, related_name='threads')
    created_at = models.DateTimeField(default=timezone.now)


class Post(models.Model):
    # Thread Post Model with thread, comment, User commenting and date created
    thread = models.ForeignKey(Thread, related_name='posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)
