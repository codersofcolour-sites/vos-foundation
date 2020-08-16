from django.db import models
from django.utils import timezone

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.core.rich_text import expand_db_html, RichText


class BlogIndexPage(Page):
    subpage_types = ['BlogPage']
    parent_page_type =[
        'home.HomePage'
    ]  
    max_count = 1 
    intro = models.CharField(blank=True, max_length=150)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(BlogIndexPage, self).get_context(request, *args, **kwargs)
        live_newspages = self.get_children().live()
        all_posts = live_newspages.live().order_by('-first_published_at')
        paginator = Paginator(all_posts, 12)
        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context["newspages"] = posts
        return context
    

class BlogPage(Page):
    parent_page_type =[
        'blog.BlogIndexPage'
    ]        
    subpage_types = []
    date = models.DateField("Post date")
    news_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL
    )

    # Replace wrapped rich-text div
    RichText.__html__ = lambda self: expand_db_html(self.source)

    news_content = StreamField([
        ('paragraph', blocks.RichTextBlock(icon="pilcrow", features=['p','link', 'bold', 'italic', 'ol', 'ul'])),
        ('image', ImageChooserBlock(icon="image")),
        ('quote', blocks.StructBlock([
            ('source', blocks.CharBlock(classname="full",
                                        help_text='The source of where that quote came from.')),
            ('quote_text', blocks.CharBlock(
                classname="full", help_text='Add quote.')),
        ], icon='openquote'), ),
        ('embedded_video', EmbedBlock(icon="media")),
    ], null=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('news_image'),
        StreamFieldPanel('news_content'),
    ]

    def first_paragraph(self):
        for block in self.news_content:
            if block.block_type == 'paragraph':
                return block.value

BlogPage._meta.get_field("date").default = timezone.now