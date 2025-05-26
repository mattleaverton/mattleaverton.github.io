Title: Ethernet Only Raspberry Pi
Modified: 2025-01-29 22:23
Date: 2025-01-29 22:23
Category: Writing
Tags:
Slug:
Authors: Matt Leaverton
Summary:
Status: draft

Promoting my Raspberry Pi home server to a berth near the router, so it gets a nice upgrade from wifi to ethernet.




Add the following lines to `/boot/firmware/config.txt` (current location as of this writing, which is already different from the post below from a few years back)

```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```

Thanks to this post on [Stack Exchange](https://raspberrypi.stackexchange.com/questions/43720/disable-wifi-wlan0-on-pi-3/62522#62522)