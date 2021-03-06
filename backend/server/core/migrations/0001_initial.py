# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-30 14:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('zipCode', models.CharField(max_length=255, null=True)),
                ('region', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Location address',
                'verbose_name_plural': 'Location addresses',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL)),
                ('forwarder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forwarder', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Chat',
                'verbose_name_plural': 'Chats',
            },
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField(default='', max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='issue_doc/')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Chat')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Chat Message',
                'verbose_name_plural': 'Chat Messages',
            },
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True)),
                ('value', models.TextField()),
            ],
            options={
                'verbose_name': 'Configuration',
                'verbose_name_plural': 'Configurations',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateUpdated', models.DateTimeField(default=django.utils.timezone.now)),
                ('code', models.CharField(max_length=20, null=True, unique=True)),
                ('usd', models.FloatField(default=0.0)),
                ('eur', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('userAgent', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.IntegerField(choices=[(1, b'Against policy'), (2, b'Not corresponding'), (3, b'Not received'), (4, b'Other issue')])),
                ('description', models.TextField(default='', max_length=500)),
                ('state', models.CharField(choices=[(b'OPEN', b'OPEN'), (b'CLOSED', b'CLOSED')], default=b'OPEN', max_length=25)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Chat')),
            ],
            options={
                'verbose_name': 'Issue',
                'verbose_name_plural': 'Issues',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('countryCode', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('street', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('zipcode', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('lat', models.FloatField(default=0.0, null=True)),
                ('lng', models.FloatField(default=0.0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Create DateTime')),
                ('email', models.BooleanField(default=False)),
                ('sms', models.BooleanField(default=False)),
                ('alert', models.BooleanField(default=False)),
                ('emailNotified', models.BooleanField(default=False)),
                ('smsNotified', models.BooleanField(default=False)),
                ('alertNotified', models.BooleanField(default=False)),
                ('emailSubject', models.TextField(blank=True, max_length=255, null=True)),
                ('emailData', models.TextField(blank=True, null=True)),
                ('smsData', models.TextField(blank=True, null=True)),
                ('alertData', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Create DateTime')),
                ('estimatedDate', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Estimated DateTime')),
                ('forwarderDeliveryDate', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Estimated Delivery DateTime')),
                ('collectorDeliveryDate', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Collector Delivery DateTime')),
                ('forwardedDate', models.DateTimeField(null=True, verbose_name='Forwarded DateTime')),
                ('goodType', models.IntegerField(default=0)),
                ('shippingMode', models.IntegerField(default=0)),
                ('totalPrice', models.FloatField(default=0)),
                ('shippingModePrice', models.FloatField(default=0)),
                ('shippingWeight', models.FloatField(default=0)),
                ('totalInsurance', models.BooleanField(default=False)),
                ('state', models.CharField(choices=[(b'NEW', b'NEW'), (b'PAID', b'PAID'), (b'CANCELLED', b'CANCELLED'), (b'ACCEPTED', b'ACCEPTED'), (b'REFUSED', b'REFUSED'), (b'DELIVERED', b'DELIVERED'), (b'FORWARDED', b'FORWARDED'), (b'COLLECTING', b'COLLECTING'), (b'RECEIVED', b'RECEIVED')], default=b'NEW', max_length=25)),
                ('code', models.CharField(default='', max_length=25)),
                ('refuseReason', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('score', models.FloatField(default=0)),
                ('text', models.TextField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('orderStatus', models.CharField(choices=[(b'NEW', b'NEW'), (b'PAID', b'PAID'), (b'CANCELLED', b'CANCELLED'), (b'ACCEPTED', b'ACCEPTED'), (b'REFUSED', b'REFUSED'), (b'DELIVERED', b'DELIVERED'), (b'FORWARDED', b'FORWARDED'), (b'COLLECTING', b'COLLECTING'), (b'RECEIVED', b'RECEIVED')], max_length=25, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='order_docs_front/')),
                ('description', models.TextField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderTrackingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('courier', models.CharField(choices=[(b'COURIER01', b'DHL'), (b'COURIER02', b'UPS'), (b'COURIER03', b'FedEx'), (b'COURIERCUSTOM', b'Other')], max_length=100)),
                ('courierOther', models.CharField(blank=True, max_length=100, null=True)),
                ('trn', models.CharField(max_length=100)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('fromForwarder', models.BooleanField(default=False)),
                ('trackingStatus', models.CharField(choices=[(b'1', b'First'), (b'2', b'Second'), (b'3', b'Third')], max_length=100)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Order')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerCourier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(default='', max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerCourierArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countryName', models.CharField(default='', max_length=100)),
                ('areaName', models.CharField(default='', max_length=15)),
                ('partnerCourier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PartnerCourier')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerCourierDestinationZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinationCountryName', models.CharField(default='', max_length=55)),
                ('zone', models.IntegerField(default=0)),
                ('partnerCourier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PartnerCourier')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerCourierOriginDestinationZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originArea', models.CharField(default='', max_length=15)),
                ('destinationArea', models.CharField(default='', max_length=15)),
                ('zone', models.IntegerField(default=0)),
                ('partnerCourier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PartnerCourier')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerCourierPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(default='', max_length=15)),
                ('price', models.FloatField(default='0.0')),
                ('zone', models.IntegerField(default=0)),
                ('type', models.CharField(choices=[(b'cheap', b'Cheap'), (b'standard', b'Standard'), (b'express', b'Express')], default=b'express', max_length=25)),
                ('partnerCourier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PartnerCourier')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activationKey', models.CharField(max_length=40)),
                ('verificationCode', models.CharField(default='0000', max_length=6)),
                ('keyExpires', models.DateTimeField()),
                ('dob', models.DateField(null=True)),
                ('ssn', models.CharField(default=None, max_length=255, null=True, unique=True)),
                ('mobile', models.CharField(default='', max_length=255)),
                ('mobileVerified', models.BooleanField(default=False)),
                ('enable2FASMS', models.BooleanField(default=False)),
                ('enable2FAGoogle', models.BooleanField(default=False)),
                ('termsAgreement', models.BooleanField(default=False)),
                ('accountTier', models.CharField(default='TIER_0', max_length=6)),
                ('feedback', models.FloatField(default=0.0)),
                ('avatarImage', models.ImageField(blank=True, null=True, upload_to='avatar/')),
                ('IDDocFrontImage', models.ImageField(blank=True, null=True, upload_to='id_docs_front/')),
                ('IDDocBackImage', models.ImageField(blank=True, null=True, upload_to='id_docs_back/')),
                ('docVerified', models.BooleanField(default=False)),
                ('ProofOfresidenceImage', models.ImageField(blank=True, null=True, upload_to='por_docs/')),
                ('ProofOfresidenceVerified', models.BooleanField(default=False)),
                ('SelfIDocImage', models.ImageField(blank=True, null=True, upload_to='self_id_docs/')),
                ('SelfIDocVerified', models.BooleanField(default=False)),
                ('oneSignalPlayerId', models.CharField(editable=False, max_length=255, null=True)),
                ('oneSignalPushToken', models.CharField(editable=False, max_length=255, null=True)),
                ('addresses', models.ManyToManyField(to='core.Address')),
                ('defaultAddress', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_address', to='core.Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Create DateTime')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Create DateTime')),
                ('type', models.CharField(choices=[(b'p2p-freight', b'P2P Freight Forwarding'), (b'package-collecting', b'Package Collecting'), (b'express-delivery', b'Express Delivery')], max_length=25)),
                ('title', models.CharField(default='', max_length=100)),
                ('enabled', models.BooleanField(default=False)),
                ('maxSize', models.IntegerField(default=0)),
                ('maxWeight', models.IntegerField(default=0)),
                ('totalAssurance', models.BooleanField(default=False)),
                ('acceptedPacksFromPrivate', models.BooleanField(default=False)),
                ('acceptedPacksFromCompany', models.BooleanField(default=False)),
                ('addPartnerForwarder', models.BooleanField(default=False)),
                ('partnerForwarderMargin', models.FloatField(default=0.0)),
                ('addOtherPartner', models.BooleanField(default=False)),
                ('otherCourierPartnerName', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('price', models.FloatField(default=0.0)),
                ('priceCheap', models.FloatField(default=0.0)),
                ('priceStandard', models.FloatField(default=0.0)),
                ('priceExpress', models.FloatField(default=0.0)),
                ('priceCheapEnabled', models.BooleanField(default=True)),
                ('priceStandardEnabled', models.BooleanField(default=False)),
                ('priceExpressEnabled', models.BooleanField(default=False)),
                ('sunday', models.BooleanField(default=False)),
                ('monday', models.BooleanField(default=False)),
                ('tuesday', models.BooleanField(default=False)),
                ('wednesday', models.BooleanField(default=False)),
                ('thursday', models.BooleanField(default=False)),
                ('friday', models.BooleanField(default=False)),
                ('saturday', models.BooleanField(default=False)),
                ('deliveryOnDawn', models.BooleanField(default=False)),
                ('deliveryOnMorning', models.BooleanField(default=False)),
                ('deliveryOnLunchTime', models.BooleanField(default=False)),
                ('deliveryOnAfternoon', models.BooleanField(default=False)),
                ('deliveryOnEvening', models.BooleanField(default=False)),
                ('deliveryOnNight', models.BooleanField(default=False)),
                ('locationFrom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_from', to='core.Location')),
                ('locationTos', models.ManyToManyField(related_name='location_tos', to='core.Location')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Profile')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='timeSlots',
            field=models.ManyToManyField(to='core.TimeSlot'),
        ),
        migrations.AddField(
            model_name='ordertrackinginfo',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Profile'),
        ),
        migrations.AddField(
            model_name='ordernote',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Profile'),
        ),
        migrations.AddField(
            model_name='orderfeedback',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Profile'),
        ),
        migrations.AddField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Profile'),
        ),
        migrations.AddField(
            model_name='order',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Service'),
        ),
        migrations.AddField(
            model_name='issue',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Order'),
        ),
        migrations.AddField(
            model_name='issue',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Profile'),
        ),
        migrations.AddField(
            model_name='event',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Profile'),
        ),
    ]
