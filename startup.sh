#!/bin/bash
# bash script to install and run sumo-ratings. 

sudo apt update 

# install logging agent 
curl -sSO https://dl.google.com/cloudagents/install-logging-agent.sh
sudo bash install-logging-agent.sh

#install pipenv and git 
sudo apt -y install pipenv
sudo apt -y install git

# clone repo and change to that directory 
git clone https://github.com/Sumo-Data/sumo-ratings.git home/joseph_p_hackett/sumo-ratings && cd home/joseph_p_hackett/sumo-ratings

pipenv install 
pipenv run python sumo_ratings.py