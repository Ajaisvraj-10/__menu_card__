# Generated by Django 5.0.4 on 2024-04-22 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_backend', '0005_alter_hotelusers_amount_alter_hotelusers_tax_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelusers',
            name='amount',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hotelusers',
            name='mobile',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='hotelusers',
            name='tax',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hotelusers',
            name='total_amount',
            field=models.BigIntegerField(null=True),
        ),
    ]
