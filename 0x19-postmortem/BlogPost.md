# My first postmortem

Postmortem: Web Stack Outage Incident

[PostMorten] https://www.eficode.com/hubfs/Blameless%20postmortem.png
[PostMorten] https://www.hardsplash.com/wp-content/uploads/2023/03/getting-actionable-insights-campaign-post-mortem-blog-hero.png

Issue Summary:


**Duration:**
Start Time: January 22, 2024, 14:00 UTC
End Time: January 22, 2024, 17:30 UTC

**Impact:**
The outage affected the core authentication service, rendering users unable to log in. Approximately 30% of our user base experienced disruptions, leading to frustration and a temporary halt in user activity.

**Root Cause:**
The root cause was identified as an unexpected surge in database connections, overwhelming the authentication service and causing a cascading failure.

**Timeline:**

14:00 UTC: Issue detected as a spike in error rates on the authentication service.

14:15 UTC: Monitoring alerts triggered, indicating a sudden increase in database connection errors.

14:30 UTC: Initial investigation focused on the authentication service logs and server metrics. Assumption: A potential issue with the authentication service code or server capacity.

15:00 UTC: Misleading path: Initial suspicion pointed towards a DDoS attack due to the unusual spike in traffic. Security team engaged for a detailed analysis.

15:30 UTC: With DDoS ruled out, attention shifted to database performance. Assumption: Database server overload leading to connection failures.

16:00 UTC: Incident escalated to the database operations team. Further investigation revealed an unoptimized query causing a surge in database connections.

16:30 UTC: The unoptimized query was identified and fixed, but database connections were not recovering. Misleading path: Focused on potential network issues between the authentication service and the database.

17:00 UTC: Incident escalated to senior engineers and database administrators. Discovered that the database connection pool was exhausted, causing the persistent connection failures.

17:30 UTC: Database connection pool increased, resolving the issue. Service recovery initiated, and error rates returned to normal.


**Root Cause and Resolution:**

**Root Cause:**
The unoptimized database query led to a surge in database connections, exhausting the connection pool and causing the authentication service to fail.

**Resolution:**
The immediate resolution involved fixing the unoptimized query and increasing the database connection pool. Additionally, a performance review of all critical queries was initiated to prevent similar issues.


**Corrective and Preventative Measures:**

**Things to Improve/Fix:**
Conduct a comprehensive review of all critical queries for optimization opportunities.
Implement automated monitoring for database connection pool health and set up alerts for potential issues.
Establish a post-incident review process to share learnings and improve incident response.


**Tasks to Address the Issue:**
Optimize all critical database queries, addressing performance bottlenecks.
Implement automated testing for database queries in the CI/CD pipeline.
Enhance monitoring and alerting systems to detect and respond to similar issues promptly.
Conduct a training session for the engineering team on identifying and troubleshooting database performance issues.
Document and communicate the incident response process to ensure a coordinated and efficient response in future incidents.

By addressing these corrective measures, we aim to fortify our system against similar incidents, enhance our monitoring capabilities, and foster a proactive approach to system performance and reliability.
