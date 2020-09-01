from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, InlinePanel

from wagtail.core.models import Page

from streams import blocks
from wagtail.core.blocks import StreamBlock

class DonatePage(Page):
    parent_types = ['home.HomePage']
    subpage_types = []   
    max_count = 1 
    header = models.CharField(max_length=150, blank=False, null=True)
    body = models.CharField(max_length=350, blank=True)

    donation_link = StreamField(  
        StreamBlock (
            [('gofundme', blocks.goFundMeBlock()), ('paypal', blocks.PaypalBlock()), ('amazon_smile', blocks.AmazonSmileBlock()),],
            max_num=3
        ), null=True
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('header'),
        FieldPanel('body'),
        StreamFieldPanel('donation_link')
    ]