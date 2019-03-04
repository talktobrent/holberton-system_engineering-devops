<h1>0x1A. Application server</h1>
<h2>Tasks</h2>
  <h3>
    0. Welcome Gunicorn
  </h3>
  <p>Let&rsquo;s serve what you built for AirBnB clone v2 - Web framework on <code>web01</code>.</p>
<p>Requirements:</p>
<ul>
<li>Git clone your <code>AirBnB_clone_v2</code></li>
<li>Install <code>Gunicorn</code> and other libraries required by your application</li>
<li>Create an <code>Upstart</code> script that starts a <code>Gunicorn</code> instance to serve <code>web_flask/0-hello_route.py</code> from your <code>AirBnB_clone_v2</code></li>
<li>Setup <code>Nginx</code> so that the route <code>/airbnb-onepage/</code> points to your <code>Gunicorn</code> instance</li>
<li><code>Nginx</code> must serve this page both locally and on its public IP on port <code>80</code></li>
<li>Upload your <code>Upstart</code> config file as <code>0-welcome_gunicorn-upstart_config</code></li>
<li>Upload your <code>Nginx</code> config file as <code>0-welcome_gunicorn-nginx_config</code></li>
</ul>
<p>Do not forget that logs are your friends! (E.g. <code>Nginx</code>&lsquo;s logs are located in <code>/var/log/nginx</code>)
Also <code>init-checkconf</code> is great for checking your <code>Upstart</code> config files.</p>
<p>Above I start my <code>Upstart</code> service <code>airbnb-onepage</code> (meaning that I have a Upstart config <code>/etc/init/airbnb-onepage.conf</code>) which will start my <code>Gunicorn</code> application server. I then <code>curl</code> my <code>Gunicorn</code> server on port <code>8000</code> (but you can choose whichever port number you want), and then I <code>curl</code> my Nginx server.</p>
        <p>File: <code>0-welcome_gunicorn-upstart_config, 0-welcome_gunicorn-nginx_config</code></p>
  <h3>
    1. Pass a query parameter
  </h3>
  <p>Let&rsquo;s serve what you built for AirBnB clone v2 - Web framework on <code>web01</code>.</p>
<p>Requirements:</p>
<ul>
<li>Create an <code>Upstart</code> script that starts a <code>Gunicorn</code> instance to serve <code>web_flask/6-number_odd_or_even.py</code> from your <code>AirBnB_clone_v2</code></li>
<li>Setup <code>Nginx</code> so that the route<code>/airbnb-dynamic/</code> points to your <code>Gunicorn</code> instance</li>
<li><code>Nginx</code> must serve this page both locally and on its public IP on port <code>80</code></li>
<li>Upload your <code>Upstart</code> config file as <code>1-pass_parameter-upstart_config</code></li>
<li>Upload your <code>Nginx</code> config file as <code>1-pass_parameter-nginx_config</code></li>
</ul>
        <p>File: <code>1-pass_parameter-upstart_config, 1-pass_parameter-nginx_config</code></p>
  <h3>
    2. Let&#39;s do this for your API
  </h3>
  <p>Let&rsquo;s serve what you built for AirBnB clone v3 - RESTful API on <code>web01</code>.</p>
<p>Requirements:</p>
<ul>
<li>Git clone your <code>AirBnB_clone_v3</code></li>
<li>MySQL 5.7</code>&ldquo; target=&rdquo;_blank&quot;>Setup <code>MySQL 5.7</code> and import your production data dump</li>
<li>Create an <code>Upstart</code> script that starts a <code>Gunicorn</code> instance to serve <code>api/v1/app.py</code> from your <code>AirBnB_clone_v3</code></li>
<li>Make sure to use the necessary environment variables for your <code>AirBnB_clone_v3</code> app</li>
<li>Setup <code>Nginx</code> so that the route <code>/api/</code> points to your <code>Gunicorn</code> instance</li>
<li><code>Nginx</code> must serve this page both locally and on its public IP on port <code>80</code></li>
<li>Upload your <code>Upstart</code> config as <code>2-api-upstart_config</code></li>
<li>Upload your <code>Nginx</code> config  as <code>2-api-nginx_config</code></li>
</ul>
        <p>File: <code>2-api-upstart_config, 2-api-nginx_config</code></p>
  <h3>
    3. Serve your complete Airbnb clone
  </h3>
  <p>Let&rsquo;s serve what you built for AirBnB clone - Web dynamic on <code>web01</code>.</p>
<p>Requirements:</p>
<ul>
<li>Git clone your <code>AirBnB_clone_v4</code></li>
<li>Create an <code>Upstart</code> script that starts a <code>Gunicorn</code> instance to serve <code>web_dynamic/2-hbnb.py</code> from your <code>AirBnB_clone_v4</code></li>
<li>Setup <code>Nginx</code> so that the route <code>/</code> points to your <code>Gunicorn</code> instance</li>
<li>Setup <code>Nginx</code> so that it properly serves the static assets found in <code>web_dynamic/static/</code></li>
<li>For your website to be fully functional, you will need to reconfigure <code>web_dynamic/static/scripts/2-hbnb.js</code> to the correct IP and port</li>
<li><code>Nginx</code> must serve this page both locally and on its public IP on port <code>80</code></li>
<li>Make sure to pull up your Developer Tools on your favorite browser to verify that you have no errors</li>
<li>Upload your <code>Upstart</code> config as <code>3-complete_webapp-upstart_config</code></li>
<li>Upload your <code>Nginx</code> config  as <code>3-complete_webapp-nginx_config</code></li>
</ul>
<p>After loading, your website should look like this:</p>
        <p>File: <code>3-complete_webapp-upstart_config, 3-complete_webapp-nginx_config</code></p>
