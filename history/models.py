from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.core.rich_text import expand_db_html, RichText


class HistoryPage(Page):
    subpage_types = []
    parent_types = ['about.AboutPage']
    max_count = 1
    # Replace wrapped rich-text div
    RichText.__html__ = lambda self: expand_db_html(self.source)

    history_content = StreamField([
        ('paragraph', blocks.RichTextBlock(icon="pilcrow", features=['p','link', 'bold', 'italic', 'ol', 'ul'])),
        ('image', ImageChooserBlock(icon="image")),
        ('embedded_video', EmbedBlock(icon="media")),
    ], null=True)
    
    content_panels = Page.content_panels + [
        StreamFieldPanel('history_content'),
    ]
