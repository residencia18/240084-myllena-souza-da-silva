# Generated by Django 5.0.3 on 2024-03-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bebida",
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
                ("nome", models.CharField(max_length=200)),
                ("preco", models.DecimalField(decimal_places=2, max_digits=3)),
                ("data_registro", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
