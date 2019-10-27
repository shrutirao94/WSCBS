#!/usr/bin/env bash

set -e # exit if any non 0 exit code

apt update
echo "apt update DONE" >> ~/status.txt

apt --assume-yes install python3-pip
echo "install pip DONE" >> ~/status.txt

# echo "export LC_ALL=C.UTF-8" >> ~/.bashrc
# echo "export LANG=C.UTF-8" >> ~/.bashrc
# echo "export FLASK_APP=url_shortner" >> ~/.bashrc
# echo "export FLASK_ENVIRONMENT=development" >> ~/.bashrc

export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export FLASK_APP=url_shortner
export FLASK_ENVIRONMENT=development
echo "export lang DONE" >> ~/status.txt

# exec $SHELL
# echo "reset shell DONE" >> ~/status.txt

pip3 install flask
pip3 install short-url
echo "install dependencies DONE" >> ~/status.txt

cp -R url_shortner/ ~/
echo "cp app DONE" >> ~/status.txt

cd ~/
flask init-db
echo "init-db DONE" >> ~/status.txt

echo "starting service..." >> ~/status.txt
flask run --host=0.0.0.0 --port=5000
