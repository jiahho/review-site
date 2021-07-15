# Generated by Django 2.2.5 on 2021-07-15 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210713_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorite_book_genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book_genre', to='categories.Category'),
        ),
        migrations.AlterField(
            model_name='user',
            name='favorite_movie_genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movie_genre', to='categories.Category'),
        ),
    ]
