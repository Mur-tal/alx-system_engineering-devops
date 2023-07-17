# 0x13. Firewall
#### DevOps, SysAdmin, Security
##### [Task 0. Block all incoming traffic but](./0-block_all_incoming_traffic_but)
Let’s install the `ufw` firewall and setup a few rules on `web-01`.

<b>Requirements:</b>  
* The requirements below must be applied to `web-01` (feel free to do it on `lb-01` and `web-02`, but it won’t be checked)
* Configure `ufw` so that it blocks all incoming traffic, except the following TCP ports:
1. `22` (SSH)
2. `443` (HTTPS SSL)
3. `80` (HTTP)  

<b>Resources</b>
[How To Set Up a Firewall with UFW on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-20-04)

