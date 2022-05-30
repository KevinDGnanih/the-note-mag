# Generated by Django 3.2 on 2022-05-30 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mag_app', '0009_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('playlist', 'playlist'), ('review', 'review'), ('music', 'music'), ('concert', 'concert')], default='Music', max_length=200),
        ),
    ]
