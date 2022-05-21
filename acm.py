import boto3
import time

session = boto3.session.Session(profile_name = "terraform", region_name='us-east-1')
client = session.client('acm')

responce =client.list_certificates(
    CertificateStatuses=[
        'PENDING_VALIDATION','ISSUED','INACTIVE','EXPIRED','VALIDATION_TIMED_OUT','REVOKED','FAILED',
    ]
   
)

# print(type(responce))
for key in responce:
    print(responce[key][CertificateArn])


# responce1 = client.describe_certificate(
#     CertificateArn='arn:aws:acm:us-east-1:057324157993:certificate/25e6393b-14ed-4c08-aef8-37bd9d84481c'
# )
# print("--------------------------------------------------")
# print(responce1)