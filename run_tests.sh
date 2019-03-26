#!/bin/bash
echo -e "PWD #####\n"
pwd
cd ~/rrobotin/iris2
echo -e "PWD #####\n"
pwd
export DISPLAY=:99.0
Xvfb :99 -screen 0 1920x1080x24+32 +extension GLX +extension RANDR > /dev/null 2>&1 &
sleep 3
echo -e " start CI tests ##### \n"
sudo pipenv run iris firefox ci_tests/test_fake_keyboard_input.py -vk -i DEBUG
echo -e " FINISH RUNNING TESTS !!!! ##### \n"
