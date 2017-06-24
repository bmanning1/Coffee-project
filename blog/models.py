from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    """ Post new blog model with options: Author, Title, Content, Created Date, Published Date, Views, Tag, Image """

    class Meta:
        """ This ensures build in the IDE """
        app_label = "blog"

    # Author is linked to a registered User in the 'auth_user' table
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # Record how often a post is seen
    views = models.IntegerField(default=0)
    # Create a tag that can be used to summarise the blog post
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def publish(self):
        """ Save published date as now """
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title
