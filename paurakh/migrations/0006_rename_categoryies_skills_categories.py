# Generated by Django 4.2.7 on 2023-12-03 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paurakh', '0005_rename_catagory_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='Categoryies',
            new_name='Categories',
        ),
    ]