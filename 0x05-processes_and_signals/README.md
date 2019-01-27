<h1>0x05. Processes and signals</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a PID</li>
<li>What is a process</li>
<li>How to find a process&rsquo; PID</li>
<li>How to kill a process</li>
<li>What is a signal</li>
<li>What are the 2 signals that cannot be ignored</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. What is my PID
  </h3>
  <p>Write a Bash script that displays its own PID.</p>
        <p>File: <code>0-what-is-my-pid</code></p>
  <h3>
    1. List your processes
  </h3>
  <p>Write a Bash script that displays a list of currently running processes.</p>
<p>Requirements:</p>
<ul>
<li>Must show all processes, for all users, including those which might not have a TTY</li>
<li>Display in a user-oriented format</li>
<li>Show process hierarchy</li>
</ul>
        <p>File: <code>1-list_your_processes</code></p>
  <h3>
    2. Show your Bash PID
  </h3>
  <p>Using your previous exercise command, write a Bash script that displays line containing the <code>bash</code> word, thus allowing you to easily get the PID of your Bash process</p>
<p>Requirements:</p>
<ul>
<li>You cannot use <code>pgrep</code></li>
<li>The third line of your script must be <code># shellcheck disable=SC2009</code> (for more info about ignoring <code>shellcheck</code> error here)</li>
</ul>
<p>Here we can see that my Bash PID is <code>4404</code>.</p>
        <p>File: <code>2-show_your_bash_pid</code></p>
  <h3>
    3. Show your Bash PID made easy
  </h3>
  <p>Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word <code>bash</code>.</p>
<p>Requirements:</p>
<ul>
<li>You cannot use <code>ps</code></li>
</ul>
<p>Here we can see that: </p>
<ul>
<li>For the first iteration: <code>bash</code> PID is <code>4404</code> and that the <code>3-show_your_bash_pid_made_easy</code> script PID is <code>4555</code></li>
<li>For the second iteration: <code>bash</code> PID is <code>4404</code> and that the <code>3-show_your_bash_pid_made_easy</code> script PID is <code>4557</code></li>
</ul>
        <p>File: <code>3-show_your_bash_pid_made_easy</code></p>
  <h3>
    4. To infinity and beyond
  </h3>
  <p>Write a Bash script that displays <code>To infinity and beyond</code> indefinitely. </p>
<p>Requirements:</p>
<ul>
<li>In between each iteration of the loop, add a <code>sleep 2</code></li>
</ul>
<p>Note that I <code>ctrl+c</code> (killed) the Bash script in the example.</p>
        <p>File: <code>4-to_infinity_and_beyond</code></p>
  <h3>
    5. Kill me now
  </h3>
  <p>We killed our <code>4-to_infinity_and_beyond</code> process using <code>ctrl+c</code> in the previous task, there is actually another way to do this.</p>
<p>Write a Bash script that kills <code>4-to_infinity_and_beyond</code> process.</p>
<p>Requirements:</p>
<ul>
<li>You must use <code>kill</code></li>
</ul>
<p>Terminal #0</p>
<p>Terminal #1</p>
<p>I opened 2 terminals in this example, started by running my <code>4-to_infinity_and_beyond</code> Bash script in terminal #0 and then moved on terminal #1 to run <code>5-kill_me_now</code>. We can then see in terminal #0 that my process has been terminated.</p>
        <p>File: <code>5-kill_me_now</code></p>
  <h3>
    6. Kill me now made easy
  </h3>
  <p>Write a Bash script that kills <code>4-to_infinity_and_beyond</code> process.</p>
<p>Requirements:</p>
<ul>
<li>You cannot use <code>kill</code> or <code>killall</code></li>
</ul>
<p>Terminal #0</p>
<p>Terminal #1</p>
<p>I opened 2 terminals in this example, started by running my <code>4-to_infinity_and_beyond</code> Bash script in terminal #0 and then moved on terminal #1 to run <code>6-kill_me_now_made_easy</code>. We can then see in terminal #0 that my process has been terminated.</p>
        <p>File: <code>6-kill_me_now_made_easy</code></p>
  <h3>
    7. Highlander
  </h3>
  <p>Write a Bash script that displays: </p>
<ul>
<li><code>To infinity and beyond</code> indefinitely</li>
<li>With a <code>sleep 2</code> in between each iteration</li>
<li><code>I am invincible!!!</code> when receiving a <code>SIGTERM</code> signal</li>
</ul>
<p>Make a copy of your <code>6-kill_me_now_made_easy</code> script, name it <code>67-kill_me_now_made_easy</code>,  that kills the <code>7-highlander</code> process instead of the <code>4-to_infinity_and_beyond</code> one.</p>
<p>Terminal #0</p>
<p>Terminal #1</p>
<p>I started <code>7-highlander</code> in Terminal #0 and then run <code>67-kill_me_now_made_easy</code> in terminal #1, for every iteration we can see <code>I am invincible!!!</code> appearing in terminal #0.</p>
        <p>File: <code>7-highlander</code></p>
  <h3>
    8. Beheaded process
  </h3>
  <p>Write a Bash script that kills the process <code>7-highlander</code>.</p>
<p>Terminal #0</p>
<p>Terminal #1</p>
<p>I started <code>7-highlander</code> in Terminal #0 and then run <code>8-beheaded_process</code> in terminal #1 and we can see that the <code>7-highlander</code> has been killed.</p>
        <p>File: <code>8-beheaded_process</code></p>
