# Task 1: Three Server Web Infrastructure Design

![1-distributed_web_infrastructure](https://github.com/njdam/alx-system_engineering-devops/assets/16462040/886098ef-e7ff-4c8a-aa95-8bbc837d8842)

## I. [Web Infrastructure Diagram]()

1. ***2 Servers***: There are two physical servers in this setup to provide redundancy and avoid a single point of failure (SPOF).

2. ***Web Server (Nginx)***: Nginx is used as the web server to handle incoming HTTP requests and serve static content efficiently. It can also act as a reverse proxy to forward requests to the application server.

3. ***Application Server***: The application server hosts your code base and processes dynamic requests from users.

4. ***Load Balancer (HAProxy)***: HAProxy is configured to distribute incoming traffic between the two application servers. It uses a round-robin distribution algorithm to distribute requests evenly.

5. ***Application Files***: The application files are stored on the application server, containing your code base and any resources needed for your website.

6. ***Database (MySQL)***: A MySQL database is used to store and manage your website's data.


## II. [Explanation for Additional Elements:]()

1. ***2 Servers***: Having two servers increases availability and fault tolerance. If one server goes down, the other can still handle requests.


2. ***Load Balancer***: The load balancer distributes traffic evenly between the application servers, ensuring efficient resource utilization and reducing load on any single server.


3. ***Database:*** The database stores and manages website data, making it accessible to both application servers.


4. ***Load Balancer Algorithm:***

* `Round-Robin Algorithm`: The load balancer uses a round-robin algorithm to distribute incoming requests sequentially to each application server in a circular order.


5. ***Is load-balancer enabling an Active-Active or Active-Passive?***

* `Active-Active`: This setup is active-active, as both application servers are actively serving traffic. In an active-active setup, both servers are actively processing requests simultaneously.

* `Active-Passive`: In an active-passive setup, only one server is actively processing requests, while the other remains in a standby state.


6. ***Database Primary-Replica Cluster:***

* In a Primary-Replica (Master-Slave) setup, the primary node (master) handles write operations, while the replica nodes (slaves) replicate data from the primary and handle read operations.

* This setup provides data redundancy, backup, and read scalability.

* **Primary vs Replica**:

	* `Primary Node`: Handles write operations and updates to the database. It's the authoritative source for data changes.

	* `Replica Node`: Handles read operations and provides a copy of the data from the primary node. It improves read performance and can act as a failover in case the primary node fails.


## [Identified Issues for This Web infrastructure:]()

1. ***Single Points of Failure (SPOF):***

* The load balancer itself can become a SPOF. If it fails, traffic distribution stops.

* The database can also become a SPOF if the primary node fails and there's no automatic failover mechanism.


2. ***Security Issues:***

* `Lack of firewall`: Without a firewall, the servers are more vulnerable to unauthorized access and attacks.

* `No HTTPS`: The absence of HTTPS leaves user data and communications unprotected during transmission.


3. ***No Monitoring:***

* Monitoring tools are needed to track server and application health, performance, and resource utilization. Without monitoring, issues might go unnoticed.


[Note that:]() This is a high-level design, and actual implementations might involve more configuration and setup. Additionally, addressing the identified issues would require further steps such as implementing load balancer high availability, enabling HTTPS, setting up firewalls, and implementing monitoring tools.
