# Generated by Django 5.1.3 on 2025-03-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_client_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='role',
            field=models.CharField(choices=[('customer', 'Customer'), ('admin', 'Admin')], default='customer', max_length=20),
        ),
    ]
