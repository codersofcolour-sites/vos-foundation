# Generated by Django 3.0.4 on 2020-09-01 10:55

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('trustees', '0007_trusteespage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trusteespage',
            name='content',
            field=wagtail.core.fields.StreamField([('text_with_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(features=['p', 'link', 'bold', 'italic'])), ('button_name', wagtail.core.blocks.CharBlock(help_text='Add text', max_length=100)), ('Button_link', wagtail.core.blocks.PageChooserBlock())])), ('ltext_rimage', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock(help_text='Add header', max_length=150)), ('text', wagtail.core.blocks.RichTextBlock(features=['p', 'link', 'bold', 'italic'])), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('jumbo_text', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Add text', max_length=200))]))], null=True),
        ),
    ]