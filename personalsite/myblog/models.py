from django.db import models

# Create your models here.

class Tags(models.Model):
    tag_name = models.CharField(max_length=30)
    def __str__(self):
            return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
#    needs pillow to work
#    image = models.ImageField(upload_to='')# use this as header for content and image for preview
    content = models.TextField(max_length=500) # change to rich-text-field soon
#    tags = # list of tags
    date_created = models.DateTimeField(auto_now_add=True)
    # Add view count later

    def __str__(self):
        return self.title
