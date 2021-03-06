from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from wagtail_webstories.blocks import StoryChooserBlock, StoryEmbedBlock, ExternalStoryBlock, ExternalStoryEmbedBlock
from wagtail_webstories.models import BaseWebStoryPage


class StoryPage(BaseWebStoryPage):
    pass


class StoryIndexPage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        context['stories'] = StoryPage.objects.child_of(self).live().order_by('-first_published_at')
        return context


class BlogPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('story_embed', StoryEmbedBlock(label="Imported story")),
        ('external_story', ExternalStoryEmbedBlock(label="External story")),
        ('carousel', blocks.StreamBlock([
            ('story', StoryChooserBlock(label="Imported story")),
            ('external_story', ExternalStoryBlock(label="External story")),
        ], template="stories/blocks/carousel.html")),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
