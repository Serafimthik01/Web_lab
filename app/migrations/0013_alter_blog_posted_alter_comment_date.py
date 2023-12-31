# Generated by Django 4.2.5 on 2023-10-28 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0012_alter_blog_posted_alter_comment_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="posted",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2023, 10, 28, 21, 17, 32, 777643),
                verbose_name="Опубликована",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="date",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2023, 10, 28, 21, 17, 32, 778644),
                verbose_name="Дата",
            ),
        ),
    ]
