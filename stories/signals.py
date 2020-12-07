from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import StoryPage


@receiver(post_save, sender=StoryPage)
def import_story_images(sender, instance, **kwargs):
    images_changed = instance.import_images()
    videos_changed = instance.import_videos()
    if images_changed or videos_changed:
        instance.save()
