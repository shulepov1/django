# Generated by Django 4.2.5 on 2023-11-25 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_alter_award_players'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='award',
            unique_together={('name', 'year')},
        ),
    ]
