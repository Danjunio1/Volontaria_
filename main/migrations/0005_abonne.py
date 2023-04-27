# Generated by Django 4.1.7 on 2023-04-23 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_remove_comment_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Abonne",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("created", models.DateField(auto_now_add=True)),
                ("updated", models.DateField(auto_now=True)),
            ],
        ),
    ]
