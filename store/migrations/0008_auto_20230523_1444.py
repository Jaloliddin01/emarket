# Generated by Django 4.2.1 on 2023-05-23 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rename_customers_last_na_89bb5f_idx_store_custo_last_na_e6a359_idx_and_more'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO store_collection (title)
            VALUES ('collection1')
        """, """
            DELETE FROM store_collection
            WHERE title='collection1'
        """)
    ]