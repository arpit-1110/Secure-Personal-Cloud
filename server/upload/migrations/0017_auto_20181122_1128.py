# Generated by Django 2.1.2 on 2018-11-22 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0016_auto_20181122_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='md5sum',
        ),
        migrations.AddField(
            model_name='file',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
