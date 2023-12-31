# Generated by Django 4.2.5 on 2023-10-28 09:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_alter_blog_posted_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="image",
            field=models.FileField(
                default="temp.jpg", upload_to="", verbose_name="Путь к картинке"
            ),
        ),
        migrations.AlterField(
            model_name="blog",
            name="posted",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2023, 10, 28, 14, 14, 10, 498841),
                verbose_name="Опубликована",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="date",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2023, 10, 28, 14, 14, 10, 499841),
                verbose_name="Дата",
            ),
        ),
    ]
