# Generated by Django 3.0.1 on 2020-01-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_books_book_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_publish_time',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='图书出版时间'),
        ),
    ]