#!/usr/bin/env python3 

import boto3

ssm_client = boto3.client("ssm", region_name="us-east-1")

def get_email():          
    email = ssm_client.get_parameter(Name='ppwuname')
    return email["Parameter"]["Value"]

def get_password():
    pwd = ssm_client.get_parameter(Name='ppwpwd')
    return pwd["Parameter"]["Value"]




