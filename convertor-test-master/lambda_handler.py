import os
from docx2pdf import convert
import boto3
import subprocess
import tempfile

def lambda_handler(event, context):
    try:
        # TODO: Accept docx file content from 
        s3 = boto3.client('s3')

        bucket = 'unisys-bucket'
        object_name = 'input.docx'
        
        temp_dir = tempfile.TemporaryDirectory()
        temp_dir_path = temp_dir.name

        # Download the Word doc file from S3.
        s3.download_file(bucket, object_name, f'/{temp_dir_path}/input.docx')

        
        # convert("/tmp/input.docx", "/tmp/output.pdf")
        subprocess.run(
            f"/opt/libreoffice7.6/program/soffice --headless --convert-to pdf {temp_dir_path}/input.docx --outdir {temp_dir_path}",
            shell=True,
            check=True,
            # libreoffice needs to create a dir called .cache/dconf in the HOME dir.
            # So HOME  must be writable. But on aws lambda, the default HOME is read-only.
            env={"HOME": temp_dir_path},
        )
        s3.upload_file(f'{temp_dir_path}/output.pdf', bucket, 'output.pdf')
        
        status = "success"

    except Exception as error:
        status = "failure"
        print("An error occurred ", error)
        return {
            'status': status
        }

