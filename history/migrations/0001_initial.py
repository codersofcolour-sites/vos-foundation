# Generated by Django 3.0.4 on 2020-08-07 14:48

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('history_content', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['p', 'link', 'bold', 'italic', 'ol', 'ul'], icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media'))], null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
