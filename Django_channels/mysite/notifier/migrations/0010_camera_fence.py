# Generated by Django 2.1.3 on 2018-12-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifier', '0009_profile_loginchk'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='fence',
            field=models.BooleanField(default=False),
        ),
    ]
