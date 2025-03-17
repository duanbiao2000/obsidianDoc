---
aliases: 短URL链接服务：系统设计面试攻略！
createdAt: 2024-11-12 13:46
categories:
  - Tools
tags:
  - IELTS
---
Here’s a concise summary of the URL shortener system design content:
<!--more-->
[短URL链接服务：系统设计面试攻略！\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1pZmHY8Eqh/?vd_source=7038f96b6bb3b14743531b102b109c43)
1. **Core Functional Requirements**:
   - Shorten a long URL to a short one (7 characters max), supporting up to 100 million shortens per month.
   - Allow custom short URLs with up to 16 characters.
   - Redirect from short URL to long URL instantly; links persist for 100 years.
2. **Nonfunctional Requirements**:
   - High availability, rapid redirection, REST APIs for integration.
   - Support for about 8,000 reads per second and storage needs of up to 60 TB over 100 years.
3. **Traffic and Usage Patterns**:
   - Expected read-to-write ratio of 200:1, with about 700 million reads per day.
   - Popular links (20% of URLs) account for 80% of traffic, requiring around 70 GB for caching.
4. **System Scalability and Reliability**:
   - Use a load balancer to distribute traffic across servers to avoid single points of failure.
   - Implement caching for popular URLs using solutions like Redis to enhance read speeds.
5. **Database Choices**:
   - NoSQL databases (like Cassandra) are suitable for scaling with high read and write demands but have eventual consistency.
   - Alternatively, relational databases provide ACID compliance but are more complex to scale.
5. **Database Sharding and Caching**:
   - Use sharding with hashing to manage data distribution, with seven-character hashed URLs as keys.
   - For caching, use a Least Recently Used (LRU) policy to manage memory efficiently.
7. **Redundancy and Failover**:
   - Incorporate redundancy for caching and load balancing across servers to handle potential DDoS attacks or server downtime.
8. **Custom URL Handling**:
   - Custom URLs should have a minimum length (e.g., eight characters) to avoid conflicts with randomly generated ones.
   - Dedicated databases for custom URLs could support premium options if custom links are monetized.
9. **Load Balancing Strategies**:
   - Initially distribute traffic evenly using round-robin, with health checks to adjust based on server load.
10. **Security and Uniqueness**:
    - Use secure encoding methods like Base62 for URL generation, avoiding collision risks in popular algorithms like MD5. 
These points cover the core design elements, traffic assumptions, data storage, caching, load balancing, and scalability considerations in designing a URL shortener system.