# Generated by Django 5.2.4 on 2025-07-29 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_remove_participant_events_participant_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='event',
        ),
        migrations.AddField(
            model_name='participant',
            name='events',
            field=models.ManyToManyField(to='events.event'),
        ),
    ]
