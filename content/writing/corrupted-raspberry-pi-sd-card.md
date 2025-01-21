Title: Corrupted Raspberry PI SD Card
Modified: 2025-01-16 18:45
Date: 2025-01-16 18:45
Category: Writing
Tags:
Slug:
Authors: Matt Leaverton
Summary:
Status: draft

Backup image
`sudo ddrescue /dev/sda raspberry_backup.img raspberry_backup.logfile`

Industrial SD card
Fast flash drive

The plan is to make the SD card with the filesystem read-only, then do work on the flash drive. This way if the file system corrupts, all of my work is still available on the flash drive. TBD.

Investigating `litestream` for Sqlite backups.



Reinstall Docker
```
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker $USER
```


Chat with details is here:
https://chat.mattleaverton.com/c/ca429df4-43bc-4f9b-afba-0632f4c43c8e




set flash drive as home dir
```
lsblk
sudo mkfs.ext4 /dev/sda1
...
TBD
```

change Docker data dir
```
sudo systemctl stop docker
sudo systemctl status docker
sudo mkdir -p /home/docker
sudo nano /etc/docker/daemon.json
sudo chown root:root /home/docker
sudo systemctl start docker
docker info | grep "Docker Root Dir"
```

log2ram
```
curl -L https://github.com/azlux/log2ram/archive/master.tar.gz | tar zxf -
cd log2ram-master
chmod +x install.sh && sudo ./install.sh
cd ..
rm -r log2ram-master/
sudo nano /etc/log2ram.conf
du -sh /var/log
sudo du -sh /var/log
sudo nano /etc/log2ram.conf
sudo reboot
```