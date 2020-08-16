from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel

class AboutPage(Page):   
    subpage_types = ['trustees.TrusteesPage', 'history.HistoryPage', 'beneficiaries.BeneficiariesPage', 'supporters.SupportersPage']
    max_count = 1 
    about_content = StreamField([
        ('subheading', blocks.RichTextBlock(icon="title", features=['h2'])),
        ('paragraph', blocks.RichTextBlock(icon="pilcrow", features=['p','link', 'bold', 'italic'])),
    ], null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('about_content')            
    ]