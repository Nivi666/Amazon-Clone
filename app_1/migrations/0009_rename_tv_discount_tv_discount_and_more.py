# Generated by Django 4.1.4 on 2023-02-20 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0008_search_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tv',
            old_name='tv_discount',
            new_name='discount',
        ),
        migrations.RenameField(
            model_name='tv',
            old_name='tv_discount_price',
            new_name='discount_price',
        ),
        migrations.RenameField(
            model_name='tv',
            old_name='tv_head',
            new_name='head',
        ),
        migrations.RenameField(
            model_name='tv',
            old_name='tv_integer_dicount',
            new_name='int_dicount_price',
        ),
        migrations.RenameField(
            model_name='tv',
            old_name='tv_integer_orginal',
            new_name='int_orginal_price',
        ),
        migrations.RenameField(
            model_name='tv',
            old_name='tv_orginal_price',
            new_name='orginal_price',
        ),
    ]
