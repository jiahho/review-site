# Generated by Django 2.2.5 on 2021-07-15 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'people'},
        ),
    ]
