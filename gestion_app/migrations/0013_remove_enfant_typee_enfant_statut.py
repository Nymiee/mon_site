# Generated by Django 5.1.1 on 2025-04-02 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_app', '0012_rename_type_enfant_typee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfant',
            name='typee',
        ),
        migrations.AddField(
            model_name='enfant',
            name='statut',
            field=models.CharField(blank=True, choices=[('Enfant', 'Enfant'), ('Orphelin', 'Orphelin')], max_length=20, null=True),
        ),
    ]
