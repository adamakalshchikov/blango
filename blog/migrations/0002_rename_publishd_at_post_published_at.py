# Generated by Django 3.2.5 on 2023-02-23 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publishd_at',
            new_name='published_at',
        ),
    ]
