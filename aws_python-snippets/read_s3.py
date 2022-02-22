import json
import urllib.parse
import boto3
import botocore
import codecs
import os
print('first Loading function')

s3 = boto3.client('s3')
# s3 = boto3.resource('s3')

bucket_name = os.getenv("bucket_name", "")


def lambda_handler(event, context):

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    print(bucket)
    # Iterates through all the objects, doing the pagination for you. Each obj
    # is an ObjectSummary, so it doesn't contain the body. You'll need to call
    # get to get the whole body.
    for obj in bucket.objects.all():
        key = obj.key
        print(key)
        body = obj.get()['Body'].read()
        print(body)

    return body
