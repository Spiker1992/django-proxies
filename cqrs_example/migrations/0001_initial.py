# Generated by Django 5.0.1 on 2024-05-09 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('status', models.CharField(default='draft', max_length=30)),
            ],
        ),
    ]
