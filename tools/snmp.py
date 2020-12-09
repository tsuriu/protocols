from easysnmp import Session
import binascii

class snmp:

    Sys = {
            'SysUptime':'.1.3.6.1.2.1.1.3.0',
            'SysName':'.1.3.6.1.2.1.1.5.0',
            'SysDescr':'.1.3.6.1.2.1.1.1.0',
            'SysObjectID':'.1.3.6.1.2.1.1.2.0'
          }

    SysDT = {}

    def __init__(self,host,snmpword,ver):
        self.host = host
        self.snmpword = snmpword
        self.ver = ver
        self.session = Session(hostname=self.host, community=self.snmpword, version=self.ver)

        for key in list(self.Sys.keys()):
            oid_base = self.Sys[key]
            dt_base = self.Get(oid_base)

            self.SysDT.update({key:dt_base['value']})

    def parsedt(self,dt):
        if dt.oid_index == '':
            index0 = (dt.oid).split('.')
            index = index0[-1]
            if index == '1':
                index = index0[-2]
        else:
            index = dt.oid_index

        dt_index = index

        pdt = {
                'oid':dt.oid,
                'oidx':dt_index,
                'type':dt.snmp_type,
                'value':dt.value
              }        
        return pdt

    def Walk(self,oid):
        walk_data = {}
        s = self.session
        wdt = s.walk(oid)
        for dt in wdt:
            widx = wdt.index(dt)
            dct = self.parsedt(dt)
            walk_data.update({str(widx):dct})
        return walk_data
        
    def Get(self,oid):
        s = self.session
        while True:
            dt = s.get(oid)
            if dt.value != 'NOSUCHINSTANCE':
                break

        get_data = self.parsedt(dt)
        return get_data