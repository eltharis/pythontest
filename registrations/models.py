from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class TeacherGrade(models.Model):
    teacherGradeShort = models.TextField(max_length=5, verbose_name=_('teacherGrade|short'))
    teacherGradeLong = models.TextField(max_length=10, verbose_name=_('teacherGrade|long'))

    def __str__(self):
        return self.teacherGradeShort

    class Meta:
        verbose_name = _('teacherGrade')
        verbose_name_plural = _('teacherGrade|plural')


class Teacher(models.Model):
    teacherName = models.TextField(max_length=200, verbose_name=_('teacher|name'))
    teacherGrade = models.ForeignKey(TeacherGrade)

    def __str__(self):
        return "%s %s" % (str(self.teacherGrade), self.teacherName)

    class Meta:
        verbose_name = _('teacher')
        verbose_name_plural = _('teacher|plural')


class TermType(models.Model):
    typeName = models.TextField(max_length=100, verbose_name=_('termType|name'))

    def __str__(self):
        return self.typeName

    class Meta:
        verbose_name = _('termType')
        verbose_name_plural = _('termType|plural')


class Term(models.Model):
    termName = models.TextField(max_length=200, verbose_name=_('term|name'))
    termTeacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    termMaxStudents = models.IntegerField(verbose_name=_('term|maxStudents'), default=15)
    termType = models.ForeignKey(TermType)

    def __str__(self):
        return "%s: %s - %s" % (str(self.termType), self.termName, str(self.termTeacher))

    class Meta:
        verbose_name = _('term')
        verbose_name_plural = _('term|plural')


class TermTime(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE, verbose_name=_('term'))
    timeStart = models.TimeField(verbose_name=_('termTime|start'))
    timeStop = models.TimeField(verbose_name=_('termTime|stop'))

    def exceeded_max(self):
        return self.signedstudents_set.count() < self.term.termMaxStudents

    def student_not_signed(self, user):
        return self.signedstudents_set.filter(signedStudent__id=user.id) == []

    def sign_student(self, user):
        if not self.exceeded_max() or self.student_not_signed(user):
            self.signedstudents_set.create(signedStudent=user)

    def __str__(self):
        return "%s, %s/%s" % (str(self.term), str(self.signedstudents_set.count()), str(self.term.termMaxStudents))

    class Meta:
        verbose_name = _('termTime')
        verbose_name_plural = _('termTime|plural')


class SignedStudents(models.Model):
    signedStudent = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('student'))
    signedTermTime = models.ForeignKey(TermTime, on_delete=models.CASCADE, verbose_name=_('term'))

    def __str__(self):
        return "%s; %s: %s" % (str(self.signedTermTime), _('signedStudents'), str(self.signedStudent))

    class Meta:
        verbose_name = _('signedStudents')
        verbose_name_plural = _('signedStudents|plural')
