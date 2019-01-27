<h1>0x13. Firewall</h1>
<h2>Tasks</h2>
  <h3>
    0. Firewall ABC
  </h3>
  <p>Pick one answer for every question.</p>
<p>What is a firewall?</p>
<ol>
<li>A hardware security system</li>
<li>A hardware or software security system</li>
<li>A software security system</li>
</ol>
<p>What are the 2 types of firewall:</p>
<ol>
<li>Soft and hard firewall</li>
<li>Incoming and outgoing firewall</li>
<li>Network and host-based firewall</li>
</ol>
<p>What is the main function of a firewall?</p>
<ol>
<li>To filter incoming and outgoing network traffic</li>
<li>To filter  incoming and outgoing TCP traffic</li>
<li>To  filter outgoing traffic</li>
</ol>
        <p>File: <code>0-firewall_ABC</code></p>
  <h3>
    1. Block all incoming traffic but
  </h3>
  <p>Let&rsquo;s install the <code>ufw</code> firewall and setup a few rules on <code>web-01</code>.</p>
<p>Requirements:</p>
<ul>
<li>The requirements below must be applied to <code>web-01</code> (feel free to do it on <code>lb-01</code> and <code>web-02</code>, but it won&rsquo;t be checked)</li>
<li>Configure <code>ufw</code> so that it blocks all incoming traffic, except the following TCP ports:
<ul>
<li><code>22</code> (SSH)</li>
<li><code>443</code> (HTTPS SSL)</li>
<li><code>80</code> (HTTP)</li>
</ul></li>
<li>Share the <code>ufw</code> commands that you used in your answer file</li>
</ul>
        <p>File: <code>1-block_all_incoming_traffic_but</code></p>
  <h3>
    2. Port forwarding
  </h3>
  <p>Firewalls can not only filter requests, they can also forward them.</p>
<p>Requirements:</p>
<ul>
<li>Configure <code>web-01</code> so that its firewall redirects port <code>8080/TCP</code> to port <code>80/TCP</code>.</li>
<li>Your answer file should be a copy of the <code>ufw</code> configuration file that you modified to make this happen</li>
</ul>
<p>Terminal in <code>web-01</code>:</p>
<ul>
<li>My web server <code>nginx</code> is only listening on port <code>80</code></li>
<li><code>netstat</code> shows that nothing is listening on <code>8080</code></li>
</ul>
<p>Terminal in <code>web-02</code>:</p>
<p>I use curl to query <code>web-01.holberton.online</code>, and since my firewall is forwarding the ports, I get a <code>HTTP 200</code> response on port <code>80/TCP</code> and also on port <code>8080/TCP</code>.</p>
        <p>File: <code>100-port_forwarding</code></p>
