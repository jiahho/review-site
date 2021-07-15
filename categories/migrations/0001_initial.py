# Generated by Django 2.2.5 on 2021-07-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=10)),
                ('kind', models.CharField(blank=True, choices=[('book', 'Book'), ('movie', 'Movie'), ('both', 'Both')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]