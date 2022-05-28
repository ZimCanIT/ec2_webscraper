# install python 3.7 : https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-linux.html 
sudo yum update -y # update upstream package repositories 
sudo yum install python37 -y

# install pip and python modules for scrpit
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
pip install webdriver-manager
pip install selenium
pip install boto3 

# installling google chrome for amazon linux: https://help.looker.com/hc/en-us/articles/360035411973-Installing-Chromium-for-Amazon-Linux
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
sudo yum install ./google-chrome-stable_current_x86_64.rpm -y
sudo ln -s /usr/bin/google-chrome-stable /usr/bin/chromium


# install git and clone code repo (edit code such that the username and password field read the ppw credentials as system variables)
sudo yum install git -y
git clone https://github.com/ZimCanIT/ec2_webscraper.git # need code in repo that uses boto3 mod to read credentials for signing into the site 

# change into the directory containing code
cd ec2_webscraper 
python 3.7 app.py # app needs to have an explicit wait defined 

