<h1>0x02. Shell, I/O Redirections and filters</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>Shell, I/O Redirection</h3>

<ul>
<li>What do the commands <code>head</code>, <code>tail</code>, <code>find</code>, <code>wc</code>, <code>sort</code>, <code>uniq</code>, <code>grep</code>, <code>tr</code> do</li>
<li>How to redirect standard output to a file</li>
<li>How to get standard input from a file instead of the keyboard</li>
<li>How to send the output from one program to the input of another program</li>
<li>How to combine commands and filters with redirections</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Hello World
  </h3>
  <p>Write a script that prints “Hello, World”, followed by a new line to the standard output.</p>
        <p>File: <code>0-hello_world</code></p>
  <h3>
    1. Confused smiley
  </h3>
  <p>Write a script that displays a confused smiley <code>&quot;(Ôo)&#39;</code>.</p>
        <p>File: <code>1-confused_smiley </code></p>
  <h3>
    2. Let&#39;s display a file
  </h3>
  <p>Display the content of the <code>/etc/passwd</code> file.</p>
        <p>File: <code>2-hellofile</code></p>
  <h3>
    3. What about 2?
  </h3>
  <p>Display the content of <code>/etc/passwd</code> and <code>/etc/hosts</code></p>
        <p>File: <code>3-twofiles</code></p>
  <h3>
    4. Last lines of a file
  </h3>
  <p>Display the last 10 lines of <code>/etc/passwd</code></p>
<p>Tips from Dora Korpar (Cohort 0 San Francisco): &ldquo;Thinks of it as a cat, what is at the end of it?&rdquo;</p>
        <p>File: <code>4-lastlines</code></p>
  <h3>
    5. I&#39;d prefer the first ones actually
  </h3>
  <p>Display the first 10 lines of <code>/etc/passwd</code></p>
        <p>File: <code>5-firstlines</code></p>
  <h3>
    6. Line #2
  </h3>
  <p>Write a script that displays the third line of the file <code>iacta</code>.</p>
<p>The file <code>iacta</code> will be in the working directory</p>
<ul>
<li>You&rsquo;re not allowed to use <code>sed</code></li>
</ul>
<p>Note: The output will differ, depending on the content of the file <code>iacta</code>.</p>
        <p>File: <code>6-third_line</code></p>
  <h3>
    7. It is a good file that cuts iron without making a noise
  </h3>
  <p>Write a shell script that creates a file named exactly <code>\*\\&#39;&quot;Holberton School&quot;\&#39;\\*$\?\*\*\*\*\*:)</code> containing the text <code>Holberton School</code>  ending by a new line.</p>
        <p>File: <code>7-file</code></p>
  <h3>
    8. Save current state of directory
  </h3>
  <p>Write a script that writes into the file <code>ls_cwd_content</code> the result of the command <code>ls -la</code>. If the file <code>ls_cwd_content</code> already exists, it should be overwritten. If the file <code>ls_cwd_content</code> does not exist, create it.</p>
        <p>File: <code>8-cwd_state </code></p>
  <h3>
    9. Duplicate last line
  </h3>
  <p>Write a script that duplicates the last line of the file <code>iacta</code></p>
<ul>
<li>The file <code>iacta</code> will be in the working directory</li>
</ul>
        <p>File: <code>9-duplicate_last_line </code></p>
  <h3>
    10. No more javascript
  </h3>
  <p>Write a script that deletes all the regular files (not the directories) with a <code>.js</code> extension that are present in the current directory and all its subfolders.</p>
        <p>File: <code>10-no_more_js </code></p>
  <h3>
    11. Don&#39;t just count your directories, make your directories count
  </h3>
  <p>Write a script that counts the number of directories and sub-directories in the current directory.</p>
<ul>
<li>The current and parent directories should not be taken into account</li>
<li>Hidden directories should be counted</li>
</ul>
        <p>File: <code>11-directories</code></p>
  <h3>
    12. What’s new
  </h3>
  <p>Create a script that displays the 10 newest files in the current directory.</p>
<p>Requirements:</p>
<ul>
<li>One file per line</li>
<li>Sorted from the newest to the oldest</li>
</ul>
        <p>File: <code>12-newest_files</code></p>
  <h3>
    13. Being unique is better than being perfect
  </h3>
  <p>Create a script that takes a list of words as input and prints only words that appear exactly once.</p>
