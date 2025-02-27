from .models import Bookmarks
from .serializers import BookmarksSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from backend.bookmarks import serializers


# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_bookmarks(request):
    """
    Get all bookmarks
    """
    bookmarks = Bookmarks.objects.filter(user=request.user)
    serializer = BookmarksSerializer(bookmarks, many=True)
    response_data = {
        "total_count": bookmarks.count(),
        "bookmarks": serializer.data,
    }

    return Response(response_data, status=status.HTTP_200_OK)


