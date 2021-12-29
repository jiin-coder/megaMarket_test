# Generated by Django 4.0 on 2021-12-28 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productreal',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_reals', to='products.product'),
        ),
        migrations.AlterField(
            model_name='productreal',
            name='stock_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='재고개수, 품절일때 유용함'),
        ),
    ]