# Task 2: Secured and monitored web infrastructure

## I. [Design of Three-Server Web Infrastructure for www.foobar.com:]()

1. ***Load Balancer:***

* `Purpose`: Distribute incoming traffic across multiple servers for load distribution and high availability.

* `Explanation`: Load balancers help evenly distribute incoming requests across the three servers, preventing any single server from being overwhelmed and ensuring better performance and fault tolerance.


2. ***Firewalls (3):***

* `Purpose`: Protect servers from unauthorized access, malicious attacks, and traffic filtering.

* `Explanation`: Firewalls act as a barrier between the servers and the internet, filtering incoming and outgoing traffic to block potentially harmful requests and ensure the security of the infrastructure.


3. ***SSL Certificate:***

* `Purpose`: Enable secure communication over HTTPS by encrypting data transmission.

* `Explanation`: SSL certificates are essential for encrypting sensitive data exchanged between the client's browser and the server, ensuring the confidentiality and integrity of the communication.


4. ***Web Servers (3):***

* `Purpose`: Serve web content and process incoming requests.

* `Explanation`: Web servers handle client requests, process dynamic content, and return web pages to users' browsers. Having multiple web servers improves performance, as the load balancer distributes traffic among them.


5. ***Application Servers (3):***

* `Purpose`: Execute application logic, process requests, and interact with databases.

* `Explanation`: Application servers are responsible for processing business logic and generating dynamic content. Separating them from web servers allows for better scalability and maintainability.


6. ***Database Servers (3):***

* `Purpose`: Store and manage website data.

* `Explanation`: Database servers store data required by the website. Having separate database servers enables redundancy and load distribution, enhancing performance and data availability.


7. ***Monitoring Clients (3 - SumoLogic):***

* `Purpose`: Collect data about server performance, security, and user experience.

* `Explanation`: Monitoring tools like SumoLogic collect and analyze data from servers, helping identify performance bottlenecks, security breaches, and user experience issues.


## II. [Issues with the Infrastructure:]()

1. ***Terminating SSL at Load Balancer:***

* `Issue`: Encrypting and decrypting SSL/TLS at the load balancer can strain its resources and increase latency. It exposes decrypted traffic within the internal network.


2. ***Single MySQL Server for Writes:***

* `Issue`: A single MySQL server for write operations creates a single point of failure. If the server fails, write operations and data integrity are compromised.


3. ***Uniform Server Components:***

* `Issue`: Using the same components (database, web server, app server) on all servers can lead to a lack of diversity. A vulnerability affecting one component can affect all servers simultaneously.


4. ***Monitoring Web Server QPS***

To monitor web server Query Per Second (QPS):

* Set up monitoring agents to collect data from each web server.
* Define monitoring metrics related to QPS (e.g., requests per second).
* Configure alerts to trigger when QPS exceeds predefined thresholds.
* Use monitoring tools to visualize and analyze QPS trends over time.


[Note That:]() This design is a starting point, and considerations such as scaling, redundancy, and specific security configurations may require further adjustments based on the website's actual needs and expected traffic.
