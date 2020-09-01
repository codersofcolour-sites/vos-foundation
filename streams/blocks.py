from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
class goFundMeBlock(blocks.StructBlock):
  gofundme_page_link = blocks.URLBlock(help_text='Add gofundme donation page link.')

  class Meta:
    template = 'streams/gofundme_block.html'
    icon= 'fa-gbp'
    label = "Add gofundme"

class PaypalBlock(blocks.StructBlock):
  paypal_email = blocks.EmailBlock(help_text='Add PayPal acount email')
  class Meta:
    template = 'streams/paypal_block.html'
    icon= 'fa-paypal'
    label = "Add Paypal"

class AmazonSmileBlock(blocks.StructBlock):
  text = blocks.RichTextBlock(features=['p','bold','italic'])
  amazon_smile_link = blocks.URLBlock(help_text='Add Amazon Smile link')
  class Meta:
    template = 'streams/amazon_smile_block.html'
    icon= 'fa-amazon'
    label = "Add Amazon Smile" 

class TextWithRightImageBlock(blocks.StructBlock):
  header = blocks.CharBlock(max_length=150, help_text='Add header')
  text = blocks.RichTextBlock(features=['p','link', 'bold', 'italic',])
  image = ImageChooserBlock()
  class Meta:
    template = 'streams/ltext_rimage_block.html'
    icon= 'fa-align-left'
    label = "Add leftside text and rightside image" 

class TextWithCardsBlock(blocks.StructBlock):
  header = blocks.CharBlock(max_length=150, help_text='Add header')
  text = blocks.RichTextBlock(features=['p','link', 'bold', 'italic',])
  cards = blocks.StreamBlock(
    [
        ('card', blocks.StructBlock([
            ('image', ImageChooserBlock()),
            ('header', blocks.TextBlock()),
            ('text', blocks.RichTextBlock(features=['p','link', 'bold', 'italic',])),
        ],icon='fa-id-card-o')),
    ],
    
)
  class Meta:
    template = 'streams/text_with_cards_block.html'
    icon= 'fa-align-justify'
    label = "Add text with cards" 

class JumboTextBlock(blocks.StructBlock):
  text = blocks.CharBlock(max_length=200, help_text='Add text')

  class Meta:
    template = 'streams/jumbo_text_block.html'
    icon= 'form'
    label = "Add jumbo text" 

class TextWithButtonBlock(blocks.StructBlock):
  text = blocks.RichTextBlock(features=['p','link', 'bold', 'italic',])
  button_name = blocks.CharBlock(max_length=100, help_text='Add text')
  Button_link = blocks.PageChooserBlock()

  class Meta:
    template = 'streams/text_with_button.html'
    icon= 'form'
    label = "Add text with button" 

