# Generated by Django 4.2.3 on 2023-07-21 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_remove_champion_category_remove_champion_created_at_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Champion',
            new_name='Items',
        ),
    ]
