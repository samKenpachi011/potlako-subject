from django.db import models
from edc_base.utils import get_utcnow
from edc_base.model_validators import date_is_future, date_not_future

from ..choices import SMS_OUTCOME


class SMS(models.Model):

    date_time_form_filled = models.DateTimeField(
        verbose_name='Date SMS form filled',
        default=get_utcnow,)

    next_ap_date = models.DateField(
        verbose_name='Date of next appointment (referral or return)',
        validators=[date_is_future, ],)

    date_reminder_sent = models.DateField(
        verbose_name='Date visit reminder SMS sent',
        validators=[date_not_future, ],)

    sms_outcome = models.CharField(
        verbose_name='Outcome of reminder SMS',
        choices=SMS_OUTCOME,
        max_length=50,)

    class Meta:
        app_label = 'potlako_subject'
        verbose_name = 'SMS'
        verbose_name_plural = 'SMSes'