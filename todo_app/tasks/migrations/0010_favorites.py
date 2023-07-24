# Generated by Django 4.2.3 on 2023-07-24 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0009_rename_descrption_champion_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='champion_name', to='tasks.champion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='champion_favorite', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
