from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from wagtail_webstories.blocks import StoryEmbedBlock
from wagtail_webstories.models import BaseWebStoryPage


class StoryPage(BaseWebStoryPage):
    pass


class BlogPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('story_embed', StoryEmbedBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
