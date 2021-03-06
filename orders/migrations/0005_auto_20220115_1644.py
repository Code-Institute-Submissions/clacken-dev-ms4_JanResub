# Generated by Django 3.2.9 on 2022-01-15 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_description'),
        ('orders', '0004_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='user',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='customer_name',
            field=models.CharField(default=2, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonial',
            name='product_purchased',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='products.product'),
        ),
    ]
