# Generated by Django 3.1 on 2022-04-12 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_textdescriptioncomponent'),
    ]

    operations = [
        migrations.AddField(
            model_name='textcomponent',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='textdescriptioncomponent',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='textdescriptioncomponent',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
    ]