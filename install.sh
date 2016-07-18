#!/bin/sh

yum install -y wget git

yum install -y python-pip
pip install validate_email
pip install pyDNS

cd ..

cp -r chekemail /opt/chekemail

cp /opt/chekemail/checkemail /etc/init.d/checkemail

chmod +x /etc/init.d/checkemail

chkconfig /etc/init.d/checkemail on

/etc/init.d/checkemail start
