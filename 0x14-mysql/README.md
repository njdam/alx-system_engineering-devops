<center><h1>MySQL</h1></center>

MySQL is an open-source relational database management system (RDBMS) that is widely used for managing and storing data. It is known for its speed, reliability, and ease of use, making it a popular choice for both small-scale and large-scale applications.

<center><h2>Here are some key features and information about MySQL:</h2></center>

1. **Open Source:** MySQL is an open-source database system, which means that it is freely available, and its source code can be modified to suit specific needs. It is developed, distributed, and supported by Oracle Corporation.

2. **Relational Database:** MySQL is a relational database, which means it organizes data into structured tables with rows and columns. This structured approach makes it easy to store and retrieve data.

3. **SQL Language:** MySQL uses the Structured Query Language (SQL) for data manipulation and management. SQL is a standard language for interacting with relational databases.

4. **High Performance:** MySQL is known for its high performance and efficiency. It can handle large volumes of data and is suitable for applications that require fast and efficient data retrieval.

5. **Scalability:** MySQL can be easily scaled to meet the needs of growing applications. It supports both vertical and horizontal scaling, allowing for increased capacity and performance as needed.

6. **Security:** MySQL provides various security features, including user authentication, access control, and encryption, to protect data from unauthorized access and attacks.

7. **ACID Compliance:** MySQL is ACID (Atomicity, Consistency, Isolation, Durability) compliant, which ensures that database transactions are reliable and maintain data integrity.

8. **Replication and Clustering:** MySQL supports replication and clustering, allowing you to create redundant copies of your data for backup, failover, and load distribution.

9. **Community and Enterprise Editions:** MySQL is available in both community and enterprise editions. The community edition is open source and free to use, while the enterprise edition provides additional features and support.

10. **Storage Engines:** MySQL supports different storage engines, such as InnoDB, MyISAM, and more. Each storage engine has its own characteristics and features, allowing you to choose the one that best fits your application's requirements.

11. **Cross-Platform:** MySQL is cross-platform and can be run on various operating systems, including Linux, Windows, macOS, and more.

12. **Third-Party Tools and Libraries:** There are numerous third-party tools and libraries available for MySQL, making it easier to manage and interact with the database.

13. **Usage:** MySQL is used in a wide range of applications, including web development, content management systems (CMS), e-commerce platforms, data warehousing, and more.

14. **Competitors:** MySQL faces competition from other relational database systems like PostgreSQL, Oracle Database, Microsoft SQL Server, and SQLite, as well as NoSQL databases like MongoDB.

[Note That:]() MySQL is a versatile database system that can be tailored to suit various application needs. Its popularity in the web development world and the availability of extensive documentation and community support make it a valuable choice for many developers and organizations.


<center><h2>Review Questions</h2></center>

<h3>1. Main Role of a Database:</h3>

The main role of a database is to efficiently and securely store, manage, retrieve, and organize data.

* Databases serve as central repositories for structured data, allowing users and applications to perform various operations on the data, including adding, updating, deleting, and querying.

* Databases play a crucial role in data management, providing data integrity, consistency, and reliability.

* They are used in a wide range of applications, including web and mobile apps, business systems, e-commerce platforms, content management systems, and more.


<h3>2. Database Replica:</h3>

A database replica is a copy of a database that is synchronized with the original (master) database. Replicas are typically created for the purpose of redundancy, scalability, and high availability. There are two main types of database replicas:

* **Read-Only Replica:** This type of replica is primarily used for read operations. It allows multiple users or applications to read data simultaneously without affecting the performance of the master database. Read-only replicas can improve query response times and distribute read traffic.

* **Master-Slave Replica (or Primary-Secondary Replica):** In this configuration, one database server (the master or primary) handles write operations, while one or more replica servers (the slaves or secondaries) replicate the data from the master and serve read operations. Master-slave replication provides fault tolerance and load distribution.


<h3>3. Purpose of a Database Replica:</h3>

The primary purposes of having database replicas are as follows:

* **High Availability:** Database replicas provide redundancy, ensuring that data remains accessible even if the master database or server experiences downtime or failures. This is critical for applications that require continuous availability.

* **Load Balancing:** Replicas distribute read traffic across multiple servers, which can improve the overall performance and responsiveness of the database system.

* **Disaster Recovery:** Replicas serve as backup copies of the data. In the event of data corruption, accidental deletion, or other catastrophic events, replicas can be used to restore the database to a previous state.


<h3>4. Storing Database Backups in Different Physical Locations:</h3>

Storing database backups in different physical locations is important for several reasons:

* **Redundancy:** If backups are stored in a single location and that location experiences a disaster (e.g., fire, flood, or hardware failure), the backups could be lost. Storing backups in multiple physical locations ensures redundancy and minimizes the risk of data loss.

* **Disaster Recovery:** In the event of a regional disaster or site-wide failure, having backups in a different location allows for faster recovery and business continuity.

* **Compliance:** Some industries and regulations require data to be backed up and stored in geographically dispersed locations to ensure data security and availability.


<h3>5. Regularly Testing Database Backup Strategy:</h3>

To ensure that your database backup strategy works effectively, you should regularly perform the following operations:

* **Testing Restores:** Periodically test the process of restoring data from backups. This ensures that your backup files are not corrupted and that you can successfully recover data when needed. Testing restores helps identify any issues in the backup and restore procedures.

* **Validation:** After restoring data, validate that the restored data is consistent and accurate. Check for data integrity and completeness to confirm that the backup strategy is reliable.

* **Backup Monitoring:** Implement monitoring and alerting systems to notify you of any backup failures or issues. Regularly review backup logs and reports to detect and address any anomalies.

* **Documentation and Procedures:** Keep your backup procedures and documentation up to date. Ensure that your team is familiar with the backup and recovery process and that procedures are well-documented.

[Note That:]() By regularly testing your backup strategy, you can be confident that your data is adequately protected and recoverable in case of unforeseen events or data loss scenarios.

## MANDATORY TASKS

<h3>TASK 4</h3>

***Server 1:***

Commenting out bind address & Add this in /etc/mysql/mysql-conf.d/mysql.cnf
```
#bind-address 	= 127.0.0.1
server-id 	= 1
log_bin		= /var/log/mysql/mysql-bin.log
binlog_do_db 	= tyrell_corp
```

***Server 2:***

Commenting out bind address & Add this in /etc/mysql/mysql-conf.d/mysql.cnf
```
#bind-address   = 127.0.0.1
server-id       = 2
relay-log       = /var/log/mysql/mysql-relay-bin.log
log_bin         = /var/log/mysql/mysql-bin.log
binlog_do_db    = tyrell_corp
```

and in mysql server 2

```
mysql> CHANGE MASTER TO MASTER_HOST='--.--.--.--', # Ip adress server 1
    -> MASTER_USER='replica_user',  # User of replicator
    -> MASTER_PASSWORD='****',  # Password of User
    -> MASTER_LOG_FILE='mysql-bin.000001',  # LOG file name in server 1
    -> MASTER_LOG_POS=154;  # POSITION number in server 1 on master satatus
Query OK, 0 rows affected, 2 warnings (0.07 sec)

mysql> START SLAVE;
Query OK, 0 rows affected (0.00 sec)

mysql> SHOW SLAVE STATUS\G
```
