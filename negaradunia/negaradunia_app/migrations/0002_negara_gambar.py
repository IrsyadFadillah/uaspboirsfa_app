# Generated by Django 4.1.1 on 2022-10-31 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("negaradunia_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="negara",
            name="gambar",
            field=models.CharField(max_length=70, null=True),
        ),
    ]