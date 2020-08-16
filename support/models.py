from django.db import models
from django.core.validators import RegexValidator

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


class BecomeSupporterPage(Page):
    subpage_types = []
    max_count = 1
    # Replace wrapped rich-text div
    RichText.__html__ = lambda self: expand_db_html(self.source)

    supporter_content = StreamField([
        ('paragraph', blocks.RichTextBlock(icon="pilcrow", features=['p','link', 'bold', 'italic', 'ol', 'ul'])),
    ], null=True)
    contact_info = models.CharField(max_length=150, blank=False)
    contact_name = models.CharField(max_length=150, blank=False, null=True)
    email = models.EmailField(blank=False, null=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('supporter_content'),
        FieldPanel('contact_info'),
        FieldPanel('contact_name'),
        FieldPanel('email'),
        FieldPanel('phone_number'),
    ]

class BecomeVolunteerPage(Page):
    subpage_types = []
    max_count = 1
    # Replace wrapped rich-text div
    RichText.__html__ = lambda self: expand_db_html(self.source)

    volunteer_content = StreamField([
        ('paragraph', blocks.RichTextBlock(icon="pilcrow", features=['p','link', 'bold', 'italic', 'ol', 'ul'])),
    ], null=True)
    contact_info = models.CharField(max_length=150, blank=False)
    contact_name = models.CharField(max_length=150, blank=False, null=True)
    email = models.EmailField(blank=False, null=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('volunteer_content'),
        FieldPanel('contact_info'),
        FieldPanel('contact_name'),
        FieldPanel('email'),
        FieldPanel('phone_number'),
    ]
