# -*- coding: utf-8 -*-
# Create your models here.
from django.db import models
from common.common import run_cmd


class MysqlAccounts(models.Model):
    # __tablename__ = 'mysql_account'
    loginUser = models.CharField(u'认证用户名', max_length=100, default='dbmanager')
    loginPassword = models.CharField(u'认证用户密码', max_length=255,
                                     default='15cac1c0748acf5d0783d7c2f19aa6ab17ee7129f1a7e25724c1def36911f3e4')
    name = models.CharField(u'用户名', max_length=100)
    password = models.CharField(u'密码', max_length=255)
    host = models.CharField(u'授权数据库IP', max_length=100)
    priv = models.CharField(u'权限', max_length=200)
    remoteHost = models.CharField(u'来源IP', max_length=100)
    database = models.CharField(u'数据库名', max_length=100)
    tableName = models.CharField(u'表名', max_length=100)

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.host, self.remoteHost)
