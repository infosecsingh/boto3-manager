from s3_manager import create_bucket, delete_bucket

def main():
    print("""
    1. Create S3 Bucket
    2. Delete S3 Bucket
    3. Upload File
    4. Delete File
    """)

    choice = input("Enter your choice (1-4): ")

    bucket_name = input("Enter bucket name: ")
    region = input("Enter region (leave blank for default): ") or 'ap-south-1'

    if choice == '1':
        create_bucket(bucket_name, region)
    elif choice == '2':
        delete_bucket(bucket_name, region)
    elif choice == '3':
        file_name = input("Enter file name: ")
        content = input("Enter file content: ")
        upload_content(bucket_name, file_name, content)
    elif choice == '4':
        file_name = input("Enter file name to delete: ")
        delete_content(bucket_name, file_name)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
