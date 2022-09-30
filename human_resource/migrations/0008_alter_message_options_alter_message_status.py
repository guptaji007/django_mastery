# Generated by Django 4.1 on 2022-09-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0007_message_email_message_name_message_phone_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('R', 'Read'), ('P', 'Pending')], default='P', max_length=1),
        ),
    ]
