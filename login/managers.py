# -*- coding:utf-8 -*-
__author__ = 'sxm34916'

from django.db import models


class ProjectInfoManager(models.Manager):
    def update_project(self, id, **kwargs):
        obj = self.get(id=id)
        obj.project_name = kwargs.get('project_name')
        obj.responsible_name = kwargs.get('responsible_name')
        obj.test_user = kwargs.get('test_user')
        obj.dev_user = kwargs.get('dev_user')
        obj.req_user = kwargs.get('req_user')
        obj.simple_desc = kwargs.get('simple_desc')
        obj.save()


class ModuleInfoManager(models.Manager):
    def update_module(self, id, **kwargs):
        obj = self.get(id=id)
        obj.module_name = kwargs.get('module_name')
        obj.test_user = kwargs.get('test_user')
        obj.simple_desc = kwargs.get('simple_desc')
        obj.save()