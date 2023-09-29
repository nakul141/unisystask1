import os
import boto3
import subprocess

def lambda_handler(event, context):
    try:
        # TODO: Accept docx file binary content from request context

        s3 = boto3.client('s3')

        bucket = 'unisys-bucket'
        object_name = 'input.docx'

        # Download the Word doc file from S3.
        s3.download_file(bucket, object_name, '/tmp/input.docx')
        os.chdir('/tmp')
        subprocess.run(
            f"libreoffice7.5 --headless --invisible --nodefault --view --nolockcheck --nologo --norestore --convert-to pdf --outdir /tmp /tmp/input.docx",
            shell=True,
            check=True,
            stderr=subprocess.STDOUT
        )
        s3.upload_file(f'/tmp/input.pdf', bucket, 'input.pdf')
        status = "success"
    except Exception as error:
        status = "failure"
        print("An error occurred ", error)

    return {
        'status':status
        }