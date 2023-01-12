# Generated by Django 4.1.3 on 2023-01-12 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0006_userinfo_depart"),
    ]

    operations = [
        migrations.AddField(
            model_name="userinfo",
            name="gender",
            field=models.SmallIntegerField(
                choices=[(1, "男"), (2, "女")], default=None, verbose_name="性别"
            ),
        ),
    ]
