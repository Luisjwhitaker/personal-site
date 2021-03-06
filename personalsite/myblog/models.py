from django.db import models
from taggit.managers import TaggableManager
# Create your models here.

#class Tags(models.Model):
#    tag_name = models.CharField(max_length=30)
#    def __str__(self):
#            return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=99999) # change to rich-text-field soon
    post_tags = TaggableManager()
    date_created = models.DateTimeField(auto_now_add=True)
    # Add view count later ?

    def __str__(self):
        return self.title
