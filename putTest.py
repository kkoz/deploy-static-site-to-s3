import boto3

def attempt_put():
    data = open('index.html', 'rb')
    s3 = boto3.resource('s3')
    s3.Bucket('test1.test.foridaho.org').put_object(Key='putTest.html', Body=data)

attempt_put()
