# Generated by Django 2.2.6 on 2019-10-09 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20191009_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.FileField(default='', upload_to='static/upload/'),
        ),
    ]