# Generated by Django 4.2.5 on 2023-09-28 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0003_alter_todo_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('C', 'Completed'), ('P', 'Pending'), ('S', 'Started')], max_length=1),
        ),
    ]
