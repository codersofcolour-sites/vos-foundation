from django.db import models
from django import forms
from django.utils import timezone
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.core.rich_text import expand_db_html, RichText

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text='A slug to identify posts by this category',
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

class BlogIndexPage(RoutablePageMixin, Page):
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
        paginator = Paginator(all_posts, 18)
        page = request.GET.get("page")
        try: 
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context["newspages"] = posts
        context["categories"] = BlogCategory.objects.all()
        return context
    
    @route(r'^category/(?P<cat_slug>[-\w]*)/$', name='category_view')
    def category_view(self, request, cat_slug):
        context = self.get_context(request)
        live_newspages = self.get_children().live()
        try:
            category = BlogCategory.objects.get(slug=cat_slug)
        except:
            category = None
        cat_posts = BlogPage.objects.filter(categories__in=[category])
        paginator = Paginator(cat_posts, 18)
        page = request.GET.get("page")

        try: 
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context["posts"] = posts
        context['cat'] = category
        return render(request, "blog/category_view.html", context)
    

class BlogPage(Page):
    TOP = 'top'
    IMAGE_POSITION = [
        (TOP, 'Top part'),
        ('center', 'Center part'),
        ('bottom', 'Bottom part'),
    ]
    parent_page_type =[
        'blog.BlogIndexPage'
    ]        
    subpage_types = []
    date = models.DateField("Post date")
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    news_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL
    )
    display_image_position = models.CharField(
        max_length=6,
        choices= IMAGE_POSITION,
        default=TOP,
        help_text='Adjust the positon of image displayed on article page cover'
    )

    # Replace wrapped rich-text div
    RichText.__html__ = lambda self: expand_db_html(self.source)

    news_content = StreamField([
        ('paragraph', blocks.RichTextBlock(icon="pilcrow", features=['p','link', 'bold', 'italic', 'ol', 'ul'])),
        ('image', ImageChooserBlock(icon="image")),
        ('quote', blocks.StructBlock([
            ('source', blocks.CharBlock(blank=True, classname="full",
                                        help_text='The source of where that quote came from.')),
            ('quote_text', blocks.CharBlock(
                classname="full", help_text='Add quote.')),
        ], icon='openquote'), ),
        ('embedded_video', EmbedBlock(icon="media")),
    ], null=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldRowPanel([
            ImageChooserPanel('news_image'),
            FieldPanel('display_image_position'),
        ],
        heading='Image cover',
        ),
        StreamFieldPanel('news_content'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    ]

    def first_paragraph(self):
        for block in self.news_content:
            if block.block_type == 'paragraph':
                return block.value

BlogPage._meta.get_field("date").default = timezone.now