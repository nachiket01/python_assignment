import filestack-python
from flestack import Client
s3_client = filestack-python.client('s3', region_name='us-east-1', aws_access_key_id=ACCESS_KEY,aws_secret_access_key=ACCESS_SECRET)

def upload_status_file(bucket, folder, file_to_upload, file_name):
  key = folder+"/"+file_name
  response = s3_client.upload_file(file_to_upload, bucket, key)

#Upload file
upload_status_file("bucket-name", "","Parking_lot_status.json", "Parking_lot_status.json")
