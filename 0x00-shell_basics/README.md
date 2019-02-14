<h1>0x00. Shell, basics</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What does RTFM mean?</li>
<li>What is a Shebang</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Where am I?
  </h3>
  <p>Write a script that prints the absolute path name of the current working directory.</p>
        <p>File: <code>0-current_working_directory</code></p>
  <h3>
    1. What’s in there?
  </h3>
  <p>Display the contents list of your current directory.</p>
        <p>File: <code>1-listit</code></p>
  <h3>
    2. There is no place like home
  </h3>
  <p>Write a script that changes the working directory to the user’s home directory.</p>
<ul>
<li>You are not allowed to use any shell variables</li>
</ul>
        <p>File: <code>2-bring_me_home</code></p>
  <h3>
    3. The long format
  </h3>
  <p>Display current directory contents in a long format</p>
        <p>File: <code>3-listfiles</code></p>
  <h3>
    4. Hidden files
  </h3>
  <p>Display current directory contents, including hidden files (starting with <code>.</code>). Use the long format.</p>
        <p>File: <code>4-listmorefiles</code></p>
  <h3>
    5. I love numbers
  </h3>
  <p>Display current directory contents.</p>
<ul>
<li>Long format</li>
<li>with user and group IDs displayed numerically</li>
<li>And hidden files (starting with .)</li>
</ul>
        <p>File: <code>5-listfilesdigitonly</code></p>
  <h3>
    6. Welcome holberton
  </h3>
  <p>Create a script that creates a directory named <code>holberton</code> in the <code>/tmp/</code> directory.</p>
        <p>File: <code>6-firstdirectory</code></p>
  <h3>
    7. Betty in Holberton
  </h3>
  <p>Move the file <code>betty</code> from <code>/tmp/</code> to <code>/tmp/holberton</code>.</p>
        <p>File: <code>7-movethatfile</code></p>
  <h3>
    8. Bye bye Betty
  </h3>
  <p>Delete the file <code>betty</code>.</p>
<ul>
<li>The file <code>betty</code> is in <code>/tmp/holberton</code></li>
</ul>
        <p>File: <code>8-firstdelete</code></p>
  <h3>
    9. Bye bye Holberton
  </h3>
  <p>Delete the directory <code>holberton</code> that is in the <code>/tmp</code> directory.</p>
        <p>File: <code>9-firstdirdeletion</code></p>
  <h3>
    10. Back to the future
  </h3>
  <p>Write a script that changes the working directory to the previous one.</p>
        <p>File: <code>10-back</code></p>
  <h3>
    11. Lists
  </h3>
  <p>Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the <code>/boot</code> directory (in this order), in long format.</p>
        <p>File: <code>11-lists</code></p>
  <h3>
    12. File type
  </h3>
  <p>Write a script that prints the type of the file named <code>iamafile</code>. The file <code>iamafile</code> will be in the <code>/tmp</code> directory when we will run your script.</p>
<p>Example</p>
<p>Note that depending on the file, the output of your script will be different.</p>
        <p>File: <code>12-file_type</code></p>
  <h3>
    13. We are symbols, and inhabit symbols
  </h3>
  <p>Create a symbolic link to <code>/bin/ls</code>, named <code>__ls__</code>.
The symbolic link should be created in the current working directory. </p>
        <p>File: <code>13-symbolic_link</code></p>
  <h3>
    14. Copy HTML files
  </h3>
  <p>Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.</p>
<p>You can consider that all HTML files have the extension <code>.html</code></p>
        <p>File: <code>14-copy_html</code></p>
  <h3>
    15. Let’s move
  </h3>
  <p>Create a script that moves all files beginning with an uppercase letter to the directory <code>/tmp/u</code>.</p>
<p>You can assume that the directory <code>/tmp/u</code> will exist when we will run your script</p>
        <p>File: <code>15-lets_move</code></p>
  <h3>
    16. Clean Emacs
  </h3>
  <p>Create a script that deletes all files in the current working directory that end with the character <code>~</code>.</p>
        <p>File: <code>16-clean_emacs</code></p>
  <h3>
    17. Tree
  </h3>
  <p>Create a script that creates the directories <code>welcome/</code>, <code>welcome/to/</code> and <code>welcome/to/holberton</code> in the current directory.</p>
<p>You are only allowed to use two spaces in your script, not more.</p>
        <p>File: <code>17-tree</code></p>
  <h3>
    18. Life is a series of commas, not periods
  </h3>
  <p>Write a command that lists all the files and directories of the current directory, separated by commas (<code>,</code>).</p>
<ul>
<li>Directory names should end with a slash (<code>/</code>)</li>
<li>Files and directories starting with a dot (<code>.</code>) should be listed</li>
<li>The listing should be alpha ordered, except for the directories <code>.</code> and <code>..</code> which should be listed at the very beginning</li>
<li>Only digits and letters are used to sort; Digits should come first</li>
<li>You can assume that all the files we will test with will have at least one letter or one digit</li>
<li>The listing should end with a new line</li>
</ul>
        <p>File: <code>18-commas</code></p>
  <h3>
    19. File type: Holberton
  </h3>
  <p>Create a magic file <code>holberton.mgc</code> that can be used with the command <code>file</code> to detect <code>Holberton</code> data files. <code>Holberton</code> data files always contain the string <code>HOLBERTON</code> at offset 0.</p>
<p><strong>holberton.mgc has to be created on Ubuntu 14.04 LTS</strong></p>
        <p>File: <code>holberton.mgc</code></p>
