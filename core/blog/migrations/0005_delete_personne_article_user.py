# Generated by Django 4.2 on 2023-08-10 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_personne'),
    ]

    operations = [
        migrations.DeleteModel(
            name='personne',
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
