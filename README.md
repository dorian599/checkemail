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
      curl 10.20.30.40/mailAddress@domain.com
````

***checkemail demon***

````shell
      /etc/init.d/checkemail {start|stop|restart|status}
````

**JSON Responses**

***When the email is valid an exists***

````shell
      {'success': 'Email Exists', 'error':'', 'data':''}
````

***When the email does not exists***

````shell
      {'success': '', 'error':'Invalid Email', 'data':''}
````

***When the email domain does not has MX servers***

````shell
      {'success': '', 'error':'No SMTP server for this domain', 'data':''}
````

***When the email is invalid***

````shell
      {'success': '', 'error':'Invalid Email Format', 'data':''}
````
