# Generated by Django 4.1.1 on 2023-01-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("negaradunia_app", "0002_negara_gambar"),
    ]

    operations = [
        migrations.CreateModel(
            name="Konservasi",
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
                ("nama_konservasi", models.CharField(max_length=20)),
                ("titik_koordinat", models.CharField(max_length=100)),
                ("letak_negara", models.CharField(max_length=50)),
            ],
        ),
    ]
