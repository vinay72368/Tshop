# Generated by Django 3.2.7 on 2021-10-14 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_sizevariant'),
    ]

    operations = [
        migrations.AddField(
            model_name='tshirt',
            name='slug',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
