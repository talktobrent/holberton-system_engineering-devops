<h1>0x0B. Web server</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is the main role of a web server</li>
<li>What is a child process</li>
<li>Why web server usually have a parent process and child processes</li>
<li>What are the main HTTP requests</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Transfer a file to your server
  </h3>
  <p>Write a Bash script that transfers a file from our client to a server:</p>
<p>Requirements:</p>
<ul>
<li>Accepts 4 parameters
<ol>
<li>The path to the file to be transferred</li>
<li>The IP of the server we want to transfer the file to</li>
<li>The username <code>scp</code> connects with</li>
<li>The path to the SSH private key that <code>scp</code> uses</li>
</ol></li>
<li>Display <code>Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY</code> if less than 3 parameters passed</li>
<li><code>scp</code> must transfer the file to the user home directory <code>~/</code></li>
<li>Strict host key checking must be disabled when using <code>scp</code> </li>
</ul>
<p>In this example, I:</p>
<ul>
<li>remotely execute the <code>ls ~/</code> command via <code>ssh</code> to see what <code>~/</code> contains</li>
<li>create a file named <code>some_page.html</code></li>
<li>execute my <code>0-transfer_file</code> script</li>
<li> remotely execute the <code>ls ~/</code> command via <code>ssh</code> to see that the file <code>some_page.html</code> has been successfully transferred</li>
</ul>
<p>That is one way of publishing your website pages to your server.</p>
        <p>File: <code>0-transfer_file</code></p>
  <h3>
    1. Install nginx web server
  </h3>
<p>Readme:</p>
<ul>
<li>-y on apt-get command</li>
</ul>
<p>Web servers are the piece of software generating and serving HTML pages, let&rsquo;s install one!</p>
<p>Requirements:</p>
<ul>
<li>Install <code>nginx</code> on your <code>web-01</code> server</li>
<li>Nginx should be listening on port 80</li>
<li>When querying Nginx at its root <code>/</code> with a GET request (requesting a page)  using <code>curl</code>, it must return a page that contains the string <code>Holberton School</code></li>
<li>As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements</li>
</ul>
<p>In this example <code>34.198.248.145</code> is the IP of my <code>web-01</code> server. If you want to query the Nginx that is locally installed on your server, you can use <code>curl 127.0.0.1</code>.</p>
<p>If things are not going as expected, make sure to check out Nginx logs, they can be found in <code>/var/log/</code>.</p>
        <p>File: <code>1-install_nginx_web_server</code></p>
  <h3>
    2. Setup a domain name
  </h3>
  <p>Gandi is one of the top 25 domain providers. They are known for the stability and quality of their DNS hosting solution. Holberton School partnered with Gandi so that you can learn about DNS.</p>
<p>Gandi worked with domain name registrars to give you access to a free domain name for a year. Please use the promo code <strong>THXBETTY</strong>. Feel free to drop a thank you tweet for Gandi.</p>
<p>Using your Gandi account, acquire a domain name at this address, using one of these extensions: </p>
<ul>
<li><code>.website</code></li>
<li><code>.site</code></li>
<li><code>.space</code></li>
<li><code>.online</code></li>
</ul>
<p>Provide the domain name in your answer file.</p>
<p>Requirement:</p>
<ul>
<li>provide the domain name only (example: <code>foobar.online</code>), no subdomain (example: <code>www.foobar.online</code>)</li>
<li>configure your DNS records with an A entry so that your root domain points to your <code>web-01</code> IP address</li>
<li>go to your profile and enter your domain in the <code>Project website url</code> field</li>
</ul>
        <p>File: <code>2-setup_a_domain_name</code></p>
  <h3>
    3. Redirection
  </h3>
  <p>Readme:</p>
<ul>
<li>Replace a line with multiple lines with sed</li>
</ul>
<p>Configure your Nginx server so that <code>/redirect_me</code> is redirecting to another page.</p>
<p>Requirements:</p>
<ul>
<li>The redirection must be a &ldquo;301 Moved Permanently&rdquo;</li>
<li>You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements</li>
<li>Using what you did with <code>1-install_nginx_web_server</code>, write <code>3-redirection</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
</ul>
        <p>File: <code>3-redirection</code></p>
  <h3>
    4. Not found page 404
  </h3>
  <p>Configure your Nginx server to have a custom 404 page that contains the string <code>Ceci n&#39;est pas une page</code>.</p>
<p>Requirements:</p>
<ul>
<li>The page must return an HTTP 404 error code</li>
<li>The page must contain the string <code>Ceci n&#39;est pas une page</code></li>
<li>Using what you did with <code>3-redirection</code>, write <code>4-not_found_page_404</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
</ul>
        <p>File: <code>4-not_found_page_404</code></p>
