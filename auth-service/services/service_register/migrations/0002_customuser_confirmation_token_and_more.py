# Generated by Django 5.1.1 on 2024-10-07 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='confirmation_token',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
