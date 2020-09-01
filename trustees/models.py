from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import StreamFieldPanel

from wagtail.core.rich_text import expand_db_html, RichText

from wagtailmenus.models import MenuPage
from wagtailmenus.panels import menupage_panel

from streams import blocks

class TrusteesPage(Page): 
    parent_types = ['about.AboutPage']  
    subpage_types = ['TrusteePage']
    max_count = 1

    content = StreamField([
        ('text_with_button', blocks.TextWithButtonBlock()),
        ('ltext_rimage', blocks.TextWithRightImageBlock()),
        ('jumbo_text', blocks.JumboTextBlock()),
    ], blank=False, null=True)

    def get_context(self, request, *args, **kwargs):
        context = super(TrusteesPage, self).get_context(request, *args, **kwargs)
        trustees_list = self.get_children().live()
        context["trustees"] = trustees_list
        return context

    content_panels = Page.content_panels + [
        StreamFieldPanel('content')
    ]

class TrusteePage(Page):
    parent_page_type =[
        'trustees.TrusteesPage'
    ]        
    subpage_types = []
    trustee_name =  models.CharField(max_length=150, blank=False)
    trustee_role = models.CharField(max_length=150, blank=False)
    trustee_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL
    )
    email = models.EmailField(blank=True, null=True, help_text="Add email address")
    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    linkedin = models.URLField(blank=True, null=True, help_text="Linkedin URL")
    instagram = models.URLField(blank=True, null=True, help_text="Instagram URL")
    youtube = models.URLField(blank=True, null=True, help_text="Youtube channel URL")

    trustee_info = RichTextField(features=['p','link', 'bold', 'italic'])

    # Replace wrapped rich-text div
    RichText.__html__ = lambda self: expand_db_html(self.source)
    
    content_panels = Page.content_panels + [
        FieldPanel('trustee_name'),
        FieldPanel('trustee_role'),
        FieldPanel('trustee_info', classname="full"),
        ImageChooserPanel('trustee_image'),        
        MultiFieldPanel([
          FieldPanel('email'),          
          FieldPanel('facebook'),
          FieldPanel('twitter'),
          FieldPanel('linkedin'),
          FieldPanel('instagram'),
          FieldPanel('youtube')
          ], heading="Trustee social media",),
    ]