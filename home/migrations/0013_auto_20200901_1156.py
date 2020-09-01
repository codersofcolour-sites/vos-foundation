# Generated by Django 3.0.4 on 2020-09-01 10:56

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20200831_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('amazon_smile', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(features=['p', 'bold', 'italic'])), ('amazon_smile_link', wagtail.core.blocks.URLBlock(help_text='Add Amazon Smile link'))])), ('ltext_rimage', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock(help_text='Add header', max_length=150)), ('text', wagtail.core.blocks.RichTextBlock(features=['p', 'link', 'bold', 'italic'])), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('text_with_cards', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock(help_text='Add header', max_length=150)), ('text', wagtail.core.blocks.RichTextBlock(features=['p', 'link', 'bold', 'italic'])), ('cards', wagtail.core.blocks.StreamBlock([('card', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('header', wagtail.core.blocks.TextBlock()), ('text', wagtail.core.blocks.RichTextBlock(features=['p', 'link', 'bold', 'italic']))], icon='fa-id-card-o'))]))])), ('text_with_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(features=['p', 'link', 'bold', 'italic'])), ('button_name', wagtail.core.blocks.CharBlock(help_text='Add text', max_length=100)), ('Button_link', wagtail.core.blocks.PageChooserBlock())])), ('jumbo_text', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Add text', max_length=200))]))], null=True),
        ),
    ]
