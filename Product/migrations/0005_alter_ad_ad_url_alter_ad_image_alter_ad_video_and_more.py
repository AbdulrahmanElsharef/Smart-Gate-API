# Generated by Django 4.2 on 2024-11-06 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Product", "0004_remove_customuser_slug_remove_item_slug_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="ad_url",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="AD/ad_url/<function AD_directory at 0x786037bb5f30>",
            ),
        ),
        migrations.AlterField(
            model_name="ad",
            name="image",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="AD/image/<function AD_directory at 0x786037bb5f30>",
            ),
        ),
        migrations.AlterField(
            model_name="ad",
            name="video",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="AD/ad_videos/<function AD_directory at 0x786037bb5f30>",
            ),
        ),
        migrations.AlterField(
            model_name="complaint",
            name="customer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="Customer_Complaint",
                to="Product.customuser",
                verbose_name="Customer",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="Product_Items",
                to="Product.product",
                verbose_name="Product",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="room",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="Room_Item",
                to="Product.room",
                verbose_name="Room",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="users_list",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="User_Item",
                to="Product.customuser",
                verbose_name="User",
            ),
        ),
        migrations.AlterField(
            model_name="item_action",
            name="item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="Product_Action",
                to="Product.item",
                verbose_name="Item",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="last_version_url",
            field=models.FileField(
                blank=True,
                max_length=200,
                null=True,
                upload_to="Product/version_url/<function product_directory at 0x786037bb7250>",
            ),
        ),
        migrations.AlterField(
            model_name="product_action",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="Product_Action",
                to="Product.product",
                verbose_name="Product",
            ),
        ),
        migrations.AlterField(
            model_name="update",
            name="last_version_url",
            field=models.FileField(
                blank=True,
                max_length=200,
                null=True,
                upload_to="Update/version_url/<function update_directory at 0x786037bb70a0>",
            ),
        ),
        migrations.AlterField(
            model_name="update",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="Product_Update",
                to="Product.product",
                verbose_name="Product",
            ),
        ),
        migrations.AlterField(
            model_name="voice_command",
            name="item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="Item_Voice_Command",
                to="Product.item",
                verbose_name="Item",
            ),
        ),
    ]
