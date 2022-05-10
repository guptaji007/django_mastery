# Generated by Django 4.0.4 on 2022-05-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0006_vacancy_timer'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='email',
            field=models.EmailField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='phone',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]
