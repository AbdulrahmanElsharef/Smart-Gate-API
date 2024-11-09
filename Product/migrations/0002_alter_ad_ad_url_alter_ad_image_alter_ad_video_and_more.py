# Generated by Django 4.2 on 2024-11-06 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="ad_url",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="AD/ad_url/<function AD_directory at 0x757285ba4700>",
            ),
        ),
        migrations.AlterField(
            model_name="ad",
            name="image",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="AD/image/<function AD_directory at 0x757285ba4700>",
            ),
        ),
        migrations.AlterField(
            model_name="ad",
            name="video",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="AD/ad_videos/<function AD_directory at 0x757285ba4700>",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="last_version_url",
            field=models.FileField(
                blank=True,
                max_length=200,
                null=True,
                upload_to="Product/version_url/<function product_directory at 0x757285e6a4d0>",
            ),
        ),
        migrations.AlterField(
            model_name="update",
            name="last_version_url",
            field=models.FileField(
                blank=True,
                max_length=200,
                null=True,
                upload_to="Update/version_url/<function update_directory at 0x757285e6b010>",
            ),
        ),
    ]
