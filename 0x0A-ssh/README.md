<h1>0x0A. SSH</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a server</li>
<li>Where servers usually live</li>
<li>What is SSH</li>
<li>How to create an SSH RSA key pair</li>
<li>How to connect to a remote host using an SSH RSA key pair</li>
<li>The advantage of using  <code>#!/usr/bin/env bash</code> instead of <code>/bin/bash</code> </li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Use a private key
  </h3>
  <p>Write a Bash script that uses <code>ssh</code> to connect to your server using the private key <code>~/.ssh/holberton</code> with the user <code>ubuntu</code>.</p>
<p>Requirements:</p>
<ul>
<li>Only use <code>ssh</code> single-character flags</li>
<li>You cannot use <code>-l</code></li>
<li>You do not need to handle the case of a private key protected by a passphrase</li>
</ul>
        <p>File: <code>0-use_a_private_key</code></p>
  <h3>
    1. Create an SSH key pair
  </h3>
  <p>Write a Bash script that creates an RSA key pair.</p>
<p>Requirements:</p>
<ul>
<li>Name of the created private key must be <code>holberton</code></li>
<li>Number of bits in the created key to be created 4096</li>
<li>The created key must be protected by the passphrase <code>betty</code></li>
</ul>
        <p>File: <code>1-create_ssh_key_pair</code></p>
  <h3>
    2. Client configuration file
  </h3>
  <p>Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let&rsquo;s configure it to our needs so that you can connect to a server without typing a password.
Share your SSH client configuration in your answer file.</p>
<p>Requirements:</p>
<ul>
<li>Your SSH client configuration must be configured to use the private key <code>~/.ssh/holberton</code></li>
<li>Your SSH client configuration must be configured to refuse to authenticate using a password</li>
</ul>
<p>In the example above, we can see that <code>ssh</code> tries to authenticate using <code>holberton</code> and does not try to authenticate using a password. You can replace <code>98.98.98.98</code> by the IP of your server for testing purposes.</p>
        <p>File: <code>2-ssh_config</code></p>
  <h3>
    3. Let me in!
  </h3>
  <p>Now that you have successfully connected to your server, we would also like to join the party.</p>
<p>Add the SSH public key below to your server so that we can connect using the <code>ubuntu</code> user.</p>
