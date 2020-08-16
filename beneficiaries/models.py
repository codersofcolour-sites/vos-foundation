from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import StreamFieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel

class Beneficiaries(Orderable):
    page = ParentalKey("beneficiaries.BeneficiariesPage", related_name="beneficiaries_list")
    beneficiary_name = models.CharField(max_length=150, blank=False)
    beneficiary_link = models.URLField(blank=True, null=True)
    beneficiary_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    beneficiary_info = RichTextField(blank=True, features=['p','link', 'bold', 'italic', 'ol', 'ul'])


    panels = [
        FieldPanel('beneficiary_name'),
        ImageChooserPanel('beneficiary_image'),
        FieldPanel('beneficiary_link'),
        FieldPanel('beneficiary_info')
    ]
    

class BeneficiariesPage(Page):
    parent_types = ['about.AboutPage']
    subpage_types = []   
    max_count = 1 
    
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [InlinePanel("beneficiaries_list", label="Beneficiary"), ],
            heading="Beneficiaries",
        )
    ]