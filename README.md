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

            # Uncomment ONE of the following service offerings:
            #cloudstack.service_offering_id = "71004023-bb72-4a97-b1e9-bc66dfce9470" # Micro - 512 MB
            #cloudstack.service_offering_id = "b6cd1ff5-3a2f-4e9d-a4d1-8988c1191fe8" # Tiny - 1GB
            #cloudstack.service_offering_id = "21624abb-764e-4def-81d7-9fc54b5957fb" # Small - 2GB
            cloudstack.service_offering_id = "b6e9d1e8-89fc-4db3-aaa4-9b4c5b1d0844" # Medium - 4GB
            #cloudstack.service_offering_id = "c6f99499-7f59-4138-9427-a09db13af2bc" # Large - 8GB
            #cloudstack.service_offering_id = "350dc5ea-fe6d-42ba-b6c0-efb8b75617ad" # Extra-large - 16GB
            #cloudstack.service_offering_id = "a216b0d1-370f-4e21-a0eb-3dfc6302b564" # Huge - 32GB

            cloudstack.security_group_ids = [ "fc4a3d81-b0c9-4e27-9bd8-5b04b51be100", "ee9e08b0-2a30-469e-af9b-d06a70184f9e" ] # List of on or more SG your machine will be tied to. Can be omitted, then the default SG will be used
            cloudstack.keypair = "vagrant" # for SSH boxes the name of the public key pushed to the machine
        end
    end
   
Finally fire up the instance:

    vagrant up --provider=cloudstack

### Notes

* Prior to launch a linux box, make sure the Security group allows for incoming SSH (TCP 22) trafic from your IP address
* Windows boxes require to WinRM enabled in order to be bootstraped correctly by vagrant.

