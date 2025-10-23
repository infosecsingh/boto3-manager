import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name, region='ap-south-1'):

    try:
        if region == 'us-east-1':
            s3_client = boto3.client('s3', region_name=region)
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"✅ Bucket '{bucket_name}' created successfully in {region}")
    except ClientError as e:
        print(f"❌ Error creating bucket: {e}")
