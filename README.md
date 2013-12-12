This project generates the vagrant dummy boxes to run with 
[vagrant-cloudstack](https://github.com/klarna/vagrant-cloudstack)

## Run

To run the script, first check your configuration in config.py

Then execute

    python make-boxes.py

You should get an output like:

    exoscale-boxes/Linux-CentOS-6.4-64-bit-10GB-Disk.box generated OK
    exoscale-boxes/Linux-CentOS-6.4-64-bit-50GB-Disk.box generated OK
    exoscale-boxes/Linux-Ubuntu-12.04-LTS-64-bit-10GB-Disk.box generated OK
    exoscale-boxes/Linux-Ubuntu-12.04-LTS-64-bit-50GB-Disk.box generated OK
    exoscale-boxes/Linux-Ubuntu-12.04-LTS-64-bit-100GB-Disk.box generated OK
    exoscale-boxes/Linux-CentOS-6.4-64-bit-100GB-Disk.box generated OK
    exoscale-boxes/Linux-Ubuntu-12.04-LTS-64-bit-200GB-Disk.box generated OK
    exoscale-boxes/Linux-Ubuntu-12.04-LTS-64-bit-400GB-Disk.box generated OK
    exoscale-boxes/Linux-CentOS-6.4-64-bit-200GB-Disk.box generated OK
    exoscale-boxes/Linux-CentOS-6.4-64-bit-400GB-Disk.box generated OK
    exoscale-boxes/Windows-Server-2012-Disk-200GB.box generated OK
    exoscale-boxes/Windows-Server-2012-Disk-50GB.box generated OK
    exoscale-boxes/Windows-Server-2012-Disk-100GB.box generated OK
    exoscale-boxes/Windows-Server-2012-Disk-400GB.box generated OK
    exoscale-boxes/Windows-Server-2008-R2-SP1-50GB-Disk.box generated OK
    exoscale-boxes/Windows-Server-2008-R2-SP1-100GB-Disk.box generated OK
    exoscale-boxes/Windows-Server-2008-R2-SP1-200GB-Disk.box generated OK
    exoscale-boxes/Windows-Server-2008-R2-SP1-400GB-Disk.box generated OK
    exoscale-boxes/Linux-Ubuntu-13.10-64-bit-10-GB-Disk.box generated OK
    exoscale-boxes/Linux-Ubuntu-13.10-64-bit-50-GB-Disk.box generated OK
    exoscale-boxes/Linux-Ubuntu-13.10-64-bit-100-GB-Disk.box generated OK
    exoscale-boxes/Linux-Ubuntu-13.10-64-bit-200-GB-Disk.box generated OK
    exoscale-boxes/Linux-Ubuntu-13.10-64-bit-400-GB-Disk.box generated OK
    exoscale-boxes/Windows-Server-2012-R2-Disk-50GB.box generated OK
    exoscale-boxes/Windows-Server-2012-R2-Disk-100GB.box generated OK
    exoscale-boxes/Windows-Server-2012-R2-Disk-200GB.box generated OK
    exoscale-boxes/Windows-Server-2012-R2-Disk-400GB.box generated OK
    exoscale-boxes/Linux-Debian-7-64-bit-Disk-10GB.box generated OK
    exoscale-boxes/Linux-Debian-7-64-bit-Disk-50GB.box generated OK
    exoscale-boxes/Linux-Debian-7-64-bit-Disk-100GB.box generated OK
    exoscale-boxes/Linux-Debian-7-64-bit-Disk-200GB.box generated OK
    exoscale-boxes/Linux-Debian-7-64-bit-Disk-400GB.box generated OK

## Boxes usage

To use the boxes you need to have a valid Vagrant installation (>1.4)
and the vagrant-cloudstack plugin.

Add the box(es) you require to your confguration:

    vagrant box add Linux-Ubuntu-13.10-64-bit-50-GB-Disk /path/or/url/to/boxes/Linux-Ubuntu-13.10-64-bit-50-GB-Disk.box

Then generate a Vagrantfile like this one

    Vagrant.configure("2") do |config|
        config.vm.box = "Linux-Ubuntu-13.10-64-bit-50-GB-Disk"
        config.ssh.username = "root"
        config.ssh.private_key_path = "/Users/vagrant/.ssh/id_rsa.vagrant"

        config.vm.provider :cloudstack do |cloudstack, override|
            cloudstack.api_key = "AAAAAAAAAAAAAAAA-aaaaaaaaaaa"
            cloudstack.secret_key = "SSSSSSSSSSSSSSSS-ssssssssss"

            cloudstack.security_group_ids = [ "fc4a3d81-b0c9-4e27-9bd8-5b04b51be100", "ee9e08b0-2a30-469e-af9b-d06a70184f9e" ] # List of on or more SG your machine will be tied to. Can be omitted, then the default SG will be used
            cloudstack.keypair = "vagrant" # for SSH boxes the name of the public key pushed to the machine
        end
    end
   
Finally fire up the instance:

    vagrant up --provider=cloudstack

### Notes

* Windows boxes require to WinRM enabled in order to be bootstraped correctly by vagrant.

