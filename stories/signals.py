from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import StoryPage


@receiver(post_save, sender=StoryPage)
def import_story_images(sender, instance, **kwargs):
    changed = instance.import_images()
    if changed:
        instance.save()
