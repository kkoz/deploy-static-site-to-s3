# Create S3 Web Server

This is a script to create a static web server hosted in an S3 bucket.
Currently it simply uploads an index.html and error.html file, which are the only ones required by the API.

## How to run

First you must get the aws cli (https://docs.aws.amazon.com/cli/latest/userguide/installing.html)
Then, you must log in to your AWS account and create a user with privileges to create buckets and put objects. Create an access key/secret key for this user.
Then, run 
```
aws configure
```
 and provide the access key and secret key created above.

Then, install Pipenv if you haven't.
run
```
pipenv install
```
Followed by
```
pipenv shell
python test.py
```


