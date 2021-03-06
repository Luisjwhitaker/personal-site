from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from myblog.models import BlogPost
from myblog.api.serializers import BlogPostSerializer

@api_view(['GET',])
def api_post_page(request,primery_key):
    try:
        blog_post = BlogPost.objects.get(id=primery_key)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)
