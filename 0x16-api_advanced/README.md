<h1>0x16. API advanced</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to read API documentation to find the endpoints you&rsquo;re looking for</li>
<li>How to use an API with pagination</li>
<li>How to parse JSON results from an API</li>
<li>How to make a recursive API call</li>
<li>How to sort a dictionary by value</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. How many subs?
  </h3>
  <p>Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.</p>
<p>Hint: No authentication is necessary for most features of the Reddit API. If you&rsquo;re getting errors related to Too Many Requests, ensure you&rsquo;re setting a custom User-Agent.</p>
<p>Requirements:</p>
<ul>
<li>Prototype: <code>def number_of_subscribers(subreddit)</code></li>
<li>If not a valid subreddit, return 0.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul>
        <p>File: <code>0-subs.py</code></p>
  <h3>
    1. Top Ten
  </h3>
  <p>Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.</p>
<p>Requirements:</p>
<ul>
<li>Prototype: <code>def top_ten(subreddit)</code></li>
<li>If not a valid subreddit, print None.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul>
        <p>File: <code>1-top_ten.py</code></p>
  <h3>
    2. Recurse it!
  </h3>
  <p>Write a <em>recursive function</em> that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.</p>
<p>Hint: The Reddit API uses pagination for separating pages of responses.</p>
<p>Requirements:</p>
<ul>
<li>Prototype: <code>def recurse(subreddit, hot_list=[])</code></li>
<li>Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.</li>
<li>If not a valid subreddit, return None.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul>
<p>Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)</p>
        <p>File: <code>2-recurse.py</code></p>
  <h3>
    3. Count it!
  </h3>
  <p>Write a <em>recursive function</em> that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).</p>
<p>Requirements:</p>
<ul>
<li>Prototype: <code>def count_words(subreddit, word_list)</code></li>
<li>Note: You may change the prototype, but it must be able to be called with just a subreddit supplied and a list of keywords. AKA you can add a counter or anything else, but the function must work without supplying a starting value in the main.</li>
<li>Results should be printed in descending order, by the count, not the title. Words with no matches should be skipped and not printed.</li>
<li>Results are based on the number of times a keyword appears, not titles it appears in. &lsquo;java java java&rsquo; counts as 3 separate occurences of java.</li>
<li>To make life easier, &lsquo;java.&rsquo; or &lsquo;java!&rsquo; or &lsquo;java_&rsquo; should not count as &lsquo;java&rsquo;</li>
<li>If no posts match or the subreddit is invalid, print a newline.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are NOT following redirects.</li>
</ul>
<p>Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)</p>
        <p>File: <code>100-count.py</code></p>
