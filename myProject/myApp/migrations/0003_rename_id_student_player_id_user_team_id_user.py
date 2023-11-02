# Generated by Django 4.2.5 on 2023-10-02 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0002_player_id_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='id_student',
            new_name='id_user',
        ),
        migrations.AddField(
            model_name='team',
            name='id_user',
            field=models.ForeignKey(blank=True, help_text='выберите id пользователя', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id пользователя'),
        ),
    ]