# Generated by Django 4.2.7 on 2023-12-03 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paurakh', '0004_rename_catagoryies_catagory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catagory',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='catagoryiesName',
            new_name='categoryiesName',
        ),
        migrations.RenameField(
            model_name='skills',
            old_name='Catagoryies',
            new_name='Categoryies',
        ),
    ]