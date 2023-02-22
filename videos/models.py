import cv2
from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.search import index

class MainPage(Page):
    subpage_types = ["videos.VideoPage"]
    max_count = 1

class VideoPage(Page):
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(verbose_name="Превью", blank=True, null=True)
    original_video = models.FileField(verbose_name="Оригинал видео")
    original_size_width = models.IntegerField(blank=True, null=True)
    original_size_height = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    video_144 = models.FileField(verbose_name="144", blank=True, null=True)
    video_240 = models.FileField(verbose_name="240", blank=True, null=True)
    video_360 = models.FileField(verbose_name="360", blank=True, null=True)
    video_480 = models.FileField(verbose_name="480", blank=True, null=True)
    video_720 = models.FileField(verbose_name="720", blank=True, null=True)
    video_1080 = models.FileField(verbose_name="1080", blank=True, null=True)

    search_fields = Page.search_fields + [
        index.SearchField("description"),
        index.FilterField("original_size_width"),
        index.FilterField("original_size_height"),
        index.FilterField("duration"),
    ]
    content_panels = Page.content_panels + [
        FieldPanel("original_video"),
        FieldPanel("image"),
        FieldPanel("description"),
    ]
    #promote_panels = Page.promote_panels + []
    #settings_panels = Page.settings_panels + []

    parent_page_types = ["videos.MainPage"]
    subpage_types = []

    def save(self, **kwargs):
        old = self.__class__.objects.get(id=self.id).specific.original_video

        cap = cv2.VideoCapture(self.original_video.path)
        self.original_size_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.original_size_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.duration = int(cap.get(cv2.CAP_PROP_POS_MSEC))

        # get and swet image
        image = cap.read()[-1]
        io_buf = io.BytesIO(cv2.imencode(".jpg", image)[-1])
        self.image = File(io_buf)

        if old.video != self.video:
            ...
        result = super().save(**kwargs)
        return result

