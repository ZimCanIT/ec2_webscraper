# ec2_webscraper
A web scraping application that runs on an EC2 machine to iteratively delete friend requests on a social networking site.
Social networking site has a limit of 900 requests. Script iteratively deletes requests. 


# Usage
Launch AWS EC2 instance with an SSH key and aupload `userdata.sh` file from within this repo into the userdata field

Script will launch with code running in the background and makes an api call

Push credentials to AWS parameter store
*`aws ssm put-parameter --name "ppwpuname" --type "String" --value [youSecretUsername]`
*`aws ssm put-parameter --name "ppwpwd" --type "String" --value [yourSecretPassword]`

Python file `param_store.py` uses boto3 module to make api calls from paramater store and parses in credentials to the web scrapiong script: `app.py`

EC2 instance hosting code require an IAM profile in order to have access to SSM.

Video of how web scraper works locally:
