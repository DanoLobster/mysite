# Generated by Django 4.2.1 on 2023-06-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0004_alter_clothing_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('clothing', models.ManyToManyField(to='wardrobe.clothing')),
            ],
        ),
    ]
