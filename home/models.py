from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    PageChooserPanel,
)
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, InlinePanel, PageChooserPanel
from streams import blocks

class HomePageCarousel(Orderable):
    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    carousel_header = models.CharField(max_length=150, blank=True, null=True)
    carousel_text = models.CharField(max_length=300, blank=True, null=True)
    
    panels = [
        MultiFieldPanel([
            ImageChooserPanel("carousel_image"),
            FieldPanel("carousel_header"),
            FieldPanel("carousel_text"),   
        ], heading='Carousel')
]  

class HomePage(Page):
    max_count = 1 

    content = StreamField([
        ('amazon_smile', blocks.AmazonSmileBlock()),
        ('ltext_rimage', blocks.TextWithRightImageBlock()),
        ('text_with_cards', blocks.TextWithCardsBlock()),
        ('jumbo_text', blocks.JumboTextBlock()),
    ], blank=False, null=True)

    video_url = models.URLField(blank=False, null=True)
    video_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    header_1 = models.CharField(max_length=100, blank=False, null=True)
    text_1 = RichTextField(blank=False, features=['p','link', 'bold', 'italic',], null=True)
    button_link_1 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    button_text_1 = models.CharField(max_length=50, blank=False, null=True)

    header_2 = models.CharField(max_length=100, blank=False, null=True)
    text_2 = RichTextField(blank=False, features=['p','link', 'bold', 'italic',], null=True)
    button_link_2 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    button_text_2 = models.CharField(max_length=50, blank=False, null=True)
    
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=5,
                         min_num=1, label="Image"), ],
            heading="Carousel Images",
        ),
        StreamFieldPanel('content'),
        MultiFieldPanel([
            FieldPanel("video_url"),
            ImageChooserPanel("video_image"),            
        ], heading='Homepage video section'),  
        MultiFieldPanel([
            FieldPanel("header_1"),
            FieldPanel("text_1"),
            PageChooserPanel("button_link_1"),
            FieldPanel("button_text_1"),
        ], heading='Info box 1'),
        MultiFieldPanel([
            FieldPanel("header_2"),
            FieldPanel("text_2"),
            PageChooserPanel("button_link_2"),
            FieldPanel("button_text_2"),
        ], heading='Info box 2'),         
    ]

    def get_carousel_images(self):
        carousel_list = []
        for image in self.carousel_images.all():
            if image.carousel_image  != None:
                carousel_list.append(image)
        return carousel_list


