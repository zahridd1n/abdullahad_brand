# Generated by Django 5.1.4 on 2024-12-10 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]