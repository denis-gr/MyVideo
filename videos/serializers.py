from rest_framework import serializers
from .models import MainPage, VideoPage

class VideoPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPage
        fields = ["title", "description", "image", "original_video" ,
            "original_width", "original_height", "duration", "video_360",
            "video_480", "video_720", "video_1080"]