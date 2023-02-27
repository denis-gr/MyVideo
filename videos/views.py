from .models import MainPage, VideoPage
from rest_framework import viewsets
from .serializers import VideoPageSerializer

class VideoPageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = VideoPage.objects.all()
    serializer_class = VideoPageSerializer