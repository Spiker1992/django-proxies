# Generated by Django 5.0.1 on 2024-02-22 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PublishedBlog',
        ),
        migrations.CreateModel(
            name='PublishedPost',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('blog.post',),
        ),
        migrations.CreateModel(
            name='ReadyForReviewPost',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('blog.post',),
        ),
    ]
