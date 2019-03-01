<h1>0x19. Postmortem</h1>
<h2>Tasks</h2>
  <h3>
    0. My first postmortem
  </h3>
<p>Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. Most of you will never have faced an outage, so just get creative and invent your own :)</p>
<p>Requirements:</p>
<ul>
<li>Issue Summary (that is often what executives will read) must contain:
<ul>
<li>duration of the outage with start and end times (including timezone)</li>
<li>what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)</li>
<li>what was the root cause</li>
</ul></li>
<li><p>Timeline (format bullet point, format: <code>time</code> - <code>keep it short, 1 or 2 sentences</code>) must contain:</p>
<ul>
<li>when was the issue detected</li>
<li>how was the issue detected (monitoring alert, an engineer noticed something, a customer complained&hellip;)</li>
<li>actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)</li>
<li>misleading investigation/debugging paths that were taken</li>
<li>which team/individuals was the incident escalated to</li>
<li>how the incident was resolved</li>
</ul></li>
<li><p>Root cause and resolution must contain:</p>
<ul>
<li>explain in detail what was causing the issue</li>
<li>explain in detail how the issue was fixed</li>
</ul></li>
<li><p>Corrective and preventative measures must contain:</p>
<ul>
<li>what are the things that can be improved/fixed (broadly speaking)</li>
<li>a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory&hellip;)</li>
</ul></li>
<li><p>Be brief and straight to the point, between 400 to 600 words</p></li>
</ul>
<p>While postmortem format can vary, stick to this one so that you can get properly reviewed by your peers.</p>
        <p>File: <code>README.md</code></p>
