<h1>0x08. Networking basics #1</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is localhost/127.0.0.1</li>
<li>What is 0.0.0.0</li>
<li>What is <code>/etc/hosts</code></li>
<li>How to display your machine&rsquo;s active network interfaces</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Localhost
  </h3>
  <p>What is <code>localhost</code>?</p>
<ol>
<li>A hostname that means <em>this IP</em></li>
<li>A hostname that means <em>this computer</em></li>
<li>An IP attached to a computer</li>
</ol>
        <p>File: <code>0-localhost</code></p>
  <h3>
    1. All IPs
  </h3>
  <p>What is <code>0.0.0.0</code>?</p>
<ol>
<li>All IPv4 addresses on the local machine</li>
<li>All the IPs</li>
<li>It means null in networking</li>
</ol>
        <p>File: <code>1-wildcard</code></p>
  <h3>
    2. Change your home IP
  </h3>
  <p>Write a Bash script that configures an Ubuntu server with the below requirements.</p>
<p>Requirements:</p>
<ul>
<li><code>localhost</code> resolves to <code>127.0.0.2</code></li>
<li> <code>facebook.com</code> resolves to <code>8.8.8.8</code>.</li>
<li> The checker is running on Docker, so make sure to read this</li>
</ul>
<p>In this example we can see that:</p>
<ul>
<li>before running the script, <code>localhost</code> resolves to <code>127.0.0.1</code> and <code>facebook.com</code> resolves to <code>157.240.11.35</code></li>
<li>after running the script,  <code>localhost</code> resolves to <code>127.0.0.2</code> and <code>facebook.com</code> resolves to <code>8.8.8.8</code></li>
</ul>
<p>If you&rsquo;re running this script on a machine that you&rsquo;ll continue to use, be sure to revert <code>localhost</code> to <code>127.0.0.1</code>. Otherwise, a lot of things will stop working!</p>
        <p>File: <code>2-change_your_home_IP</code></p>
  <h3>
    3. Show attached IPs
  </h3>
  <p>Write a Bash script that displays all active IPv4 IPs on the machine it&rsquo;s executed on.</p>
<p>Obviously, the IPs displayed may be different depending on which machine you are running the script on.</p>
<p>Note that we can see our <code>localhost</code> IP :)</p>
        <p>File: <code>3-show_attached_IPs</code></p>
  <h3>
    4. Port listening on localhost
  </h3>
  <p>Write a Bash script that listens on port <code>98</code> on <code>localhost</code>.</p>
<p><strong>Terminal 0</strong></p>
<p>Starting my script.</p>
<p><strong>Terminal 1</strong></p>
<p>Connecting to <code>localhost</code> on port <code>98</code> using <code>telnet</code> and typing some text.</p>
<p><strong>Terminal 0</strong></p>
<p>Receiving the text on the other side.</p>
<p>For the sake of the exercise, this connection is made entirely within <code>localhost</code>. This isn&rsquo;t really exciting as is, but we can use this script across networks as well. Try running it between your local PC and your remote server for fun!</p>
<p>As you can see, this can come in very handy in a multitude of situations. Maybe you&rsquo;re debugging socket connection issues, or you&rsquo;re trying to connect to a software and you are unsure if the issue is the software or the network, or you&rsquo;re working on firewall rules&hellip; Another tool to add to your debugging toolbox!</p>
        <p>File: <code>4-port_listening_on_localhost</code></p>
