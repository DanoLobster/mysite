# Generated by Django 4.2.1 on 2023-07-01 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0007_outfit'),
    ]

    operations = [
        migrations.CreateModel(
            name='MergedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='merged_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterField(
            model_name='clothing',
            name='category',
            field=models.CharField(choices=[('headwear', 'Headwear'), ('neckwear', 'Neckwear'), ('top', 'Top'), ('bottom', 'Bottom'), ('legwear', 'Legwear'), ('feetwear', 'Feetwear'), ('underwear', 'Underwear'), ('underwear', 'Accessory'), ('other', 'Other')], default='other', max_length=15),
        ),
        migrations.DeleteModel(
            name='Outfit',
        ),
    ]
