# Generated by Django 4.1 on 2022-09-14 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0015_candidate_experience_candidate_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='file',
            field=models.FileField(default='', upload_to='files'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='personality',
            field=models.CharField(choices=[('I am outgoing', 'I am outgoing'), ('I am antisocial', 'I am antisocial'), ('I am serious', 'I am serious')], max_length=50, null=True),
        ),
    ]
