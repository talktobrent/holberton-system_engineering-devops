<h1>0x14. Mysql</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is the main role of a database</li>
<li>What is a database replica</li>
<li>What is the purpose of a database replica</li>
<li>Why database backups need to be stored in different physical locations</li>
<li>What operation should you regularly perform to make sure that your database backup strategy actually works</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Setup a Primary-Replica infrastructure using MySQL
  </h3>
<p>Install and configure MySQL  on<code>web-01</code> and <code>web-02</code> so that they for a primary/replica (master/slave) cluster.</p>
<p>Having a replica member on for your MySQL database has 2 advantages:</p>
<ul>
<li>Redundancy: if you lose one of the database servers, you will still have another working one and a copy of your data</li>
<li>Load distribution: you can split the read operations between the 2 servers, allowing to reduce the load on the primary member and improve query response speed</li>
</ul>
<p>Requirements:</p>
<ul>
<li>MySQL primary must be hosted on <code>web-01</code> - do not use the <code>bind-address</code>,  just comment this parameter</li>
<li>MySQL replica must be hosted on <code>web-02</code></li>
<li>Setup replication for the MySQL database named <code>holberton</code></li>
<li>Provide your MySQL primary configuration as answer file(<code>my.cnf</code>) with the name <code>0-mysql_configuration_primary</code></li>
<li>Provide your MySQL replica configuration as an answer file with the name <code>0-mysql_configuration_replica</code></li>
<li>Create a MySQL user named <code>holberton</code>, password <code>projectcorrection280hbtn</code> with read access on replication status (the checker will use it to verify that replication is running fine)</li>
<li>Make sure that task #3 of your SSH project is completed for <code>web-01</code> and <code>web-02</code>, the checker will connect to your servers to check MySQL status - mainly this task: Let me in! </li>
<li><strong>Make sure to do task #3 of your SSH project for the <code>web-02</code> server as the key needs to be on both servers</strong></li>
</ul>
<p>Tips:</p>
<ul>
<li>Make sure you have at least one table with one row in your primary database before starting the replication</li>
<li>Once MySQL is installed on <code>web-01</code>, create a database containing at least one table with one record (name and what type of fields does not matter)</li>
<li>Once MySQL replication is setup, add a new record in your table via MySQL on <code>web-01</code> and check if the record has been replicated in MySQL <code>web-02</code>. If you see it, it means your replication is working!</li>
</ul>
        <p>File: <code>0-mysql_configuration_primary, 0-mysql_configuration_replica</code></p>
  <h3>
    1. MySQL backup
  </h3>
<p>What if the data center where both your primary and replica database servers are hosted are down because of a power outage or even worse: flooding, fire? Then all your data would inaccessible or lost. That&rsquo;s why you want to backup and store them in a different system in another physical location. This can be achieved by dumping your MySQL data, compressing them and storing them in a different data center.</p>
<p>Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.</p>
<p>Requirements:</p>
<ul>
<li>The MySQL dump must contain all your MySQL databases</li>
<li> The MySQL dump must be named <code>backup.sql</code></li>
<li>The MySQL dump file has to be compressed to a <code>tar.gz</code> archive</li>
<li>This archive must have the following name format: <code>day-month-year.tar.gz</code></li>
<li>The user to connect to the MySQL database must be <code>root</code></li>
<li>The Bash script accepts one argument that is the password used to connect to the MySQL database</li>
</ul>
        <p>File: <code>1-mysql_backup</code></p>
