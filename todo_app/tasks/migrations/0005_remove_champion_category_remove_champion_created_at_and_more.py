# Generated by Django 4.2.3 on 2023-07-21 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_categories_options_champion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champion',
            name='category',
        ),
        migrations.RemoveField(
            model_name='champion',
            name='created_at',
        ),
        migrations.AddField(
            model_name='champion',
            name='descrption',
            field=models.TextField(blank=True, null=True),
        ),
    ]
