# Generated by Django 5.1.4 on 2025-03-15 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_package_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packageitem',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_items', to='store.package'),
        ),
    ]
