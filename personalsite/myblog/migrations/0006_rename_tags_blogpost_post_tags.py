# Generated by Django 3.2 on 2021-05-25 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_blogpost_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='tags',
            new_name='post_tags',
        ),
    ]
