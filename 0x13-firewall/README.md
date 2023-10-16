# Firewall

***A firewall*** is a network security device or software that is designed to monitor, filter, and control incoming and outgoing network traffic based on an organization's previously established security policies. Firewalls are a critical component of network security and are used to protect networks, devices, and data from unauthorized access, cyberattacks, and other threats. 

<h3>Here are some key points about firewalls:</h3>

1. **Packet Filtering:** Firewalls inspect data packets as they pass through the network. They examine various attributes of packets, such as source and destination IP addresses, port numbers, and protocol types, and make decisions on whether to allow or block the packets based on defined rules.

2. **Stateful Inspection:** Stateful inspection firewalls keep track of the state of active connections. This means they are aware of the current state of connections, allowing them to make more informed decisions and better protect against unauthorized access.

3. **Proxy Services:** Some firewalls act as proxies, serving as intermediaries between internal and external network requests. These proxy firewalls can provide an additional layer of security by hiding the internal network structure.

4. **Application Layer Filtering:** Modern firewalls often include deep packet inspection (DPI) capabilities that can analyze the content of data packets to identify and block specific applications or protocols. This can help in preventing malicious or unauthorized applications from accessing the network.

5. **Access Control Lists (ACLs):** Firewalls use ACLs to define rules that dictate which network traffic is allowed and which is blocked. These rules can be customized to meet the organization's security requirements.

6. **Network Address Translation (NAT):** Firewalls can perform Network Address Translation to hide internal IP addresses from external networks. This enhances security by obfuscating the internal network structure.

7. **Intrusion Detection and Prevention:** Some firewalls have intrusion detection and prevention capabilities, which allow them to identify and respond to suspicious or malicious traffic patterns.

8. **Logging and Reporting:** Firewalls often maintain logs of network activity, which can be valuable for monitoring and auditing purposes. These logs provide information about security events and incidents.

9. **Security Policies:** Organizations define security policies that specify how the firewall should behave. These policies determine what traffic is allowed or denied and can be customized to meet specific security requirements.

10. **Virtual Private Networks (VPNs):** Some firewalls support VPN functionality, allowing secure remote access to the network and the encryption of data during transmission.

11. **Firewall Types:** There are various types of firewalls, including hardware firewalls (dedicated devices), software firewalls (installed on servers or endpoints), and cloud-based firewalls.

[Note That:]() Firewalls play a critic8al role in safeguarding networks and data from a wide range of threats, including hackers, malware, viruses, and other cyberattacks. They are an essential component of any comprehensive network security strategy.

<h3>Configure UFW (Uncomplicated Firewall) on Server</h3>

To configure the UFW (Uncomplicated Firewall) on your server (in this case, web-01) to block all incoming traffic except for the specified TCP ports (22, 443, and 80), you can follow these steps:

1. **Install UFW (if not already installed):**
If UFW is not already installed on your server, you can install it by running:
```
sudo apt update
sudo apt install ufw
```

2. **Set Default Policies:**
By default, you should block all incoming traffic and allow outgoing traffic:
```
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

3. **Allow Specific Ports:**
Allow incoming traffic on the specific ports (22, 443, and 80):
```
sudo ufw allow 22/tcp     # Allow SSH (Port 22)
sudo ufw allow 443/tcp    # Allow HTTPS SSL (Port 443)
sudo ufw allow 80/tcp     # Allow HTTP (Port 80)
```

4. **Enable UFW:**
Enable the UFW firewall:
```
sudo ufw enable
```

5. **Check the Status:**
You can check the status to ensure the rules are applied correctly:
```
sudo ufw status
```

6. **Optional:** If you're using SSH to access the server, make sure the SSH port (22) is allowed before enabling the firewall. Otherwise, you may lose your SSH connection.

[Done]() After following these steps, UFW will be configured to block all incoming traffic except for SSH (Port 22), HTTPS (Port 443), and HTTP (Port 80).

[Note That:]() Make sure to have console access or alternative methods to access the server if you are configuring this on a remote server, to prevent accidental lockout in case of any issues.

## MANDATORY TASK
```
Status: active

To                         Action      From
--                         ------      ----
Nginx HTTP                 ALLOW       Anywhere
22/tcp                     ALLOW       Anywhere
443/tcp                    ALLOW       Anywhere
80/tcp                     ALLOW       Anywhere
Nginx HTTP (v6)            ALLOW       Anywhere (v6)
22/tcp (v6)                ALLOW       Anywhere (v6)
443/tcp (v6)               ALLOW       Anywhere (v6)
80/tcp (v6)                ALLOW       Anywhere (v6)
```

## ADVANCED TASK

To configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP, you can use the Uncomplicated Firewall (UFW). Here's how you can achieve this:

1. **SSH into web-01:**
```
ssh ubuntu@web-01
```

2. **Edit the UFW configuration:**

You will need to modify the UFW configuration file to set up the port forwarding rule. The configuration file is typically located at `/etc/ufw/before.rules`.


3. **Open the UFW configuration file in a text editor using sudo:**
```
sudo vi /etc/ufw/before.rules
```


4. **Add the Port Forwarding Rule:**

Add the following rule to forward traffic from port `8080` to port `80`. This rule **should be added before** the `*filter` section in the `before.rules` file.
```
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -i eth0 -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT
```


5. **Here's what the rule does:**

It creates a new NAT table (`*nat`) to handle the port forwarding.
The PREROUTING chain is used to modify packets as they come into the network interface (`-i eth0`).

* `-A PREROUTING` appends a rule to the PREROUTING chain.
* `-p tcp` specifies that this rule applies to TCP traffic.
* `--dport 8080` specifies the destination port (port 8080).
* `-j REDIRECT --to-port 80` redirects the traffic to port 80.


6. **Save the File:**

Save the changes to the `before.rules` file and exit the text editor.


7. **Reload UFW:**

Reload UFW to apply the changes:
```
sudo ufw reload
```


8. **Check UFW Status:**

You can check the status of UFW to ensure that the changes are applied correctly:
```
sudo ufw status
```


9. **Testing:**

From web-02, you can use curl to test the port forwarding:
```
curl -sI web-01.example.tech:8080
```
You should see a response similar to what you provided, indicating that the port forwarding from 8080 to 80 is working.

[Please note that]() the configuration may vary depending on your specific server setup, so make sure to back up any configuration files before making changes and test thoroughly to ensure the port forwarding is working as expected
