# Generated by Django 2.1.5 on 2019-03-24 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('kyykka', '0002_auto_20190319_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='throw',
            name='score',
        ),
        migrations.RemoveField(
            model_name='throw',
            name='throw_number',
        ),
        migrations.AddField(
            model_name='throw',
            name='score_first',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='throw',
            name='score_fourth',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='throw',
            name='score_second',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='throw',
            name='score_third',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches',
                                    to='kyykka.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches',
                                    to='kyykka.Team'),
        ),
    ]