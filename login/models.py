# -*- coding:utf-8 -*-
from django.db import models
from .managers import ProjectInfoManager,ModuleInfoManager


class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']
        verbose_name = "用户"
        verbose_name_plural = "用户"


class ProjectInfo(models.Model):
    class Meta:
        verbose_name = "项目信息"
        db_table = 'Project_Info'

    project_name = models.CharField('项目名称', max_length=50, unique=True, null=False)
    responsible_name = models.CharField('项目负责人', max_length=20, null=False)
    test_user = models.CharField('测试人员', max_length=20, null=False)
    dev_user = models.CharField('开发人员', max_length=20, null=False)
    req_user = models.CharField('需求人员', max_length=20)
    simple_desc = models.CharField('简介', max_length=200)
    objects = ProjectInfoManager()


class ModuleInfo(models.Model):
    class Meta:
        verbose_name = "模块信息"
        db_table = 'Module_info'

    module_name = models.CharField('模块名称', max_length=150, unique=True, null=False)
    belong_project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    test_user = models.CharField('测试人员', max_length=20)
    simple_desc = models.CharField('简介', max_length=200)
    objects = ModuleInfoManager()