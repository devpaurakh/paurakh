# Generated by Django 4.2.7 on 2023-12-03 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paurakh', '0006_rename_categoryies_skills_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categoryiesName',
            new_name='categoriesName',
        ),
    ]
