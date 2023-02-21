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

