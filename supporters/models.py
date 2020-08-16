from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core.rich_text import expand_db_html, RichText
from wagtail.images.edit_handlers import ImageChooserPanel

class Supporters(Orderable):
    page = ParentalKey("supporters.SupportersPage", related_name="supporters_list")
    supporter_name = models.CharField(max_length=150, blank=False)
    supporter_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    supporter_info = RichTextField(blank=True, features=['p','link', 'bold', 'italic', 'ol', 'ul'])

    
    panels = [
        FieldPanel('supporter_name'),
        ImageChooserPanel('supporter_image'),
        FieldPanel('supporter_info')
    ]
    

class SupportersPage(Page):
    parent_types = ['about.AboutPage']
    subpage_types = []   
    max_count = 1 
    intro =  models.CharField(max_length=650, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        MultiFieldPanel(
            [InlinePanel("supporters_list", label="Supporter"), ],
            heading="Supporters",
        )
    ]