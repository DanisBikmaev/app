# Generated by Django 4.1.4 on 2022-12-23 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='blog.tag'),
        ),
    ]