# updgrading yum packages and installing git
sudo yum update -y 
sudo yum install git -y

# installling google chrome for amazon linux 
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
sudo yum install ./google-chrome-stable_current_x86_64.rpm -y
sudo ln -s /usr/bin/google-chrome-stable /usr/bin/chromium

# upgrading pip and installing modules
python3 -m pip install --upgrade pip
pip install webdriver-manager
pip install selenium
pip install boto3 

# clone github repo and launch application 
git clone https://github.com/ZimCanIT/ec2_webscraper.git  
cd ec2_webscraper 
python3 app.py 
