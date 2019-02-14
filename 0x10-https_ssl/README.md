<h1>0x10. HTTPS SSL</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is HTTPS SSL 2 main roles</li>
<li>What is the purpose encrypting traffic</li>
<li>What SSL termination means</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. HTTPS ABC
  </h3>
  <p>As for project 0x07, use numbers in your answer file.</p>
<p>What is HTTPS?</p>
<ol>
<li>A secure version of HTTP</li>
<li>A faster version of HTTP</li>
<li>A superior version of HTTP</li>
</ol>
<p>Why do you need HTTPS?</p>
<ol>
<li>To encrypt credit card and social security number information going between the client and the website servers</li>
<li>To encrypt all communication between the client and the website servers</li>
<li>To accelerate the communication between the client and the website servers</li>
</ol>
<p>You want to setup HTTPS on your website, where shall you place the certificate?</p>
<ol>
<li>In a secure location where nobody can access it</li>
<li>You can host it anywhere but you have to share the link to it on your website</li>
<li>On your website web server(s)</li>
</ol>
        <p>File: <code>0-https_abc</code></p>
  <h3>
    1. World wide web
  </h3>
  <p>Configure your domain zone so that the subdomain <code>www</code> points to your load-balancer IP (<code>lb-01</code>).
Let&rsquo;s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.</p>
<p>Requirements:</p>
<ul>
<li>Add the subdomain <code>www</code> to your domain, point it to your <code>lb-01</code> IP (your domain name might  be configured with default subdomains, feel free to remove them)</li>
<li>Add the subdomain <code>lb-01</code> to your domain, point it to your <code>lb-01</code> IP</li>
<li>Add the subdomain <code>web-01</code> to your domain, point it to your <code>web-01</code> IP</li>
<li>Add the subdomain <code>web-02</code> to your domain, point it to your <code>web-02</code> IP</li>
<li>Your Bash script must accept 2 arguments:
<ol>
<li><code>domain</code>:
<ul>
<li> type: string</li>
<li> what: domain name to audit</li>
<li>mandatory: yes</li>
</ul></li>
<li><code>subdomain</code>:
<ul>
<li>type: string</li>
<li>what: specific subdomain to audit</li>
<li>mandatory: no</li>
</ul></li>
</ol></li>
<li>Output:  <code>The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]</code></li>
<li>When only the parameter <code>domain</code> is provided, display information for its subdomains <code>www</code>, <code>lb-01</code>, <code>web-01</code> and <code>web-02</code> - in this specific order</li>
<li>When passing <code>domain</code> and <code>subdomain</code> parameters, display information for the specified subdomain</li>
<li>Ignore <code>shellcheck</code> case <code>SC2086</code></li>
<li>Must use: 
<ul>
<li><code>awk</code></li>
<li>at least one Bash function</li>
</ul></li>
<li>You do not need to handle edge cases such as:
<ul>
<li>Empty parameters </li>
<li>Nonexistent domain names</li>
<li>Nonexistent subdomains</li>
</ul></li>
</ul>
        <p>File: <code>1-world_wide_web</code></p>
  <h3>
    2. HAproxy SSL termination
  </h3>
  <p>&ldquo;Terminating SSL on HAproxy&rdquo; means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to the next hope.</p>
<p>Create a certificate using <code>certbot</code> and configure <code>HAproxy</code> to accept encrypted traffic for your subdomain <code>www.</code>.</p>
<p>Requirements:</p>
<ul>
<li>HAproxy must be listening on port TCP 443</li>
<li>HAproxy must be accepting SSL traffic</li>
<li>HAproxy must serve encrypted traffic that will return the <code>/</code> of your web server</li>
<li>When querying the root of your domain name, the page returned must contain <code>Holberton School</code></li>
<li>Share your HAproxy config as an answer file (<code>/etc/haproxy/haproxy.cfg</code>)</li>
</ul>
<p>The file <code>2-haproxy_ssl_termination</code> must be your HAproxy configuration file</p>
<p>Make sure to install HAproxy 1.5 or higher, SSL termination is not available before v1.5.</p>
        <p>File: <code>2-haproxy_ssl_termination</code></p>
  <h3>
    3. No loophole in your website traffic
  </h3>
  <p>A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.</p>
<p>Requirements:</p>
<ul>
<li>This should be transparent to the user</li>
<li>HAproxy should return a 301</li>
<li>HAproxy should redirect HTTP traffic to HTTPS</li>
<li>Share your HAproxy config as an answer file (<code>/etc/haproxy/haproxy.cfg</code>)</li>
</ul>
<p>The file <code>100-redirect_http_to_https</code> must be your HAproxy configuration file</p>
        <p>File: <code>100-redirect_http_to_https</code></p>
