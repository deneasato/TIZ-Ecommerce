# Generated by Django 5.1.4 on 2025-03-31 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_orderitem'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='packageitem',
            constraint=models.UniqueConstraint(fields=('package', 'product'), name='package_product Uniqueness'),
        ),
    ]
