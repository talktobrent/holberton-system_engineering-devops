<h1>0x0C. Web stack debugging #0</h1>
<h2>Tasks</h2>
  <h3>
    0. Give me a page!
  </h3>
  <p>Be sure to read the Docker concept page.</p>
<p>In this first debugging project, you will need to get Apache to run on the container and to return a page containing <code>Hello Holberton</code> when querying the root of it.</p>
<p>Here we can see that after starting my Docker container, I <code>curl</code> the port <code>8080</code> mapped to the Docker container port <code>80</code>, it does not return a page but an error message. Note that you might also get the error message <code>curl: (52) Empty reply from server</code>.</p>
<p>After connecting to the container and fixing whatever needed to be fixed (here is your mission), you can see that curling port 80 return a page that contains <code>Hello Holberton</code>.
Paste the command(s) you used to fix the issue in your answer file.</p>
        <p>File: <code>0-give_me_a_page</code></p>
