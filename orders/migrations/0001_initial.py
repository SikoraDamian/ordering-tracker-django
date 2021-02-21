# Generated by Django 3.1.2 on 2021-02-21 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_number', models.CharField(max_length=20)),
                ('total', models.CharField(max_length=20)),
                ('quote_status', models.CharField(choices=[('Creating', 'Creating'), ('Sent_for_quotation', 'Sent_for_quotation'), ('Quoted', 'Quoted'), ('In_links', 'In_links'), ('Ordered', 'Ordered'), ('Delivered', 'Delivered')], max_length=20)),
                ('cad_shared', models.IntegerField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.CharField(max_length=20)),
                ('descriptions', models.CharField(max_length=120)),
                ('request_status', models.CharField(choices=[('Quoted', 'Quoted'), ('Ordered', 'Ordered'), ('Completed', 'Completed'), ('On_hold', 'On_hold')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(choices=[('PHARMA', 'Pharma Stainless'), ('QED', 'QED'), ('DL', 'Dawnlough'), ('EMC', 'EMC'), ('McMasterCARR', 'McMasterCARR')], max_length=20)),
                ('order_status', models.CharField(choices=[('Quoted', 'Quoted'), ('Ordered', 'Ordered'), ('Delivered', 'Delivered'), ('Completed', 'Completed')], max_length=20)),
                ('ereq', models.CharField(max_length=20)),
                ('pr_pcard', models.CharField(max_length=20)),
                ('delivery', models.DateField()),
                ('quote_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.quote')),
                ('request_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.request')),
            ],
        ),
    ]