<h1>0x0E. Web stack debugging #1</h1>
<h2>Tasks</h2>
  <h3>
    0. Nginx likes port 80
  </h3>
  <p>Using your debugging skills, find out what&rsquo;s keeping your Ubuntu container&rsquo;s Nginx installation from listening on port <code>80</code>. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.</p>
<p>Requirements:</p>
<ul>
<li>Nginx must be running, and listening on port <code>80</code> of all the server&rsquo;s active IPv4 IPs </li>
<li>Write a Bash script that configures a server to the above requirements</li>
</ul>
<p>Container before debugging (I manually installed <code>curl</code> to show this example):</p>
<p>Container after debugging (I manually installed <code>curl</code> to show this example):</p>
        <p>File: <code>0-nginx_likes_port_80</code></p>
