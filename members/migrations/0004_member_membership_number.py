# Generated by Django 4.1.7 on 2023-02-17 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_double_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='membership_number',
            field=models.IntegerField(null=True),
        ),
    ]
