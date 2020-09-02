from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.core.models import Orderable
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel 
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from wagtail.snippets.models import register_snippet

@register_setting(icon='site')
class SocialMediaSettings(BaseSetting):
  facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
  twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
  linkedin = models.URLField(blank=True, null=True, help_text="Linkedin URL")
  instagram = models.URLField(blank=True, null=True, help_text="Instagram URL")
  youtube = models.URLField(blank=True, null=True, help_text="Youtube channel URL")
  pinterest = models.URLField(blank=True, null=True, help_text="Pinterest URL")
  email = models.EmailField(blank=True, null=True, help_text="Add email address")

  panels = [
    FieldPanel('email'),
    FieldPanel('facebook'),
    FieldPanel('twitter'),
    FieldPanel('linkedin'),
    FieldPanel('instagram'),
    FieldPanel('youtube'),
    FieldPanel('pinterest'),
  ]

  class Meta:
    verbose_name = 'social media accounts'

@register_setting(icon='image')
class WebsiteLogo(BaseSetting):
  website_logo = models.ForeignKey(
    "wagtailimages.Image",
    null=True,
    blank=False,
    on_delete=models.SET_NULL,
    related_name="+",
  )


  panels = [
    ImageChooserPanel('website_logo'),
  ]

  class Meta:
    verbose_name = 'Website Logo'

@register_setting(icon='image')
class WebsiteBannerImage(BaseSetting):
  website_banner = models.ForeignKey(
    "wagtailimages.Image",
    null=True,
    blank=False,
    on_delete=models.SET_NULL,
    related_name="+",
  )
  
  panels = [
    ImageChooserPanel('website_banner'),
  ]

  class Meta:
    verbose_name = 'Website Banner Image'

@register_setting(icon='cog')
class FooterSetting(BaseSetting):
  phone_number = models.CharField(max_length=30, blank=True)
  address = models.CharField(max_length=250, blank=True, null=True)
  email = models.EmailField(blank=True, null=True) 
  charity_number = models.CharField(max_length=10, blank=True, null=True)

  panels = [
      MultiFieldPanel([
          FieldPanel('phone_number'),
          FieldPanel('email'),
          FieldPanel('address')],
          heading="Charity Information",
      ),  
      MultiFieldPanel(
          [FieldPanel('charity_number'),],
          heading="Registered Charity Number",
      ),          
  ]

@register_setting(icon='cog')
class ImportantPages(BaseSetting):

    select_related = ["donate_page", "home_page"]

    donate_page = models.ForeignKey(
        'wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    home_page = models.ForeignKey(
        'wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        PageChooserPanel('home_page'),
        PageChooserPanel('donate_page'),
    ]