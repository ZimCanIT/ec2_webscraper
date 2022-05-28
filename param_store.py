#!/usr/bin/env python3 

# https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-parameter.html
# https://blair55.github.io/blog/aws-parameter-store-scripting/

import boto3

ssm_client = boto3.client("ssm", region_name="us-east-1")

def get_email():          
    email = ssm_client.get_parameter(Name='ppwuname')
    return email["Parameter"]["Value"]

def get_password():
    pwd = ssm_client.get_parameter(Name='ppwpwd')
    return pwd["Parameter"]["Value"]




