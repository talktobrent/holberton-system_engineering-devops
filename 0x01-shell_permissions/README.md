<h1>0x01. Shell, permissions</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>Permissions</h3>

<ul>
<li>What do the commands <code>chmod</code>, <code>sudo</code>, <code>su</code>, <code>chown</code>, <code>chgrp</code> do</li>
<li>Linux file permissions</li>
<li>How to represent each of the three sets of permissions (owner, group, and other) as a single digit</li>
<li>How to change permissions, owner and group of a file</li>
<li>Why can&rsquo;t a normal user <code>chown</code> a file</li>
<li>How to run a command with root privileges</li>
<li>How to change user ID or become superuser<br></li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. My name is Betty
  </h3>
  <p>Create a script that changes your user ID to <code>betty</code>.</p>
<ul>
<li>You should use exactly 8 characters for your command (+1 character for the new line)</li>
<li>You can assume that the user <code>betty</code> will exist when we will run your script</li>
</ul>
        <p>File: <code>0-iam_betty</code></p>
  <h3>
    1. Who am I
  </h3>
  <p>Write a script that prints the effective userid of the current user.</p>
        <p>File: <code>1-who_am_i</code></p>
  <h3>
    2. Groups
  </h3>
  <p>Write a script that prints all the groups the current user is part of.</p>
<p>Note: depending on the user, you will get a different output.</p>
        <p>File: <code>2-groups</code></p>
  <h3>
    3. New owner
  </h3>
  <p>Write a script that changes the owner of the file <code>hello</code> to the user <code>betty</code>.</p>
        <p>File: <code>3-new_owner </code></p>
  <h3>
    4. Empty!
  </h3>
  <p>Write a script that creates an empty file called <code>hello</code>.</p>
        <p>File: <code>4-empty</code></p>
  <h3>
    5. Execute
  </h3>
  <p>Write a script that adds execute permission to the owner of the file <code>hello</code>.</p>
<ul>
<li>The file <code>hello</code> will be in the working directory</li>
</ul>
        <p>File: <code>5-execute</code></p>
  <h3>
    6. Multiple permissions
  </h3>
  <p>Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file <code>hello</code>.</p>
<ul>
<li>The file <code>hello</code> will be in the working directory</li>
</ul>
        <p>File: <code>6-multiple_permissions</code></p>
  <h3>
    7. Everybody!
  </h3>
  <p>Write a script that adds execution permission to the owner, the group owner and the other users, to the file <code>hello</code></p>
<ul>
<li>The file <code>hello</code> will be in the working directory</li>
<li>You are not allowed to use commas for this script</li>
</ul>
        <p>File: <code>7-everybody</code></p>
  <h3>
    8. James Bond
  </h3>
  <p>Write a script that sets the permission to the file <code>hello</code> as follows:</p>
<ul>
<li>Owner: no permission at all</li>
<li>Group: no permission at all</li>
<li>Other users: all the permissions</li>
</ul>
<p>The file <code>hello</code> will be in the working directory
You are not allowed to use commas for this script</p>
        <p>File: <code>8-James_Bond</code></p>
  <h3>
    9. John Doe
  </h3>
  <p>Write a script that sets the mode of the file <code>hello</code> to this:</p>
<ul>
<li>The file <code>hello</code> will be in the working directory</li>
<li>You are not allowed to use commas for this script</li>
</ul>
        <p>File: <code>9-John_Doe</code></p>
  <h3>
    10. Look in the mirror
  </h3>
  <p>Write a script that sets the mode of the file <code>hello</code> the same as <code>olleh</code>’s mode.</p>
<ul>
<li>The file <code>hello</code> will be in the working directory</li>
<li>The file <code>olleh</code> will be in the working directory</li>
</ul>
<p>Note: the mode of <code>olleh</code> will not always be 664. Make sure your script works for any mode.</p>
        <p>File: <code>10-mirror_permissions</code></p>
  <h3>
    11. Directories
  </h3>
  <p>Create a script that adds execute permission to all subdirectories of the current directory for  the owner, the group owner and all other users. Regular files should not be changed.</p>
        <p>File: <code>11-directories_permissions</code></p>
  <h3>
    12. More directories
  </h3>
  <p>Create a script that creates a directory called <code>dir_holberton</code> with permissions 751 in the working directory.</p>
        <p>File: <code>12-directory_permissions</code></p>
  <h3>
    13. Change group
  </h3>
  <p>Write a script that changes the group owner to <code>holberton</code> for the file <code>hello</code></p>
<ul>
<li>The file <code>hello</code> will be in the working directory</li>
</ul>
        <p>File: <code>13-change_group</code></p>
  <h3>
    14. Owner and group
  </h3>
  <p>Write a script that changes the owner to <code>betty</code> and the group owner to <code>holberton</code> for all the files and directories in the working directory.</p>
        <p>File: <code>14-change_owner_and_group</code></p>
  <h3>
    15. Symbolic links
  </h3>
  <p>Write a script that changes the owner and the group owner of the file <code>_hello</code> to <code>betty</code> and <code>holberton</code> respectively.</p>
<ul>
<li>The file <code>_hello</code> is in the working directory</li>
<li>The file <code>_hello</code> is a symbolic link</li>
</ul>
        <p>File: <code>15-symbolic_link_permissions</code></p>
  <h3>
    16. If only
  </h3>
  <p>Write a script that changes the owner of the file <code>hello</code> to <code>betty</code> only if it is owned by the user <code>guillaume</code>.</p>
<ul>
<li>The file <code>hello</code> will be in the working directory</li>
</ul>
        <p>File: <code>16-if_only </code></p>
  <h3>
    17. Star Wars
  </h3>
  <p>Write a script that will play the StarWars IV episode in the terminal.</p>
        <p>File: <code>100-Star_Wars</code></p>
  <h3>
    18. RTFM
  </h3>
  <p>Create a man page that looks exactly like this one and passes all checks.</p>
<p><em>NOTE:</em> A new line is not necessary at the end of this file, refer to the output of <code>wc</code>, as shown below.</p>
        <p>File: <code>101-man_holberton</code></p>
