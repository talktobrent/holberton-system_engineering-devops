<h1>0x0D Configuration management</h1>
<h2>Tasks</h2>
  <h3>
    0. Create a file
  </h3>
  <p>Using Puppet, create a file in <code>/tmp</code>.</p>
<p>Requirements:</p>
<ul>
<li>File path is <code>/tmp/holberton</code></li>
<li>File permission is <code>0744</code></li>
<li>File owner is <code>www-data</code></li>
<li>File group is <code>www-data</code></li>
<li>File contains <code>I love Puppet</code></li>
</ul>
        <p>File: <code>0-create_a_file.pp</code></p>
  <h3>
    1. Install a package
  </h3>
  <p>Using Puppet, install <code>puppet-lint</code>.</p>
<p>Requirements:</p>
<ul>
<li>Install <code>puppet-lint</code></li>
<li>Version must be <code>2.1.1</code></li>
</ul>
        <p>File: <code>1-install_a_package.pp</code></p>
  <h3>
    2. Execute a command
  </h3>
  <p>Using Puppet, create a manifest that kills a process named <code>killmenow</code>.</p>
<p>Requirements:</p>
<ul>
<li>Must use the <code>exec</code> Puppet resource</li>
<li>Must use <code>pkill</code> </li>
</ul>
<p>Terminal #0 - starting my process</p>
<p>Terminal #1 - executing my manifest </p>
<p>Terminal #0 - process has been terminated</p>
        <p>File: <code>2-execute_a_command.pp</code></p>
