# Generated by Django 2.1.5 on 2019-07-13 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls_app', '0005_remove_question_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, upload_to='static/polls_app', verbose_name='img'),
        ),
    ]
