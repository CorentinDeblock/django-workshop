# Generated by Django 2.2.6 on 2019-10-09 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20191009_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
