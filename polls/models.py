from django.db import models


# Create your models here.
from django.utils.translation import ugettext_lazy as _


class Question(models.Model):
    questionText = models.CharField(max_length=200, verbose_name=_('question|questionText'))
    pubDate = models.DateTimeField(_('question|datePublished'))

    def __str__(self):
        return self.questionText

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('question|plural')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_('question'))
    choiceText = models.CharField(max_length=200, verbose_name=_('choice|choiceText'))
    votes = models.IntegerField(default=0, verbose_name=_('choice|votes'))

    def __str__(self):
        s = ": "
        return s.join((self.question.questionText, self.choiceText))

    class Meta:
        verbose_name = _('choice')
        verbose_name_plural = _('choice|plural')
