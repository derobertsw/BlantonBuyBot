# BlantonBuyBot

## Setup

Install Home Brew
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

Install Chrome
`brew install --cask google-chrome`

Install Selenium
`pip install -U selenium`

Install Chrome Driver
`brew tap homebrew/cask && brew cask install chromedriver`

## Add credentials
Create new file called env_variables.py in the root directory; enter the following into the file

`user_name: str = "PUT YOUR EMAIL ADDRESS HERE"`
`password: str = "PUT YOUR PASSWORD HERE"`

## Run
`python3 BlantonBot`
