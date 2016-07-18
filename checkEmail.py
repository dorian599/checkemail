#!/usr/bin/python

## yum install -y python-pip
## pip install validate_email
## pip install pyDNS

import sys
import json
import re
from validate_email import validate_email

# Checke if email is valid
def chechValidEmail(email):
    is_valid = validate_email(email,verify=True)
    return is_valid

## chec SMTP servers
def chechValidSMTP(email):
    is_valid = validate_email(email,check_mx=True)
    return is_valid

# check if the email format id good
def validateEmailFormat(email):

    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
        else:
            return False

# put all together
def checkEmailExists(email):

    if validateEmailFormat(email):
        if chechValidSMTP(email):
            if chechValidEmail(email):
                return json.dumps({'success': 'Email Exists', 'error':'', 'data':''})
            else:
                return json.dumps({'success': '', 'error':'Invalid Email', 'data':''})
        else:
            return json.dumps({'success': '', 'error':'No SMTP server for this domain', 'data':''})
    else:
        return json.dumps({'success': '', 'error':'Invalid Email Format', 'data':''})
