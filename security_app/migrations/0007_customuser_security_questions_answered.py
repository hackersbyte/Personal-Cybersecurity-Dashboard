# Generated by Django 4.2.7 on 2023-11-21 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security_app', '0006_customuser_active_sessions_customuser_device_history_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='security_questions_answered',
            field=models.BooleanField(default=False),
        ),
    ]