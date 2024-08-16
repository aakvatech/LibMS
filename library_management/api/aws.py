import io
import boto3
import base64
import frappe
from frappe.utils.password import get_decrypted_password
from botocore.exceptions import NoCredentialsError, ClientError


class s3Client:
    def __init__(self):
        self.setting_doc = frappe.get_cached_doc("Library Setting", "Library Setting")
        self.access_key = self.setting_doc.get_password("access_key")
        self.secret_key = self.setting_doc.get_password("secret_key")
        self.bucket_name = self.setting_doc.aws_bucket_name
        self.region_name = self.setting_doc.aws_region_name
        self.folder_name = self.setting_doc.folder_name

        if not self.access_key or not self.secret_key:
            frappe.throw("AWS credentials not available, Please set it on Library Setting")

        if not self.bucket_name:
            frappe.throw("AWS bucket name not available, Please set it on Library Setting")
        
        if not self.region_name:
            frappe.throw("AWS region name not available, Please set it on Library Setting")

        try:
            self.s3_client = boto3.client(
                "s3",
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key,
                region_name=self.region_name,
            )
        
        except NoCredentialsError as e:
            frappe.throw(msg=str(e), title="NoCredentialsError")
        except ClientError as e:
            frappe.throw(msg=str(e), title="ClientError")
        except Exception as e:
            frappe.throw(msg=str(e), title="Error")
    

    def generate_presigned_url(self, aws_key):
        try:
            presigned_url = self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket_name, 'Key': aws_key},
                ExpiresIn=20
            )
            return presigned_url
        
        except NoCredentialsError:
            frappe.throw("AWS credentials not available, Please set it on Library Setting", title="NoCredentialsError")
        except ClientError as e:
            frappe.throw(msg=str(e), title="ClientError")
        except Exception as e:
            frappe.throw(msg=str(e), title="Error")
    
    def upload_file(self, file, filename):
        try:
            if self.folder_name:
                filename = f"{self.folder_name}/{filename}"

            self.s3_client.upload_fileobj(
                Fileobj=file,
                Bucket=self.bucket_name,
                Key=filename
            )
            return filename
        
        except NoCredentialsError:
            frappe.throw("AWS credentials not available, Please set it on Library Setting", title="NoCredentialsError")
        except ClientError as e:
            frappe.throw(msg=str(e), title="ClientError")
        except Exception as e:
            frappe.throw(msg=str(e), title="Error")
    

@frappe.whitelist()
def get_book_from_aws(aws_key):
    if not aws_key:
        frappe.throw("AWS Book key not available")
    
    s3 = s3Client()
    presigned_url = s3.generate_presigned_url(aws_key)
    return presigned_url


@frappe.whitelist()
def upload_book_file_to_aws(filedata, filename):

    if not filedata:
        frappe.throw("File not available, attach a file to upload")
    
    file_bytes = base64.b64decode(filedata)
    file = io.BytesIO(file_bytes)

    s3 = s3Client()
    filename = s3.upload_file(file, filename)
    return filename