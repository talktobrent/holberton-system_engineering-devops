<h1>0x04. Loops, conditions and parsing</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to create SSH keys</li>
<li>What is the advantage of using  <code>#!/usr/bin/env bash</code> over <code>#!/bin/bash</code></li>
<li>How to use <code>while</code>, <code>until</code> and <code>for</code> loops</li>
<li>How to use <code>if</code>, <code>else</code>, <code>elif</code> and <code>case</code> condition statements</li>
<li>How to use the <code>cut</code> command</li>
<li>What are files and other comparison operators, and how to use them</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Create a SSH RSA key pair
  </h3>
  <p>Read for this task:</p>
<ul>
<li>Linux and Mac OS users</li>
<li>Windows users</li>
</ul>
<p>man: <code>ssh-keygen</code></p>
<p>You will soon have to manage your own servers hosted on remote data centers. We need to set them up with your RSA public key so that you can access them via SSH.</p>
<p>Create a RSA key pair.</p>
<p>Requirements:</p>
<ul>
<li>Share your <strong>public key</strong> in your answer file <code>0-RSA_public_key.pub</code></li>
<li>Fill the <code>SSH public key</code> field of your intranet profile with the public key you just generated</li>
<li><strong>Keep the private key to yourself in a secure location</strong>, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects</li>
<li>If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase</li>
</ul>
<p>SSH and RSA keys will be covered in depth in a later project.</p>
        <p>File: <code>0-RSA_public_key.pub</code></p>
  <h3>
    1. For Holberton School loop
  </h3>
  <p>Write a Bash script that displays <code>Holberton School</code> 10 times.</p>
<p>Requirement:</p>
<ul>
<li>You must use the <code>for</code> loop (<code>while</code> and <code>until</code> are forbidden)</li>
</ul>
<p>Note that: </p>
<ul>
<li>The first line of my Bash script starts with <code>#!/usr/bin/env bash</code></li>
<li>The second line of my Bash scripts is a comment explaining what it is doing</li>
</ul>
        <p>File: <code>1-for_holberton_school</code></p>
  <h3>
    2. While Holberton School loop
  </h3>
  <p>Write a Bash script that displays <code>Holberton School</code> 10 times.</p>
<p>Requirements:</p>
<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
</ul>
        <p>File: <code>2-while_holberton_school</code></p>
  <h3>
    3. Until Holberton School loop
  </h3>
  <p>Write a Bash script that displays <code>Holberton School</code> 10 times.</p>
<p>Requirements:</p>
<ul>
<li>You must use the <code>until</code> loop (<code>for</code> and <code>while</code> are forbidden)</li>
</ul>
        <p>File: <code>3-until_holberton_school</code></p>
  <h3>
    4. If 9, say Hi!
  </h3>
  <p>Write a Bash script that displays <code>Holberton School</code> 10 times, but for the 9th iteration, displays <code>Holberton School</code> <em>and then</em> <code>Hi</code> on a new line.</p>
<p>Requirements:</p>
<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
<li>You must use the <code>if</code> statement</li>
</ul>
        <p>File: <code>4-if_9_say_hi</code></p>
  <h3>
    5. 4 bad luck, 8 is your chance
  </h3>
  <p>Write a Bash script that loops from 1 to 10 and:</p>
<ul>
<li>displays <code>bad luck</code> for the 4th loop iteration</li>
<li>displays <code>good luck</code> for the 8th loop iteration</li>
<li>displays <code>Holberton School</code> for the other iterations</li>
</ul>
<p>Requirements:</p>
<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
<li>You must use the <code>if</code>, <code>elif</code> and <code>else</code> statements</li>
</ul>
<p>For the most curious:</p>
<ul>
<li>8 in the Chinese culture</li>
<li>4 in the Chinese culture</li>
</ul>
        <p>File: <code>5-4_bad_luck_8_is_your_chance</code></p>
  <h3>
    6. Superstitious numbers
  </h3>
  <p>Write a Bash script that displays numbers from 1 to 20 and:</p>
<ul>
<li>displays <code>bad luck from China</code> for the 4th loop iteration</li>
<li>displays <code>bad luck from Japan</code> for the 9th loop iteration</li>
<li>displays <code>bad luck from Italy</code> for the 17th loop iteration</li>
</ul>
<p>Requirements:</p>
<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
<li>You must use the <code>case</code> statement</li>
</ul>
        <p>File: <code>6-superstitious_numbers</code></p>
  <h3>
    7. Clock
  </h3>
  <p>Write a Bash script that displays the time for 12 hours and 59 minutes:</p>
<ul>
<li>display hours from 0 to 12</li>
<li>display minutes from 1 to 59</li>
</ul>
<p>Requirements:</p>
<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
</ul>
<p>Note that in this example, we only display the first 70 lines using the <code>head</code> command.</p>
        <p>File: <code>7-clock</code></p>
  <h3>
    8. For ls
  </h3>
  <p>Write a Bash script that displays:</p>
