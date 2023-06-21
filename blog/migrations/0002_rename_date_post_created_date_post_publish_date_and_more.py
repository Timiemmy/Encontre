# Generated by Django 4.2.2 on 2023-06-21 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="date",
            new_name="created_date",
        ),
        migrations.AddField(
            model_name="post",
            name="publish_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                max_length=255, null=True, unique_for_date="publish_date"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[("DF", "Draft"), ("PB", "Published")],
                default="PB",
                max_length=2,
            ),
        ),
    ]