# Generated by Django 4.2.20 on 2025-04-01 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_game_post_game_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='game_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.game', to_field='game'),
        ),
    ]
