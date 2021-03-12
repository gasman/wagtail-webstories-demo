# Generated by Django 2.2.17 on 2021-03-12 10:28

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail_webstories.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0009_storypage_original_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('story_embed', wagtail_webstories.blocks.StoryEmbedBlock(label='Imported story')), ('external_story', wagtail_webstories.blocks.ExternalStoryEmbedBlock(label='External story')), ('carousel', wagtail.core.blocks.StreamBlock([('story', wagtail_webstories.blocks.StoryChooserBlock(label='Imported story')), ('external_story', wagtail_webstories.blocks.ExternalStoryBlock(label='External story'))], template='stories/blocks/carousel.html'))]),
        ),
    ]
