# Generated by Django 3.2 on 2021-12-11 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gifts', '0012_alter_gift_committed_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='committed_by',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
