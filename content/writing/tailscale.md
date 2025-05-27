Title: Tailscale
Date: 2025-05-21 21:25
Category: Writing
Tags: 
Slug: 
Authors: Matt Leaverton
Summary: 
Status: published

Recently I've been writing and hosting web services on a Raspberry Pi in my local network. A majority of the time, I'm within access range of the network when I need to interact with the services, so this has been working well enough. Increasingly, I'm running into cases where I need access to the data when I'm out of range - especially my reading list - so I'm digging in to take the time to set up a private network so I can phone home when I'm away.

## Dynamic DNS
I remember messing around with DDNS way back in the early 2000s when my brother and I were trying to figure out how servers worked. It worked then, and I'm sure it would probably work now, but this led me in circles of which portion or how much to implement myself or delegate to a service or which service to trust, and I discounted this quickly. I also don't need to host a site from my home, which a lot of services felt more geared toward.

Honestly didn't give this a fair try. It really feels like more of a relic of home tinkering - especially when cloud services are so accessible. An instant VPS is a more reasonable value proposition if I ended up hosting anything publicly.  

## Tailscale
I remember reading about Tailscale when it launched - likely on HackerNews - and seeing how jazzed everyone was about it. At the time, it wasn't in my scope of need, so I followed with mild interest.

At some point a couple years back, after browsing homelab setups on reddit, I put in a half-baked effort to run some services on a Raspberry Pi. The recommendation at the time was to use [Tailscale](https://tailscale.com/){: target=_blank} to link everything together. Setup was easy and everything was looking good, but I set it up on my phone and it absolutely wrecked my battery life. This + my ill-conceived foray into homelab with no plan or goal, I shelved this.

## Cloudflare Tunnels
For my current (less half-baked, TBD on how well-conceived) effort, I 
Cloudflare has an offering called [Tunnels](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/){: target=_blank} that looks like it should do what I want, but for the life of me I was not able to get it working. I gave it a try the night before I trip where I thought it might be handy to have access to my home network, and I burned a couple hours banging my head against it. To my eyes, the docs assumed knowledge of other Cloudflare inner workings or standard practices that I had no knowledge of. Not being at a time in my life where I have oodles of hours to burn in a rage-IT-vortex, I gave up on this one.

There are several interesting looking offerings in Cloudflare's Zero Trust offerings - I expect I'll try again one day to see if I can sort it out.

## Tailscale Redux
Clearly since this post is titled '[Tailscale](https://tailscale.com/){: target=_blank}', this is where I landed. As is my wont, I was racing down rabbit holes trying to find the easiest and cheapest way to remotely access my services, which almost always ends up with me wasting time, then paying anyway for a service. In this case, I ended up doing neither (so far). The setup is ridiculously fast and painless. I now have several devices connected, so I can access my data and network from anywhere - it is transparent and magical.

In the first few days of use, Tailscale is averaging 5-7% of my phone battery draw, which for now is acceptable. The convenience of access to my data remotely hugely outweighs this now in the tradeoff. I'm a fan.  
