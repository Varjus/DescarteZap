# Generated by Django 3.1.7 on 2021-11-20 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0018_auto_20211120_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doacaolist',
            name='doadores_ptr',
        ),
        migrations.AlterField(
            model_name='doacaolist',
            name='doacao_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cadastros.doacao'),
        ),
    ]