# Generated by Django 5.0.6 on 2024-06-01 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="detail",
            field=models.TextField(),
        ),
    ]
