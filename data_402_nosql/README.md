What is it?  
Compare SQL to NoSQL  
What language(s) can be used?  
Example NoSQL Schema design  
NoSQL is scalable. Explain the concept and some benefits of it and any negatives?  
Types of NoSQL Database (as many as you can find?
# NoSQL
### **What is NoSQL?**

When people use the term “NoSQL database”, they typically use it to refer to any non-relational database. Some say the term “NoSQL” stands for “non SQL” while others say it stands for “not only SQL.” Either way, most agree that NoSQL databases are databases that store data in a format other than relational tables.
Scalable and flexible

|               | SQL                                                                                                                                              | NO SQL                                                                                                                                           |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Database type | Relational Databases                                                                                                                             | Non-relational Databases / Distributed Databases                                                                                                 |
| Structure     | Table- based                                                                                                                                     | key-value pairs,  Document-Based, Graph databases,wide- column stores                                                                            |
| Scalability   | Designed for scaling up vertically by upgrading one expensive custom-built hardware                                                              | Designed for scaling out **horizontally** by using shards to distribute load across multiple commodity (inexpensive) hardware, more powerful     |
| Strength      | Great for highly structured data and don't anticipate changes to the database structure                                                          | Pairs well with fast paced, agile development teams. // Data consistency  (일관성)and integrity is not priority // Expecting high transaction load. |
| Pros          | - Easy to use and setup.  <br>- Universal, compatible with many tools.  <br>- Good at high-performance workloads.  <br>- Good at structure data. | - No investment to design model.  <br>- Rapid development cycles.  <br>- In general faster than SQL.  <br>- Runs well on the cloud.              |
| Cons          | - Time consuming to understand and design the structure of the database.  <br>- Can be difficult to scale.                                       | - Unsuited for interconnected data  <br>- Technology still maturing.  <br>- Can have slower response time.                                       |

### **Language**
SQL databases use SQL (Structured Query Language). NoSQL databases use JSON (JavaScript Object Notation), XML, YAML, or binary schema, facilitating unstructured data.

### **Example NoSQL Schema design**
![img.png](img.png)

#### Design Explanation:
The address has been moved as an array is flexible enough to accommodate additional entries in the future.
Each item in the address array has a limited number of fields, no need to create a separate collection.

![img_1.png](img_1.png)

#### Design Explanation:
1-M relationships are advised to handle in a single model where data size does not increase drastically. Therefore region, country, and state are handled in a single document which is kind of a defined set of data.
Cities are kept in a separate collection for 2 reasons:
For some countries, The number of cities is huge and this will make document size much bigger.
To avoid region unnecessary nested and complex modeling.

Schema - A vs B — Better Query Performance:
The city collection provides wider range of options to query data from region collection efficiently and faster, based on “region_id”, “country_id” and “state_id”.
Cities can be grouped easily based on “region_id”, “country_id” or “state_id” more efficiently.

![img_2.png](img_2.png)
#### Design Explanation:
This schema has less nested objects therefor more clarity
It is much easier for applications such as NodeJS apps to handle queries based on predefined schemas.
Schema — A vs B — Better Query Performance:
B does contain redundancy but in NoSQL, performance is preferred to normalization.
The data in the above example is relatively limited, but consider a business case where millions of documents are involved, the performance of Schema-A is no match for Schema-B throughput.

### Types of NoSQL
NoSQL databases come in several types, each designed to handle specific data storage and retrieval requirements. Here are the primary types of NoSQL databases along with examples:

1. ```Document Stores```
Description: Store and manage data as documents, typically in JSON, BSON, or XML format. They are suitable for semi-structured data and provide flexibility in data modelling.
Examples: MongoDB, CouchDB, RavenDB.

![img_4.png](img_4.png)
2. ```Key-Value Stores```
Description: Store data as key-value pairs, where each key is unique and maps to a value. They are highly performant for simple get and put operations.
Examples: Redis, Amazon DynamoDB, Riak, Aerospike

![img_3.png](img_3.png)
3. ```Column-Family Stores (Wide-Column Stores)```
Description: Store data in columns rather than rows, allowing for efficient storage and retrieval of large datasets. They are ideal for analytical applications.
Examples: Apache Cassandra, HBase, ScyllaDB, Google Bigtable

 ![img_5.png](img_5.png)
4. ```Graph Databases```
Description: Designed to store and navigate relationships between data points, represented as nodes and edges. They are excellent for use cases involving complex relationships.
Examples: Neo4j, Amazon Neptune, ArangoDB, OrientDB
![img_7.png](img_7.png)
5. ```Time-Series Databases```
Description: Optimised for storing and querying time-stamped or time-series data, making them suitable for applications like IoT, monitoring, and analytics.
Examples: InfluxDB, TimescaleDB, OpenTSDB, Prometheus
![img_8.png](img_8.png)

6. ```Object-Oriented Databases```
Description: Store data in the form of objects, as used in object-oriented programming. They provide seamless integration with object-oriented languages.
Examples: db4o, ObjectDB, InterSystems Caché
7. ```Multimodel Databases```
Description: Support multiple data models (e.g., document, graph, key-value) within a single database engine, providing flexibility for diverse use cases.
Examples: ArangoDB, OrientDB, MarkLogic
8. ```Search Engines```
Description: Optimised for search operations, providing full-text search capabilities along with advanced querying.
Examples: Elasticsearch, Apache Solr, Splunk
9. ```Tuple Store```
Description: Store data as tuples, which are ordered lists of elements. They are similar to key-value stores but allow more complex data structures.
Examples: Amazon SimpleDB, FoundationDB
10. ```Ledger Databases```
Description: Specialised for recording transactions and maintaining a secure, immutable ledger of data changes.
Examples: Amazon QLDB (Quantum Ledger Database), Hyperledger Fabric
11. ```Spatial Databases```
Description: Designed to store and query spatial or geographic data, supporting spatial indexing and queries.
Examples: PostGIS (extension for PostgreSQL), MongoDB with GeoJSON, Neo4j with spatial plugins
12. ```NewSQL Databases```
Description: Combine the ACID guarantees of traditional SQL databases with the scalability of NoSQL databases.
Examples: Google Spanner, CockroachDB, VoltDB
Each type of NoSQL database is optimised for specific types of workloads and data models, providing flexibility and performance benefits for various applications. Selecting the appropriate NoSQL database depends on the specific requirements of the application, including data structure, query complexity, scalability needs, and consistency requirements.
