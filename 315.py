import boto3

# Hard-coded AWS credentials (not recommended for production)
AWS_ACCESS_KEY = 'your_access_key_here'
AWS_SECRET_ACCESS_KEY = 'your_secret_access_key_here'

# Create an S3 client using the hard-coded credentials
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name='us-east-1'  # specify your desired AWS region
)

# Print the access keys to the console (for debugging purposes)
print("AWS Access Key ID:", AWS_ACCESS_KEY)
print("AWS Secret Access Key:", AWS_SECRET_ACCESS_KEY)

# Example usage
# To list buckets (replace with actual use case)
try:
    response = s3_client.list_buckets()
    print("S3 Buckets:", [bucket['Name'] for bucket in response['Buckets']])
except Exception as e:
    print("Error listing buckets:", e)