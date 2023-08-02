# Networking basics #1

1. [localhost/127.0.0.1:]()

`localhost` or `127.0.0.1` is a special loopback IP address used to refer to the local machine itself. It is often used to test network services on the same machine without actually sending data over the network.


2. [0.0.0.0:]()

`0.0.0.0` is a special IP address used to represent all IP addresses in the context of network routing and binding to local addresses. When used as a listening address by a server application, it means the server is listening on all available network interfaces.


3. [/etc/hosts:]()

`/etc/hosts` is a plain text file used in Unix-like operating systems to map hostnames to IP addresses. It is used as a local DNS lookup file to resolve domain names to IP addresses without querying an external DNS server. Users can manually define hostname-to-IP mappings in this file.


4. [How to display your machine's active network interfaces:]()

You can use the ifconfig or ip command to display active network interfaces on your machine.

=> Using `ifconfig` (traditional way, not available on all systems):

```
ifconfig
```

=> Using `ip` (modern way, available on most systems):

```
ip addr show
```

[Note That:]() Both commands will display information about the active network interfaces on your machine, including their names, IP addresses, netmasks, and other network-related information. Please note that the exact commands and output may vary depending on your operating system and its version.
