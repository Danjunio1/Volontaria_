# Generated by Django 4.1.7 on 2023-04-21 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_article_vue_alter_article_poster"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="email",
        ),
    ]
