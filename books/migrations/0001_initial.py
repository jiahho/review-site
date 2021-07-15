# Generated by Django 2.2.5 on 2021-07-15 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0002_auto_20210715_1158'),
        ('categories', '0002_auto_20210715_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('cover_image', models.ImageField(null=True, upload_to='')),
                ('rating', models.IntegerField(null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.Category')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]