import boto3

def create_bucket(bucket_name):
  client = boto3.client('s3')
  client.create_bucket(Bucket=bucket_name)
  index_file_name = "index.html"
  error_file_name = "error.html"
  data = open(index_file_name, 'rb')
  s3 = boto3.resource('s3')
  s3.Bucket(bucket_name).put_object(Key=index_file_name, Body=data, ContentType='text/html')
  data = open(error_file_name, 'rb')
  s3.Bucket(bucket_name).put_object(Key=error_file_name, Body=data, ContentType='text/html')
  make_bucket_public_readable(bucket_name)
  client.put_bucket_website(Bucket=bucket_name,
    WebsiteConfiguration={
        'ErrorDocument': {
            'Key': error_file_name
        },
        'IndexDocument': {
            'Suffix': index_file_name
        }
    }
  )
  print("{} Created. Check {}.s3-website-us-east-1.amazonaws.com".format(bucket_name, bucket_name))

def make_bucket_public_readable(bucket_name):
  bucket_policy = boto3.resource('s3').BucketPolicy(bucket_name)
  policy_string = '{{\
    "Version":"2012-10-17",\
    "Statement":[{{\
      "Sid":"PublicReadGetObject",\
      "Effect":"Allow",\
      "Principal": "*",\
      "Action":["s3:GetObject"],\
      "Resource":["arn:aws:s3:::{}/*"]\
      }}]\
  }}'.format(bucket_name)
  response = bucket_policy.put(Policy=policy_string)
    

bucket_name = input('Enter bucket name: ')
create_bucket(bucket_name)
