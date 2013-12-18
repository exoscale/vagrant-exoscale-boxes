import tarfile
import json
import re
from cStringIO import StringIO
import requester
import config

def listtemplates():
    response, error = requester.make_request('listTemplates',{"templatefilter": 'executable'},None,config.host,config.port,config.apikey,config.secretkey,config.protocol,config.path)
    resp=json.loads(str(response))
    return resp['listtemplatesresponse']

metadata = """{
    "provider": "cloudstack"
}
"""

vagrantfile = """# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.provider :cloudstack do |cloudstack, override|
    cloudstack.host = "{0}"
    cloudstack.path = "{1}"
    cloudstack.port = "{2}"
    cloudstack.scheme = "{3}"
    cloudstack.template_id = "{4}"
    cloudstack.network_id = "{5}"
    cloudstack.zone_id = "{6}"
    cloudstack.network_type = "Basic"
  end
end"""

templates = listtemplates()

for t in templates['template']:
    templateName = "exoscale-boxes/" +  re.sub(r"\s+", '-', t['displaytext']) + ".box"
    out = tarfile.open(templateName, mode='w:gz')
    try:
        info = tarfile.TarInfo('metadata.json')
        info.size = len(metadata)
        out.addfile(info, StringIO(metadata))
        info = tarfile.TarInfo('Vagrantfile')
        info.size = len(vagrantfile.format(config.host, config.path, config.port, config.protocol,t['id'],config.network, config.zone))
        out.addfile(info, StringIO(vagrantfile.format(config.host, config.path, config.port, config.protocol,t['id'],config.network, config.zone)))
    finally:
        out.close()
        print templateName + " generated OK"

