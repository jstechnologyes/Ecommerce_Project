# Generated by Django 3.1.5 on 2021-03-25 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0008_auto_20210324_0802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
    ]
