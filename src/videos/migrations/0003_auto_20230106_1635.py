# Generated by Django 3.2.16 on 2023-01-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_videoproxy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoproxy',
            options={'verbose_name': 'Published Video', 'verbose_name_plural': 'Published Videos'},
        ),
        migrations.AddField(
            model_name='video',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
