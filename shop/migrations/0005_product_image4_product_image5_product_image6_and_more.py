# Generated by Django 5.2.4 on 2025-07-15 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_product_views"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image4",
            field=models.FileField(
                null=True, upload_to="shop/images/", verbose_name="تصویر کالا"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="image5",
            field=models.FileField(
                null=True, upload_to="shop/images/", verbose_name="تصویر کالا"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="image6",
            field=models.FileField(
                null=True, upload_to="shop/images/", verbose_name="تصویر کالا"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image1",
            field=models.FileField(
                null=True, upload_to="shop/images/", verbose_name="تصویر کالا"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image2",
            field=models.FileField(
                null=True, upload_to="shop/images/", verbose_name="تصویر کالا"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image3",
            field=models.FileField(
                null=True, upload_to="shop/images/", verbose_name="تصویر کالا"
            ),
        ),
    ]
