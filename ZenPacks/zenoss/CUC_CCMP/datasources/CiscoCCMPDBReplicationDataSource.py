##############################################################################
#
# Copyright (C) Zenoss, Inc. 2008-2012, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

'''
A datasource type that uses Cisco's Serviceability API to retrieve
performance counters from a Cisco Unified Communications applications.
'''

import os

from zope.component import adapts
from zope.interface import implements

from AccessControl import ClassSecurityInfo

from Products.ZenModel.BasicDataSource import BasicDataSource
from Products.ZenModel.ZenossSecurity import ZEN_VIEW
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence

from Products.Zuul.form import schema
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.template import RRDDataSourceInfo
from Products.Zuul.interfaces import IRRDDataSourceInfo
from Products.Zuul.utils import ZuulMessageFactory as _t


class CiscoCCMPDBReplicationDataSource(ZenPackPersistence, BasicDataSource):
    ZENPACKID = 'ZenPacks.zenoss.CUC_CCMP'

    CISCOCCMPDBREPLICATION = 'CiscoCCMPDBReplication'

    sourcetypes = (CISCOCCMPDBREPLICATION,)
    sourcetype = CISCOCCMPDBREPLICATION

    timeout = 30
    eventClass = "/Status/CiscoCCMP"

    hostname = ""
    username = "${dev/zWinUser}"
    password = "${dev/zWinPassword}"

    _properties = BasicDataSource._properties + (
        {'id': 'hostname', 'type': 'string', 'mode': 'w'},
        {'id': 'username', 'type': 'string', 'mode': 'w'},
        {'id': 'password', 'type': 'string', 'mode': 'w'},
        )

    _relations = BasicDataSource._relations

    factory_type_information = ({
        'immediate_view': 'editCiscoCCMPDBReplication',
        'actions': ({
            'id': 'edit',
            'name': 'Data Source',
            'action': 'editCiscoCCMPDBReplication',
            'permissions': (ZEN_VIEW,),
            },)
        },)

    security = ClassSecurityInfo()

    def __init__(self, id, title=None, buildRelations=True):
        BasicDataSource.__init__(self, id, title, buildRelations)

    def useZenCommand(self):
        return True

    def getCommand(self, context):
        parts = ['check_db_replication.py']
        parts.append('-H %s' % context.manageIp)

        if self.username:
            parts.append("-u '%s'" % self.username)

        if self.password:
            parts.append("-w '%s'" % self.password)

        cmd = ' '.join(parts)
        cmd = BasicDataSource.getCommand(self, context, cmd)
        return cmd

    def checkCommandPrefix(self, context, cmd):
        if self.usessh:
            return os.path.join(context.zCommandPath, cmd)
        zp = self.getZenPack(context)
        return zp.path('libexec', cmd)


class ICiscoCCMPDBReplicationDataSourceInfo(IRRDDataSourceInfo):
    timeout = schema.Int(title=_t(u"Timeout (seconds)"))
    cycletime = schema.Int(title=_t(u'Cycle Time (seconds)'))


class CiscoCCMPDBReplicationDataSourceInfo(RRDDataSourceInfo):
    implements(ICiscoCCMPDBReplicationDataSourceInfo)
    adapts(CiscoCCMPDBReplicationDataSource)

    timeout = ProxyProperty('timeout')
    cycletime = ProxyProperty('cycletime')
