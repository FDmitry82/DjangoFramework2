# Generated by Django 2.2.4 on 2019-10-23 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
        migrations.AddField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активен'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('FM', 'формируется'), ('STP', 'отправлен в обработку'), ('PD', 'оплачен'), ('PRD', 'обрабатывается'), ('RDY', 'готов к выдаче'), ('CNC', 'отменен')], default='FM', max_length=3, verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='создан'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='обновлен'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='ordersapp.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Product', verbose_name='продукт')),
            ],
        ),
    ]
