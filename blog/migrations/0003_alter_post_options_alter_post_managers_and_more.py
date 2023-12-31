# Generated by Django 4.2.2 on 2023-06-21 12:39

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_rename_date_post_created_date_post_publish_date_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-publish_date"]},
        ),
        migrations.AlterModelManagers(
            name="post",
            managers=[
                ("published", django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name="post",
            name="likes",
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(
                fields=["-publish_date"], name="blog_post_publish_7e8b08_idx"
            ),
        ),
    ]
