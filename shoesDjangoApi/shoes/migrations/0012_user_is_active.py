# Generated by Django 4.0.5 on 2022-06-20 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0011_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
