# Generated by Django 4.2.1 on 2023-07-01 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0008_mergedimage_delete_category_alter_clothing_category_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MergedImage',
        ),
    ]
