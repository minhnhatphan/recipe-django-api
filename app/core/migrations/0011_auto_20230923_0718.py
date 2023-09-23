# Generated by Django 3.2.21 on 2023-09-23 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_recipe_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='core.Ingredient'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
        ),
    ]