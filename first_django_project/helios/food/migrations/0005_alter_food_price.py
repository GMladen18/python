# Generated by Django 3.2 on 2021-04-22 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_rename_desctiption_food_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.FloatField(),
        ),
    ]