<ul>
<li>Input format: One line, one word</li>
<li>Output format: One line, one word</li>
<li>Words should be sorted</li>
</ul>
        <p>File: <code>13-unique</code></p>
  <h3>
    14. It must be in that file
  </h3>
  <p>Display lines containing the pattern &ldquo;root&rdquo; from the file <code>/etc/passwd</code></p>
        <p>File: <code>14-findthatword</code></p>
  <h3>
    15. Count that word
  </h3>
  <p>Display the number of lines that contain the pattern &ldquo;bin&rdquo; in the file <code>/etc/passwd</code></p>
        <p>File: <code>15-countthatword</code></p>
  <h3>
    16. What&#39;s next?
  </h3>
  <p>Display lines containing the pattern &ldquo;root&rdquo; and 3 lines after them in the file <code>/etc/passwd</code>.</p>
        <p>File: <code>16-whatsnext</code></p>
  <h3>
    17. I hate bins
  </h3>
  <p>Display all the lines in the file <code>/etc/passwd</code> that do not contain the pattern &ldquo;bin&rdquo;.</p>
        <p>File: <code>17-hidethisword</code></p>
  <h3>
    18. Letters only please
  </h3>
  <p>Display all lines of the file <code>/etc/ssh/sshd_config</code> starting with a letter.</p>
<ul>
<li>include capital letters as well</li>
</ul>
        <p>File: <code>18-letteronly</code></p>
  <h3>
    19. A to Z
  </h3>
  <p>Replace all characters <code>A</code> and <code>c</code> from input to <code>Z</code> and <code>e</code> respectively.</p>
        <p>File: <code>19-AZ </code></p>
  <h3>
    20. Without C, you would live in hiago
  </h3>
  <p>Create a script that removes all letters <code>c</code> and <code>C</code> from input.</p>
        <p>File: <code>20-hiago </code></p>
  <h3>
    21. esreveR
  </h3>
  <p>Write a script that reverse its input.</p>
        <p>File: <code>21-reverse </code></p>
  <h3>
    22. DJ Cut Killer
  </h3>
  <p>Write a script that displays all users and their home directories, sorted by users.</p>
<ul>
<li>Based on the the <code>/etc/passwd</code> file</li>
</ul>
        <p>File: <code>22-users_and_homes</code></p>
  <h3>
    23. Empty casks make the most noise
  </h3>
  <p>Write a command that finds all empty files and directories in the current directory and all sub-directories.</p>
<ul>
<li>Only the names of the files and directories should be displayed (not the entire path)</li>
<li>Hidden files should be listed</li>
<li>One file name per line</li>
<li>The listing should end with a new line</li>
<li>You are not allowed to use <code>basename</code>, <code>grep</code>, <code>egrep</code>, <code>fgrep</code> or <code>rgrep</code></li>
</ul>
        <p>File: <code>100-empty_casks</code></p>
  <h3>
    24. A gif is worth ten thousand words
  </h3>
  <p>Write a script that lists all the files with a <code>.gif</code> extension in the current directory and all its sub-directories.</p>
<ul>
<li>Hidden files should be listed</li>
<li>Only regular files (not directories) should be listed</li>
<li>The names of the files should be displayed without their extensions</li>
<li>The files should be sorted by byte values, but case-insensitive (file <code>aaa</code> should be listed before file <code>bbb</code>, file <code>.b</code> should be listed before file <code>a</code>, and file <code>Rona</code> should be listed after file <code>jay</code>) </li>
<li>One file name per line</li>
<li>The listing should end with a new line</li>
<li>You are not allowed to use <code>basename</code>, <code>grep</code>, <code>egrep</code>, <code>fgrep</code> or <code>rgrep</code></li>
</ul>
        <p>File: <code>101-gifs</code></p>
  <h3>
    25. Acrostic
  </h3>
  <p>An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval. Read more.</p>
<p>Create a script that decodes acrostics that use the first letter of each line.</p>
<ul>
<li>The ‘decoded’ message has to end with a new line</li>
<li>You are not allowed to use <code>grep</code>, <code>egrep</code>, <code>fgrep</code> or <code>rgrep</code></li>
</ul>
        <p>File: <code>102-acrostic</code></p>
  <h3>
    26. The biggest fan
  </h3>
  <p>Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.</p>
<ul>
<li>Order by number of requests, most active host or IP at the top</li>
<li>You are not allowed to use <code>grep</code>, <code>egrep</code>, <code>fgrep</code> or <code>rgrep</code></li>
</ul>
<p>Format:</p>
<p>Here is an example with one day of logs of the NASA website (1995).</p>
        <p>File: <code>103-the_biggest_fan</code></p>
