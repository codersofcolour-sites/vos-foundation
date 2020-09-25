from django.db import models
from django.core.validators import RegexValidator

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    PageChooserPanel,
    StreamFieldPanel
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.core.rich_text import expand_db_html, RichText


class BecomeSupporterPage(Page):
    subpage_types = []
    max_count = 1
    # Replace wrapped rich-text div
    RichText.__html__ = lambda self: expand_db_html(self.source)

    supporter_content = StreamField([
        ('paragraph', blocks.RichTextBlock(icon="pilcrow", features=['p','link', 'bold', 'italic', 'ol', 'ul'])),
    ], null=True)
    button_text = models.CharField(max_length=20, blank=True, null=True)
    button_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('supporter_content'),
        MultiFieldPanel([
            FieldPanel("button_text"),           
            PageChooserPanel("button_link"),
        ], heading='Button')
        
    ]

class BecomeVolunteerPage(Page):
    subpage_types = []
    max_count = 1
    # Replace wrapped rich-text div
    RichText.__html__ = lambda self: expand_db_html(self.source)

    volunteer_content = StreamField([
        ('paragraph', blocks.RichTextBlock(icon="pilcrow", features=['p','link', 'bold', 'italic', 'ol', 'ul'])),
    ], null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('volunteer_content'),
    ]
