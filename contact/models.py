from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)

class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', related_name='form_fields')

class ContactPage(AbstractEmailForm):
    subpage_types = []
    max_count = 1 
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "contact/contact_page_landing.html"

    header = models.CharField(max_length=150, blank=True)
    intro = models.CharField(max_length=150, blank=True)
    thank_you_text = RichTextField(blank=True,features=['bold', 'italic', 'link'])

    content_panels = AbstractEmailForm.content_panels + [  
        FieldPanel('header'),
        FieldPanel('intro'),      
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Notification Settings"),
    ]

    def get_form_fields(self):
        return self.form_fields.all()   

