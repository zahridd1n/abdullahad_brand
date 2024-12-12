# Generated by Django 5.1.4 on 2024-12-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_service_icon_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='workprogress',
            name='icon_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workprogress',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='works/'),
        ),
    ]
