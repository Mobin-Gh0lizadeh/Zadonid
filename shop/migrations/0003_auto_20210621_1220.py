# Generated by Django 3.2.3 on 2021-06-21 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_comment_save_share_vote'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created',)},
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
    ]
