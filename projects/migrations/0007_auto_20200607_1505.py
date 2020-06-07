# Generated by Django 3.0.7 on 2020-06-07 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20200607_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='average_content',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='project',
            name='average_design',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='project',
            name='average_usability',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]