# Generated by Django 4.2.13 on 2024-05-29 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0002_alter_project_user_alter_story_project_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('description', models.CharField(max_length=150)),
                ('image', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('unlimited', models.BooleanField(default=False)),
                ('delivery_date', models.DateTimeField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to='projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='RewardItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('image', models.CharField(max_length=255)),
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='rewards.reward')),
            ],
        ),
    ]
