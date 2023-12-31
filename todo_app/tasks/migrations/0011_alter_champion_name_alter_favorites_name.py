# Generated by Django 4.2.3 on 2023-07-25 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champion',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='champion_name', to='tasks.champion', to_field='name'),
        ),
    ]
