# Generated by Django 5.2 on 2025-04-23 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optima', '0002_users_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='passs',
            field=models.CharField(max_length=18),
        ),
    ]
