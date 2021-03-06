# Generated by Django 3.2.5 on 2021-07-07 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.PositiveSmallIntegerField(verbose_name='Цена')),
                ('image', models.ImageField(upload_to='product/image', verbose_name='Изображение')),
                ('available', models.BooleanField(default=True, verbose_name='В наличии')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя пользователя')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата заказа')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
