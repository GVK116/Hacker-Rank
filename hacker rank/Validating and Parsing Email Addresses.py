import re
import email.utils as email

def valid_email(email_string):
    name,mail_id = email_string.split()
    if re.search(r'[<][a-z][_\-\.]+[@]+[a-z]{1,3}[>]',mail_id):
        return 'true'
    else:
        return 'false'

for _ in range(int(input())):
    output = valid_email(input())
    print(output)