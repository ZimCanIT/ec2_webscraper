# install python 3.7 : https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-linux.html 
sudo yum update -y # update upstream package repositories 
sudo yum install git -y


# installling google chrome for amazon linux 
# https://help.looker.com/hc/en-us/articles/360035411973-Installing-Chromium-for-Amazon-Linux
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
sudo yum install ./google-chrome-stable_current_x86_64.rpm -y
sudo ln -s /usr/bin/google-chrome-stable /usr/bin/chromium


python3 -m venv websScrapingProd/env
source ~/websScrapingProd/env/bin/activate
cd websScrapingProd
python3 -m pip install --upgrade pip


# install modules for scrpit
pip install webdriver-manager
pip install selenium
pip install boto3 

git clone https://github.com/ZimCanIT/ec2_webscraper.git  

# change into the directory containing code and run user_data.sh 
cd ec2_webscraper 
python app.py 

