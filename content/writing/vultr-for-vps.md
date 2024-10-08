Title: VPS with Vultr
Date: 2023-07-30 21:35
Category: Writing
Tags: software, infra
Slug:
Authors: Matt Leaverton
Summary:
Status: published

I have started using [Vultr](https://www.vultr.com/) for a cheap VPS instance (again - I initially signed up
back in June 2021, resulting in Vultr getting a year of billing out of me for free). I'm using the
base level [Cloud Compute](https://www.vultr.com/pricing/#cloud-compute/), which is great for my purposes, 
and again - is cheap. I am planning to experimenting with hosting several simple Dockerized web apps for personal use.

Setup process was very simple - a few clicks, selecting a distro (Debian), a server name, and billing setup. 
There is a nifty web VNC client (using [noVNC](https://novnc.com/info.html)) accessible from the Vultr server dashboard that makes initial connection and setup dead simple. I copied over my 
SSH key and was off to the races (after I got [IPv6 working on my local network]({filename}local-ipv6-router.md){: target=_blank}).

I added a new user so that I do not live in root all the time:

```commandline
adduser matt
usermod -aG sudo matt
```

Disable password authentication for `ssh`

```commandline
sudo vi /etc/ssh/sshd_config
# Change the line with #PasswordAuthentication yes to PasswordAuthentication no
sudo systemctl restart sshd
```
