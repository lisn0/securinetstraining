# Generated by Django 2.0.1 on 2018-02-07 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf_framework', '0004_auto_20180131_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]