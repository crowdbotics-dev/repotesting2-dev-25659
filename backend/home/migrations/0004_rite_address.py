# Generated by Django 2.2.26 on 2022-07-11 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_rite"),
    ]

    operations = [
        migrations.AddField(
            model_name="rite",
            name="address",
            field=models.TextField(blank=True, null=True),
        ),
    ]
