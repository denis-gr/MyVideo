import io
import os
import tempfile


import cv2
from django.db import models
from django.core.files import File


from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.search import index

class MainPage(Page):
    subpage_types = ["videos.VideoPage"]
    max_count = 1
    template = "videos/index.html"

class VideoPage(Page):
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(verbose_name="Превью", blank=True, null=True)
    video_original = models.FileField(verbose_name="Оригинал видео")
    original_width = models.IntegerField(blank=True, null=True)
    original_height = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    video_360 = models.FileField(verbose_name="360", blank=True, null=True)
    video_480 = models.FileField(verbose_name="480", blank=True, null=True)
    video_720 = models.FileField(verbose_name="720", blank=True, null=True)
    video_1080 = models.FileField(verbose_name="1080", blank=True, null=True)

    search_fields = Page.search_fields + [
        index.SearchField("description"),
    ]
    content_panels = Page.content_panels + [
        FieldPanel("video_original"),
        FieldPanel("description"),
    ]
    #promote_panels = Page.promote_panels + []
    #settings_panels = Page.settings_panels + []

    parent_page_types = ["videos.MainPage"]
    subpage_types = []
    template = "videos/index2.html"

    def save(self, **kwargs):
        result = super().save(**kwargs)
        cap = cv2.VideoCapture(self.video_original.path)
        self.original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        self.duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) // fps

        # get and swet image
        image = cap.read()[-1]
        io_buf = io.BytesIO(cv2.imencode(".jpg", image)[-1])
        self.image = File(io_buf, name=self.title+"_image.jpg")
        
        # get video with differnet sizes
        sizes = [(640, 360), (854, 480), (1280, 720), (1920, 1080)]
        sizes = filter(lambda x: min(x) <= min([self.original_width, self.original_height]), sizes)
        out_files = { i: tempfile.mkstemp(suffix = ".avi") for i in sizes}
        video_cod = cv2.VideoWriter_fourcc(*'XVID')
        out_writers = { i: cv2.VideoWriter(j[1], video_cod, fps, i)
            for i, j in out_files.items() }
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret==True:
                for i, j in out_writers.items():
                    j.write(cv2.resize(frame, i))
            else:
                break
        for i in out_writers.values(): i.release()
        for i, j in out_files.items():
            name = f"video_{min(i)}"
            setattr(self, name, File(open(j[1], mode="rb"), name=f"{self.title}_{name}.avi"))
            os.close(j[0])
        cap.release()
        return result

