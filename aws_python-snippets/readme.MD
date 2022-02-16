## Python AWS Snippets

## `get_secret_secmgr.py`-  This snippet is used to get secret from the aws secret manager in the secure string format and further converting the secure string into dictionary & fetch the user name and password.
 1. `parameters`:   
    a. `secret_name` = "arn of the secret manager"
    b. `region_name` = "region of the secret manager"