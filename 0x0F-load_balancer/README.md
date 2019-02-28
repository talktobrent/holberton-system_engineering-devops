<h1>0x0F. Load balancer</h1>
<h2>Tasks</h2>
  <h3>
    0. Double the number of webservers
  </h3>
  <p>In this first task you need to configure <code>web-02</code> to be identical to <code>web-01</code>. Fortunately, you built a Bash script during your web server project, and they&rsquo;ll now come in handy to easily configure <code>web-02</code>. Remember, always try to automate your work!</p>
<p>Since we&rsquo;re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.</p>
<p>Requirements:</p>
<ul>
<li>Configure Nginx so that its HTTP response contains a custom header (on <code>web-01</code> and <code>web-02</code>)
<ul>
<li>The name of the custom HTTP header must be <code>X-Served-By</code></li>
<li>The value of the custom HTTP header must be the hostname of the server Nginx is running on</li>
</ul></li>
<li>Write <code>0-custom_http_response-header</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task
<ul>
<li>Ignore SC2154 for <code>shellcheck</code></li>
</ul></li>
</ul>
<p>If your server&rsquo;s hostnames are not properly configured, follow this tutorial.</p>
        <p>File: <code>0-custom_http_response-header</code></p>
  <h3>
    1. Install your load balancer
  </h3>
  <p>Install and configure HAproxy on your <code>lb-01</code> server.</p>
<p>Requirements:</p>
<ul>
<li>Configure HAproxy with version equal or greater than 1.5 so that it send traffic to <code>web-01</code> and <code>web-02</code></li>
<li>Distribute requests using a roundrobin algorithm</li>
<li>Make sure that HAproxy can be managed via an init script</li>
<li>Make sure that your servers are configured with the right hostnames: <code>[STUDENT_ID]-web-01</code> and <code>[STUDENT_ID]-web-02</code>. If not, follow this tutorial.</li>
<li>For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements</li>
</ul>
        <p>File: <code>1-install_load_balancer</code></p>