<ul>
<li>The content of the current directory</li>
<li>In a list format</li>
<li>Where only the part of the name after the first dash is displayed (refer to the example)</li>
</ul>
<p>Requirements:</p>
<ul>
<li>You must use the <code>for</code> loop (<code>while</code> and <code>until</code> are forbidden)</li>
<li>Do not display hidden files</li>
</ul>
        <p>File: <code>8-for_ls</code></p>
  <h3>
    9. To file, or not to file
  </h3>
  <p>Write a Bash script that gives you information about the <code>holbertonschool</code> file.</p>
<p>Requirements:</p>
<ul>
<li>You must use <code>if</code> and, <code>else</code> (<code>case</code> is forbidden)</li>
<li>Your Bash script should check if the file exists and print:
<ul>
<li>if the file exists: <code>holbertonschool file exists</code></li>
<li>if the file does not exist: <code>holbertonschool file does not exist</code></li>
</ul></li>
<li>If the file exists, print:
<ul>
<li>if the file is empty: <code>holbertonschool file is empty</code></li>
<li>if the file is not empty: <code>holbertonschool file is not empty</code></li>
<li>if the file is a regular file: <code>holbertonschool is a regular file</code></li>
<li>if the file is not a regular file: (nothing)</li>
</ul></li>
</ul>
        <p>File: <code>9-to_file_or_not_to_file</code></p>
  <h3>
    10. FizzBuzz
  </h3>
  <p>Write a Bash script that displays numbers from 1 to 100.</p>
<p>Requirements:</p>
<ul>
<li>Displays <code>FizzBuzz</code> when the number is a multiple of 3 and 5</li>
<li>Displays <code>Fizz</code> when the number is multiple of 3</li>
<li>Displays <code>Buzz</code> when the number is a multiple of 5</li>
<li>Otherwise, displays the number</li>
<li>In a list format</li>
</ul>
        <p>File: <code>10-fizzbuzz</code></p>
  <h3>
    11. Read and cut
  </h3>
  <p>help: <code>read</code></p>
<p>Write a Bash script that displays the content of the file <code>/etc/passwd</code>.</p>
<p>Your script should only display:</p>
<ul>
<li>username</li>
<li>user id</li>
<li>Home directory path for the user</li>
</ul>
<p>Requirements:</p>
<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
</ul>
        <p>File: <code>100-read_and_cut</code></p>
  <h3>
    12. Tell the story of passwd
  </h3>
<p>Read: </p>
<ul>
<li>IFS (internal field separator)</li>
<li>Understanding /etc/passwd</li>
</ul>
<p>The file <code>/etc/passwd</code> has already been covered in a previous project and you should be familiar with it. Today we will make up a story based on it.</p>
<p>Write a Bash script that displays the content of the file <code>/etc/passwd</code>, using the <code>while</code> loop + IFS.</p>
<p>Format: <code>The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID&#39;s place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO</code></p>
<p>Requirements:</p>
<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
</ul>
        <p>File: <code>101-tell_the_story_of_passwd</code></p>
  <h3>
    13. Let&#39;s parse Apache logs
  </h3>
<p>Apache  is among the most popular web servers in the world, serving 50% of all active websites, no doubt that you will have to interact with it within your career.</p>
<p>As a Full-Stack Software Engineer, you have to master the art of parsing log files. Today we will do a simple parsing of Apache log access files.</p>
<p>Today the Customer Support department reported that a user reported that the site being &ldquo;buggy&rdquo;. Not being a detailed description, you want to have a look at the Apache logs and gather data about the traffic.</p>
<p>Write a Bash script that displays the visitor IP along with the HTTP status code from the Apache log file.</p>
<p>Requirement:</p>
<ul>
<li>Format: IP HTTP_CODE
<ul>
<li>in a list format</li>
<li>See example</li>
</ul></li>
<li>You must use <code>awk</code></li>
<li>You are not allowed to use <code>while</code>, <code>for</code>, <code>until</code> and <code>cut</code></li>
<li>Download and commit the apache-access.log file along with your answers files</li>
</ul>
        <p>File: <code>102-lets_parse_apache_logs</code></p>
  <h3>
    14. Dig the data
  </h3>
  <p>Now that you&rsquo;ve parsed the Apache log file, let&rsquo;s sort the data so you can get a better idea of what is going on.</p>
<p>Using what you did in the previous exercise, write a Bash script that groups visitors by IP and HTTP status code, and displays this data.</p>
<p>Requirements:</p>
<ul>
<li>The exact format must be: 
<ul>
<li>OCCURENCE_NUMBER IP HTTP_CODE </li>
<li>In list format</li>
</ul></li>
<li>Ordered from the greatest to the lowest number of occurrences
<ul>
<li>See example</li>
</ul></li>
<li>You must use <code>awk</code></li>
<li>You are not allowed to use <code>while</code>, <code>for</code>, <code>until</code> and <code>cut</code></li>
</ul>
        <p>File: <code>103-dig_the-data</code></p>
