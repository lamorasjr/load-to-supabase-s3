import os
import boto3

# Creation of the AWS client connection
s3_client = boto3.client(
    service_name = "s3",
    endpoint_url = os.getenv("SUPABASE_S3_ENDPOINT"),
    region_name = os.getenv("SUPABASE_S3_REGION"),
    aws_access_key_id = os.getenv("SUPABASE_S3_ACCESS_KEY"),
    aws_secret_access_key = os.getenv("SUPABASE_S3_SECRET_KEY") 
)

# Upload a file into a s3 bucket
input_path = os.getcwd() + "/data"
dir_list = os.listdir(input_path)
s3_bucket = os.getenv("SUPABASE_S3_BUCKET")

for file_name in dir_list:
    s3_client.upload_file(
        f"{input_path}/{file_name}",
        s3_bucket,
        "raw_" + file_name
    )


print(f"Load to Supabase s3: '{s3_bucket}' has been successfuly completed.")

