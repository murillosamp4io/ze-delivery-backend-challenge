# Generated by Django 2.2.12 on 2020-05-06 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_remove_partner_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='document',
            field=models.CharField(default='', max_length=18, unique=True),
        ),
    ]