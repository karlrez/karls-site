# Generated by Django 2.1.5 on 2019-07-13 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meme_review', '0002_auto_20190713_0010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pub',
            new_name='pub_date',
        ),
    ]
