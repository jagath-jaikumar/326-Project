# Generated by Django 2.0.2 on 2018-04-03 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tibl', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='my_user',
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
