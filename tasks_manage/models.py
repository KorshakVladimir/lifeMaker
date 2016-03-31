from __future__ import unicode_literals

from django.db import models


class Task(models.Model):
    parent_task = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_create = models.TimeField(auto_now=True)
    date_execute = models.TimeField(null=True, blank=True)
    date_plan_execute = models.TimeField(null=True, blank=True)
    priority = models.IntegerField(blank=True, default = 0)
    STATUS = (
        ('done', 'Done'),
        ('Start', 'Start'),
    )
    satus = models.CharField(max_length=100, choices = STATUS)

    @classmethod
    def get_done_status(cls):
        return 'done'

    def __unicode__(self):
        return "%d %s" % (self.id, self.title)


class File_storage(models.Model):
    name = models.FileField()
    task = models.ForeignKey(Task, null=True, blank=True)

