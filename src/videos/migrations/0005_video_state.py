# Generated by Django 3.2.16 on 2023-01-07 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_auto_20230107_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='state',
            field=models.CharField(choices=[('PU', 'Publish'), ('DR', 'Draft')], default='DR', max_length=2),
        ),
    ]