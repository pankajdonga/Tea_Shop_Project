# Generated by Django 5.1.1 on 2024-11-13 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('product_img', models.ImageField(upload_to='media/')),
                ('select_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.productcategorymodel')),
            ],
        ),
    ]
