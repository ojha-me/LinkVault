# Generated by Django 5.1.6 on 2025-02-27 16:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=500)),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Studies', 'Studies'), ('Work', 'Work'), ('Coding', 'Coding'), ('Content Creation', 'Content Creation'), ('Other', 'Other')], default='Other', max_length=50)),
                ('reminder_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('forgotten_notified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
