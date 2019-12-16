# Generated by Django 2.1.5 on 2019-07-13 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('comment', models.TextField()),
                ('published_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.ImageField(blank=True, upload_to='static/meme_review', verbose_name='img')),
                ('caption', models.TextField(max_length=200)),
                ('published_date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='for_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meme_review.Post'),
        ),
    ]
