from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock

class goFundMeBlock(blocks.StructBlock):
  gofundme_page_link = blocks.URLBlock(required=True, help_text='Add gofundme donation page link.')

  class Meta:
    template = 'streams/gofundme_block.html'
    icon= 'fa-gbp'
    label = "Add gofundme"

class PaypalBlock(blocks.StructBlock):
  paypal_email = blocks.EmailBlock(required=True, help_text='Add PayPal acount email')

  class Meta:
    template = 'streams/paypal_block.html'
    icon= 'fa-paypal '
    label = "Add Paypal"