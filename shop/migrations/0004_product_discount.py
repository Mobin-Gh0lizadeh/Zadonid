# Generated by Django 3.2.3 on 2021-08-10 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210621_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]