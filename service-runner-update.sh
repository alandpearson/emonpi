#!/bin/bash

# emonPi update for use with service-runner add following entry to crontab:
# * * * * * /home/pi/emonpi/service-runner >> /var/log/service-runner.log 2>&1

username="pi"
homedir="/home/$username"
echo "username: $username"
echo

echo "-------------------------------------------------------------"

# Clear log update file
cat /dev/null > $homedir/data/emonpiupdate.log

echo "Starting emonPi Update >"
echo "via service-runner-update.sh"
echo "Service Runner update script V1.1.1"
echo "EUID: $EUID"
argument=$1
echo "Argument: "$argument
# Date and time
date

# make file system read-write
if [ -f /usr/bin/rpi-rw ]; then
  rpi-rw
fi

# Pull in latest emonpi repo before then running updated update scripts
echo "git pull $homedir/emonpi"
cd $homedir/emonpi
sudo rm -rf hardware/emonpi/emonpi2c/
git branch
git status
git pull

# Run update in main update script
$homedir/emonpi/update/main.sh
