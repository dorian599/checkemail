Check if an email address is valid
-----------------------------------------------

***Dependencies***

````shell
      yum install -y python-pip
      pip install validate_email
      pip install pyDNS
````

***Installation***

````shell
      git clone https://github.com/dorian599/checkemail.git
      cd checkemail
      sh install.sh
````

***Try it***

````shell
      curl 10.20.30.40/correo@dominio.com
````

***checkemail demon***

````shell
      /etc/init.d/checkemail {start|stop|restart|status}
````
