# Generated by Django 3.0.4 on 2020-08-30 10:47

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0008_auto_20200830_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donatepage',
            name='donation_link',
            field=wagtail.core.fields.StreamField([('gofundme', wagtail.core.blocks.StructBlock([('gofundme_page_link', wagtail.core.blocks.URLBlock(help_text='Add gofundme donation page link.', required=True))])), ('paypal', wagtail.core.blocks.StructBlock([('Paypal_email', wagtail.core.blocks.EmailBlock(help_text='Add PayPal acount email', required=True))]))], null=True),
        ),
    ]
