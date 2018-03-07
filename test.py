import boto3

def create_bucket(site_name):
  client = boto3.client('s3')
  bucket_name = site_name+ ".test.foridaho.org"
  client.create_bucket(ACL='public-read', Bucket=bucket_name)
  resource = boto3.resource('s3')
  index_file_name = "index.html"
  error_file_name = "error.html"
  resource.meta.client.upload_file('./index.html', bucket_name, index_file_name)
  resource.meta.client.upload_file('./error.html', bucket_name, error_file_name)
  response = make_file_public_read(bucket_name, index_file_name)
  response = make_file_public_read(bucket_name, error_file_name)
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

def make_file_public_read(bucket_name, key):
  object_acl = s3.ObjectAcl(bucket_name, )
  return object_acl.put(ACL='public-read')

def get_buckets():
  s3 = boto3.client('s3')
  response = s3.list_buckets()
  buckets = [bucket['Name'] for bucket in response['Buckets']]
  print("Bucket List: %s" % buckets)

get_buckets()
create_bucket("test2")
