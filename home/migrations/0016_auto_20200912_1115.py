# Generated by Django 3.0.4 on 2020-09-12 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('home', '0015_auto_20200902_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagecarousel',
            name='button_text',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='homepagecarousel',
            name='page_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
    ]
