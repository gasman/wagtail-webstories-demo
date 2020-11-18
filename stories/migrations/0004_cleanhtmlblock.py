# Generated by Django 2.2.17 on 2020-11-18 16:04

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail_webstories.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_storypage_custom_css'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storypage',
            name='pages',
            field=wagtail.core.fields.StreamField([('page', wagtail.core.blocks.StructBlock([('id', wagtail.core.blocks.CharBlock()), ('html', wagtail_webstories.blocks.AMPCleanHTMLBlock())]))]),
        ),
    ]
