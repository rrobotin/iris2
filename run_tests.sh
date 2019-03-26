#!/bin/bash
echo -e "PWD #####\n"
pwd
cd ~/mozilla/iris
echo -e "PWD #####\n"
pwd
export DISPLAY=:99.0
Xvfb :99 -screen 0 1920x1080x24+32 +extension GLX +extension RANDR > /dev/null 2>&1 &
sleep 3
echo -e " start CI tests ##### \n"
sudo pipenv run iris -j -n -d ci_tests -i DEBUG
echo -e " FINISH RUNNING TESTS !!!! ##### \n"
