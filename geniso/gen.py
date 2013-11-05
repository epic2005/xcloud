#!/usr/bin/env python
from pykickstart.parser import *
from pykickstart.version import makeVersion

ksfname = 'ks.cfg'
ksfile = 'out.cfg'

ksparser = KickstartParser(makeVersion()) 
ksparser.readKickstart(ksfname)

kshandlers = ksparser.handler

kshandlers.selinux.selinux = 0
kshandlers.firewall.enabled = 0

outfile = open(ksfile,'w')
outfile.write(kshandlers.__str__())
outfile.close()
