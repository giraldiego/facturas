# Generated by Django 4.1.5 on 2023-01-31 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('creation_at', models.DateTimeField(auto_now_add=True)),
                ('due_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_status', models.CharField(choices=[('current', 'activa'), ('paid', 'pagado'), ('unpaid', 'sin pagar'), ('expired', 'vencida')], default='activa', max_length=100)),
                ('comment', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.client')),
            ],
        ),
    ]
