# Task 1: Three Server Web Infrastructure Design

![1-distributed_web_infrastructure](https://github.com/njdam/alx-system_engineering-devops/assets/16462040/886098ef-e7ff-4c8a-aa95-8bbc837d8842)

## I. [Infrastructure Design:]()

1. ***Web Servers (Nginx):***

Two web servers to handle incoming requests.
Nginx will serve as the web server software to handle HTTP requests.
Application Server:

One application server to process dynamic content and business logic.
Hosts the application codebase.
Load Balancer (HAProxy):

One load balancer (HAProxy) to distribute incoming traffic among the web servers.
Distribution Algorithm: Round Robin - This evenly distributes requests among the available servers in a cyclic manner.
Application Files:

Application codebase stored on the application server.
Contains the website's logic and functionality.
Database (MySQL):

MySQL database to store website data.
Primary-Replica (Master-Slave) Cluster Setup:
Primary Node: Handles write operations (INSERT, UPDATE, DELETE).
Replica Node: Handles read operations (SELECT) and replicates data from the primary node.
Specifics about the Infrastructure:
Web Servers: Added for redundancy and to handle incoming HTTP requests. Nginx is used for its efficient handling of static content and reverse proxy capabilities.

Application Server: Manages application logic, dynamic content generation, and interacts with the database.

Load Balancer (HAProxy):

Distribution Algorithm: Round Robin is chosen for its simplicity, evenly distributing traffic.
Active-Passive Setup: One HAProxy instance is active while the other remains passive, taking over only if the active instance fails.
Database (MySQL) Primary-Replica Cluster:

Primary Node: Responsible for write operations, maintaining data consistency.
Replica Node: Serves read requests, reducing the load on the primary node.
Replication: Data changes on the primary node are asynchronously replicated to the replica node.
Issues with the Infrastructure:
Single Points of Failure (SPOF):

All components are vulnerable to failure. If any server or the load balancer fails, the service could be disrupted.
Security Issues:

Lack of firewall exposes the servers to potential attacks.
Lack of HTTPS leaves data transmission unencrypted, risking data interception.
No Monitoring:

The absence of monitoring tools makes it challenging to identify performance issues, resource utilization, or potential failures.

[Note That:]() Please note that this design is a basic representation of the infrastructure, and there are many additional considerations and configurations that could be made to further enhance its reliability, security, and performance.


Certainly! Here's a whiteboard design of the web infrastructure based on your requirements, along with explanations and identified issues:

Web Infrastructure Diagram

Design Overview:

2 Servers: There are two physical servers in this setup to provide redundancy and avoid a single point of failure (SPOF).

Web Server (Nginx): Nginx is used as the web server to handle incoming HTTP requests and serve static content efficiently. It can also act as a reverse proxy to forward requests to the application server.

Application Server: The application server hosts your code base and processes dynamic requests from users.

Load Balancer (HAProxy): HAProxy is configured to distribute incoming traffic between the two application servers. It uses a round-robin distribution algorithm to distribute requests evenly.

Application Files: The application files are stored on the application server, containing your code base and any resources needed for your website.

Database (MySQL): A MySQL database is used to store and manage your website's data.

Explanation:

Additional Elements:

2 Servers: Having two servers increases availability and fault tolerance. If one server goes down, the other can still handle requests.
Load Balancer: The load balancer distributes traffic evenly between the application servers, ensuring efficient resource utilization and reducing load on any single server.
Database: The database stores and manages website data, making it accessible to both application servers.
Load Balancer Algorithm:

Round-Robin Algorithm: The load balancer uses a round-robin algorithm to distribute incoming requests sequentially to each application server in a circular order.
Active-Active vs. Active-Passive:

Active-Active: This setup is active-active, as both application servers are actively serving traffic. In an active-active setup, both servers are actively processing requests simultaneously.
Active-Passive: In an active-passive setup, only one server is actively processing requests, while the other remains in a standby state.
Database Primary-Replica Cluster:

In a Primary-Replica (Master-Slave) setup, the primary node (master) handles write operations, while the replica nodes (slaves) replicate data from the primary and handle read operations.
This setup provides data redundancy, backup, and read scalability.
Primary vs. Replica:

Primary Node: Handles write operations and updates to the database. It's the authoritative source for data changes.
Replica Node: Handles read operations and provides a copy of the data from the primary node. It improves read performance and can act as a failover in case the primary node fails.
Identified Issues:

Single Points of Failure (SPOF):

The load balancer itself can become a SPOF. If it fails, traffic distribution stops.
The database can also become a SPOF if the primary node fails and there's no automatic failover mechanism.
Security Issues:

Lack of firewall: Without a firewall, the servers are more vulnerable to unauthorized access and attacks.
No HTTPS: The absence of HTTPS leaves user data and communications unprotected during transmission.
No Monitoring:

Monitoring tools are needed to track server and application health, performance, and resource utilization. Without monitoring, issues might go unnoticed.
Please note that this is a high-level design, and actual implementations might involve more configuration and setup. Additionally, addressing the identified issues would require further steps such as implementing load balancer high availability, enabling HTTPS, setting up firewalls, and implementing monitoring tools.
