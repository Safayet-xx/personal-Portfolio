# Generated by Django 5.0.7 on 2024-09-13 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image_caption',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
