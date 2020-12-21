# Generated by Django 3.1.4 on 2020-12-21 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banco_app', '0002_auto_20201217_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_transacao', models.CharField(choices=[('Débito', 'Débito'), ('Crédito', 'Crédito')], max_length=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco_app.cliente')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco_app.conta')),
            ],
        ),
    ]