# Generated by Django 3.2 on 2021-04-21 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_food_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='desctiption',
            new_name='description',
        ),
    ]
