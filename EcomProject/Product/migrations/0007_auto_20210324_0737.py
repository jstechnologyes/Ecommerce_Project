# Generated by Django 3.1.5 on 2021-03-24 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_auto_20210323_0837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
    ]
