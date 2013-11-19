#!/usr/bin/env python
##############################################################################
#
# Copyright (C) Zenoss, Inc. 2008-2012, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

import sys
import subprocess

from optparse import OptionParser

class ZenossCCMPPlugin:
    def __init__(self, host, user, passwd):
        self.host = host
        self.user = user
        self.passwd = passwd

    def run(self):
    	command = "$ZENHOME/bin/winexe -U \'%s%%%s\' //%s \'cmd /c \"C:\ZenossAlter\ccmpAlertBatch.bat\"\'" %(self.user, self.passwd, self.host)
    	#print command
        #command_out = os.system(command)
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (command_out, err) = proc.communicate()
        #print command_out
        output_lines = str(command_out).split("\n")
        print "STATUS OK|DBReplication=%s" %(output_lines[2])


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option(
        "-H", "--host", dest="host",
        help="Hostname/IP of CCMP server")

    parser.add_option(
        "-u", "--user", dest="user",
        help="Username")

    parser.add_option(
        "-w", "--password", dest="password",
        help="Password")

    options, args = parser.parse_args()

    if not options.host:
        print "You must specify the host parameter."
        sys.exit(3)

    if not options.user:
        print "You must specify the user parameter."
        sys.exit(3)

    if not options.password:
        print "You must specify the password parameter."
        sys.exit(3)

    cmd = ZenossCCMPPlugin(
        options.host, options.user, options.password)

    cmd.run()
