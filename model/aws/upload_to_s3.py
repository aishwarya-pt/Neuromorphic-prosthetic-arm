import boto3

def upload_to_s3(file_name, bucket, object_name=None):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_name, bucket, object_name or file_name)
        print(f"Uploaded {file_name} to {bucket}")
    except Exception as e:
        print("Upload failed:", e)
