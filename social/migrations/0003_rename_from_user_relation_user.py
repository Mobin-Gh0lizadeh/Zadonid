# Generated by Django 3.2.3 on 2021-06-17 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_relation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relation',
            old_name='from_user',
            new_name='user',
        ),
    ]
