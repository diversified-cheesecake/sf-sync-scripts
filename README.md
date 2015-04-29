Salesforce Scripts
=================
For syncing *VAN* records into *Salesforce*. 

To use, create a file `sf_credentials.py` in the directory, and put in your credentials as such:

``` python
username='your_salesforce_account'
password='your_salesforce_password'
security_token='Salesforce_security_token'
```

If you don't have a security token please [regenerate your password](https://login.salesforce.com/secur/forgotpassword.jsp?locale=us), and you will be granted a security token. Save this in a secure place.