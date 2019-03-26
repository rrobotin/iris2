#!/bin/bash
echo -e "PWD #####\n"
pwd
cd ~/mozilla/iris
echo -e "PWD #####\n"
pwd
echo -e " apt update ##### \n"
sudo apt-get update
cd bootstrap/
echo -e "LIST #####\n"
ls -all
echo -e " bootstrap ##### \n"
sudo chmod +x bootstrap.sh
sudo chmod +x linux_bootstrap.sh
sudo ./bootstrap.sh
pip install pip==9.0.3
pip install pipenv
echo -e " pipenv install ##### \n"
sudo pipenv install
echo -e " FINISH INSTALL!!!! ##### \n"
