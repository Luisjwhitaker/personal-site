from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost

# Register your models here.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = 'content'

admin.site.register(BlogPost, SomeModelAdmin)
#admin.site.register(BlogPost)
#admin.site.register(model.BlogPost, SummerAdmin)
