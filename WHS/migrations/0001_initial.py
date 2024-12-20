# Generated by Django 4.2 on 2024-11-27 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("CONF", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="Barcode",
                    ),
                ),
                (
                    "sku",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        unique=True,
                        verbose_name="Sku",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        default="Description", max_length=50, verbose_name="Name"
                    ),
                ),
                ("safety", models.IntegerField(default=0, verbose_name="Safety")),
                (
                    "rdp",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=8, verbose_name="RDP"
                    ),
                ),
                (
                    "rrp",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=8, verbose_name="RRP"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now=True, verbose_name="Created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now_add=True, verbose_name="Updated"),
                ),
                (
                    "note",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Note"
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Item_Brand",
                        to="CONF.brand",
                        verbose_name="Brand",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Item_Category",
                        to="CONF.category",
                        verbose_name="Category",
                    ),
                ),
                (
                    "color",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Item_Color",
                        to="CONF.color",
                        verbose_name="Color",
                    ),
                ),
                (
                    "uom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Item_uom",
                        to="CONF.uom",
                        verbose_name="Uom",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "ITEMS",
            },
        ),
        migrations.CreateModel(
            name="Stock_In",
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
                (
                    "created",
                    models.DateTimeField(auto_now=True, verbose_name="Created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now_add=True, verbose_name="Updated"),
                ),
                (
                    "note",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Note"
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Stock_In_location",
                        to="CONF.whsbranch",
                        verbose_name="Location",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Stock_In_Supplier",
                        to="CONF.supplier",
                        verbose_name="Supplier",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "STOCK_IN",
            },
        ),
        migrations.CreateModel(
            name="Stock_Out",
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
                (
                    "created",
                    models.DateTimeField(auto_now=True, verbose_name="Created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now_add=True, verbose_name="Updated"),
                ),
                (
                    "note",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Note"
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Stock_Out_Customer",
                        to="CONF.customer",
                        verbose_name="Customer",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Stock_Out_location",
                        to="CONF.whsbranch",
                        verbose_name="Location",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "STOCK_OUT",
            },
        ),
        migrations.CreateModel(
            name="Stock_Out_Detail",
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
                ("quantity", models.IntegerField(default=0, verbose_name="Quantity")),
                (
                    "serial",
                    models.CharField(
                        blank=True,
                        default="None",
                        max_length=50,
                        null=True,
                        verbose_name="Serial",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now=True, verbose_name="Created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now_add=True, verbose_name="Updated"),
                ),
                (
                    "note",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Note"
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Stock_Out_Detail_item",
                        to="WHS.item",
                        verbose_name="Item",
                    ),
                ),
                (
                    "stock_out",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Stock_Out_Detail",
                        to="WHS.stock_out",
                        verbose_name="Transaction_No",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "STOCK_OUT_REF",
            },
        ),
        migrations.CreateModel(
            name="Stock_IN_Detail",
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
                ("quantity", models.IntegerField(default=0, verbose_name="Quantity")),
                (
                    "serial",
                    models.CharField(
                        blank=True,
                        default="None",
                        max_length=50,
                        null=True,
                        verbose_name="Serial",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now=True, verbose_name="Created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now_add=True, verbose_name="Updated"),
                ),
                (
                    "note",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Note"
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Stock_IN_Detail_item",
                        to="WHS.item",
                        verbose_name="Item",
                    ),
                ),
                (
                    "stock_in",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Stock_IN_Detail",
                        to="WHS.stock_in",
                        verbose_name="Transaction_No",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "STOCK_IN_REF",
            },
        ),
    ]
