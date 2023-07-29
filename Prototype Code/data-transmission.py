from google.cloud import storage

# Create a client to access the Google Cloud Storage
client = storage.Client()

# Define the bucket and file name for data storage
bucket_name = "smart-home-data"
file_name = "motion_sensor_data.txt"

# Function to upload data to the cloud
def upload_to_cloud(data):
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_string(data)

# Sample data to be uploaded (replace this with actual sensor data)
sample_data = "Timestamp: 2023-08-15 12:00:00, Motion: Detected\n"

# Call the function to upload data to the cloud
upload_to_cloud(sample_data)