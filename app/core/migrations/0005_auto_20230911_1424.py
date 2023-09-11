# Generated by Django 3.2.21 on 2023-09-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230910_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=None, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
