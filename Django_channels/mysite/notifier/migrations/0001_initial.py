# Generated by Django 2.1.1 on 2018-11-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cam_id', models.IntegerField(default=0)),
                ('cam_status', models.CharField(max_length=20)),
                ('cam_location', models.CharField(max_length=50)),
            ],
        ),
    ]
