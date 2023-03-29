from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators

from utils.validators import validate_phone_number


class Gateway(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='gateways/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    # credentials = models.TextField(_('credentials'), blank=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'gateways'
        verbose_name = _('Gateway')
        verbose_name_plural = _('Gateways')


class Payment(models.Model):
    STATUS_VOID = 0
    STATUS_PAID = 10 # pardakht ok shod
    STATUS_ERROR = 20 # error bade pardakht for ex. ghati net or systembanki
    STATUS_CANCELED = 30 # cancle pardakht
    STATUS_REFUNDED = 31 # bargasht pol
    STATUS_CHOICES = (
        (STATUS_VOID, _('Void')),
        (STATUS_PAID, _('Paid')),
        (STATUS_ERROR, _('Error')),
        (STATUS_CANCELED, _('User Canceled')),
        (STATUS_REFUNDED, _('Refunded')),
    )

    STATUS_TRANSLATIONS = {
        (STATUS_VOID, _('Payment could not be processed')),
        (STATUS_PAID, _('Payment successful')),
        (STATUS_ERROR, _('Payment has encountered an error.')),
        (STATUS_CANCELED, _('Payment canceled by user.')),
        (STATUS_REFUNDED, _('This payment has been refunded')),
    }

    user = models.ForeignKey('users.User',verbose_name=_('user'), related_name='%(class)s', on_delete=models.CASCADE)
    package = models.ForeignKey('subscriptions.Package', verbose_name=_('package'), related_name='%(class)s', on_delete=models.CASCADE)
    gateway = models.ForeignKey(Gateway, verbose_name=_('gateway'), related_name='%(class)s', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(_('price'), default=0)
    status = models.PositiveSmallIntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_VOID, db_index=True)
    device_uuid = models.CharField(_('device uuid'), max_length=40, blank=True)
    phone_number = models.BigIntegerField(_('phone number'), validators=[validate_phone_number], db_index=True)
    notify_token = models.CharField(
        _('Notification Token'), max_length=200, blank=True,
        validators=[validators.RegexValidator(r'([a-z]|[A-Z]|[0-9])\w+',
                                              _('Notify token is not valid'), 'invalid')]
    )
    # consumed code === shomare peygiri
    consumed_code = models.PositiveIntegerField(_('consumed reference code'), null=True, db_index=True)
    created_time = models.DateTimeField(_('creation time'), auto_now_add=True, db_index=True)
    updated_time = models.DateTimeField(_('modification time'), auto_now=True)


    class Meta:
        db_table = 'payments'
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')