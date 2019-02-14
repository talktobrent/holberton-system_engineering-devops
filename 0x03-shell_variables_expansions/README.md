<h1>0x03. Shell, init files, variables and expansions</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What happens when you type <code>$ ls -l *.txt</code></li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. &lt;o&gt;
  </h3>
  <p>Create a script that creates an alias.</p>
<ul>
<li>Name: <code>ls</code></li>
<li>Value: <code>rm *</code></li>
</ul>
        <p>File: <code>0-alias </code></p>
  <h3>
    1. Hello you
  </h3>
  <p>Create a script that prints <code>hello user</code>, where user is the current Linux user.</p>
        <p>File: <code>1-hello_you </code></p>
  <h3>
    2. The path to success is to take massive, determined action
  </h3>
  <p>Add <code>/action</code> to the <code>PATH</code>.
<code>/action</code> should be the last directory the shell looks into when looking for a program.</p>
        <p>File: <code>2-path</code></p>
  <h3>
    3. If the path be beautiful, let us not ask where it leads
  </h3>
  <p>Create a script that counts the number of directories in the <code>PATH</code>.</p>
        <p>File: <code>3-paths</code></p>
  <h3>
    4. Global variables
  </h3>
  <p>Create a script that lists environment variables.</p>
        <p>File: <code>4-global_variables</code></p>
  <h3>
    5. Local variables
  </h3>
  <p>Create a script that lists all local variables and environment variables, and functions.</p>
        <p>File: <code>5-local_variables</code></p>
  <h3>
    6. Local variable
  </h3>
  <p>Create a script that creates a new local variable.</p>
<ul>
<li>Name: <code>BETTY</code></li>
<li>Value: <code>Holberton</code></li>
</ul>
        <p>File: <code>6-create_local_variable</code></p>
  <h3>
    7. Global variable
  </h3>
  <p>Create a script that creates a new global variable.</p>
<ul>
<li>Name: <code>HOLBERTON</code></li>
<li>Value: <code>Betty</code></li>
</ul>
        <p>File: <code>7-create_global_variable</code></p>
  <h3>
    8. Every addition to true knowledge is an addition to human power
  </h3>
  <p>Write a script that prints the result of the addition of 128 with the value stored in the environment variable <code>TRUEKNOWLEDGE</code>, followed by a new line.</p>
        <p>File: <code>8-true_knowledge</code></p>
  <h3>
    9. Divide and rule
  </h3>
  <p>Write a script that prints the result of <code>POWER</code> divided by <code>DIVIDE</code>, followed by a new line.</p>
<ul>
<li><code>POWER</code> and <code>DIVIDE</code> are environment variables</li>
</ul>
        <p>File: <code>9-divide_and_rule</code></p>
  <h3>
    10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath
  </h3>
  <p>Write a script that displays the result of <code>BREATH</code> to the power <code>LOVE</code></p>
<ul>
<li><code>BREATH</code> and <code>LOVE</code> are environment variables</li>
<li>The script should display the result, followed by a new line</li>
</ul>
        <p>File: <code>10-love_exponent_breath</code></p>
  <h3>
    11. There are 10 types of people in the world -- Those who understand binary, and those who don&#39;t
  </h3>
  <p>Write a script that converts a number from base 2 to base 10.</p>
<ul>
<li>The number in base 2 is stored in the environment variable <code>BINARY</code></li>
<li>The script should display the number in base 10, followed by a new line</li>
</ul>
        <p>File: <code>11-binary_to_decimal</code></p>
  <h3>
    12. Combination
  </h3>
  <p>Create a script that prints all possible combinations of two letters, except <code>oo</code>.</p>
<ul>
<li>Letters are lower cases, from <code>a</code> to <code>z</code></li>
<li>One combination per line</li>
<li>The output should be alpha ordered, starting with <code>aa</code></li>
<li>Do not print <code>oo</code></li>
<li>Your script file should contain maximum 64 characters</li>
</ul>
        <p>File: <code>12-combinations</code></p>
  <h3>
    13. Floats
  </h3>
  <p>Write a script that prints a number with two decimal places.</p>
<p>The number will be stored in the environment variable <code>NUM</code>.</p>
        <p>File: <code>13-print_float</code></p>
  <h3>
    14. Decimal to Hexadecimal
  </h3>
  <p>Write a script that converts a number from base 10 to base 16.</p>
<ul>
<li>The number in base 10 is stored in the environment variable <code>DECIMAL</code></li>
<li>The script should display the number in base 16, followed by a new line</li>
</ul>
        <p>File: <code>14-decimal_to_hexadecimal</code></p>
  <h3>
    15. What happens when you type ls *.c
  </h3>
  <p>Write a blog post describing step by step what happens when you type <code>ls *.c</code> and hit Enter in your shell.
Try to explain every step you know of, and give examples. A total beginner should understand what you have written.</p>
<ul>
<li>Have at least one picture, at the top of the blog post</li>
<li>Publish your blog post on Medium or LinkedIn</li>
<li>Share your blog post at least on Twitter and LinkedIn</li>
<li>Write professionally and intelligibly </li>
</ul>
  <h3>
    16. What is the difference between a hard link and a symbolic link?
  </h3>
  <p>Write a blog post explaining what are hard and symbolic links on Linux, how to create them, and what is the difference between the two. Use examples to illustrate.</p>
<ul>
<li>Have at least one picture, at the top of the blog post</li>
<li>Publish your blog post on Medium or LinkedIn</li>
<li>Share your blog post at least on Twitter and LinkedIn</li>
</ul>
  <h3>
    17. Everyone is a proponent of strong encryption
  </h3>
  <p>Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.</p>
        <p>File: <code>100-rot13</code></p>
  <h3>
    18. The eggs of the brood need to be an odd number
  </h3>
  <p>Write a script that prints every other line from the input, starting with the first line.</p>
        <p>File: <code>101-odd</code></p>
  <h3>
    19. I&#39;m an instant star. Just add water and stir.
  </h3>
  <p>Write a shell script that adds the two numbers stored in the environment variables <code>WATER</code>  and <code>STIR</code>  and prints the result.</p>
<ul>
<li><code>WATER</code>  is in base <code>water</code></li>
<li><code>STIR</code>  is in base <code>stir.</code></li>
<li>The result should be in base <code>behlnort</code></li>
</ul>
        <p>File: <code>102-water_and_stir</code></p>
