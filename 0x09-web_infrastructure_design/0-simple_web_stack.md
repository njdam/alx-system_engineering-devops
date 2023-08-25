# 0. Simple web stack

![0-simple_web_stack](https://github.com/njdam/alx-system_engineering-devops/assets/16462040/51eb5882-5550-416b-b337-a791221c0aa6)

## [I. Design of Single Server Web Infrastructure for www.foobar.com:]()

1. ***Server (8.8.8.8):***

A server is a powerful computer that hosts resources and services accessible over the network.

* It's the physical machine where the entire web infrastructure resides.


2. ***Role of Domain Name (www.foobar.com):***

* The `domain name` serves as the human-readable address for the website.
* It Easy to be memorable or remembeble that Ip address of every website.
* The DNS (Domain Name System) resolves the domain name to the server's IP address (8.8.8.8 in this case).


3. ***The type of DNS record www is in www.foobar.com***

* The `www` DNS record in `www.foobar.com` is a `CNAME` (`Canonical Name`) DNS record that points to the server's IP address.


4. ***Role of Web Server (Nginx):***

* The web server handle HTTP requests from users and serve web pages for requested website.
* Then, Nginx is a popular web server known for its efficiency and performance.


5. ***The Role of Application Server:***

* The application server hosts the application logic, processing user requests, and generating dynamic content.
* It communicates with the web server to process requests and deliver responses.


6. ***Application Files (Code Base):***

* The application files contain the website's code and resources.
* They are stored on the server and are accessed by the application server when generating web pages.


7. ***Role of Database (MySQL):***

* The database stores and manages the website's data, such as user accounts, posts, etc.
* where `MySQL` is a relational database management system.


8. ***Server Communication with User's Computer:***

* The server communicates with the `user's computer` over the `internet` using the `HTTP protocol`.
* When the user accesses `www.foobar.com`, their `browser` sends an `HTTP request` to the `server`, which `processes the request` and sends back an `HTTP response` containing the `web page content`.


## [II. Issues with this Single Server Infrastructure:]()

1. ***Single Point of Failure (SPOF):***

* Since all components are on a single server, if the server goes down, the entire website becomes inaccessible (go down).
*  To mitigate this, `redundant servers`, `load balancers`, and `failover mechanisms` must be implemented in this infrastructure.


2. ***Downtime During Maintenance:***

When maintenance is needed (e.g., deploying new code), the web server needs to be restarted.
* This results in downtime, impacting users' ability to access the site.
* Solutions to this, is like staging environments, canary releases, and rolling deployments can help to minimize downtime.


3. ***Scalability Challenges:***

* The single server setup cannot handle a large influx of incoming traffic effectively.
* To scale, horizontal scaling (adding more servers) and load balancing are required.


[Note That:]() In summary, while a single server with a LAMP stack can power a basic website, it comes with limitations such as potential downtime, scalability challenges, and a single point of failure. To address these issues, implementing redundant systems, load balancing, and a more distributed architecture is necessary for a robust and scalable web infrastructure.
