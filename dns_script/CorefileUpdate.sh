#!/bin/bash
NAME=$"coredns"
BACKUPPATH=$"/home/coredns"
CONFPATH=$"/etc/coredns"
SCRIPTPATH=$""
echo "-------------------------------------"
echo "Corefile Update Script - by nvlong17"
sleep 2
echo "Backing up current configurations!"
sleep 2
#Make a backup of the config
tar -zcvf $BACKUPPATH/backup/$NAME.$(date +%m%d%y%H).tar.gz $CONFPATH
sleep 5
#Delete any backup older than 5 days
find $BACKUPPATH/backup/$NAME* -mtime +5 -exec rm {} \;
sleep 3
#Execute update script
python3 "${SCRIPTPATH}"/Main.py 2
sleep 2
#Restart CoreDNS
echo "Restarting CoreDNS service"
sleep 2
systemctl restart coredns
sleep 5
echo "Finished executing Corefile update script!"
echo "-------------------------------------"
