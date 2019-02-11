<h1>0x15. API</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What Bash scripting should not be used for</li>
<li>What is an API</li>
<li>What is a REST API</li>
<li>What are microservices</li>
<li>What is the CSV format</li>
<li>What is the JSON format</li>
<li>Pythonic Package and module name style</li>
<li>Pythonic Class name style</li>
<li>Pythonic Variable name style</li>
<li>Pythonic Function name style</li>
<li>Pythonic Constant name style</li>
<li>Significance of CapWords or CamelCase in Python</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Gather data from an API
  </h3>
  <p>Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.</p>
<p>Requirements:</p>
<ul>
<li>You must use <code>urllib</code> or <code>requests</code> module</li>
<li>The script must accept an integer as a parameter, which is the employee ID</li>
<li>The script must display on the standard output the employee TODO list progress in this exact format:
<ul>
<li>First line: <code>Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):</code>
<ul>
<li><code>EMPLOYEE_NAME</code>: name of the employee</li>
<li><code>NUMBER_OF_DONE_TASKS</code>: number of completed tasks</li>
<li><code>TOTAL_NUMBER_OF_TASKS</code>: total number of tasks, which is the sum of completed and non-completed tasks</li>
</ul></li>
<li>Second and N next lines display the title of completed tasks: Tab <code>TASK_TITLE</code> (with 1 tabulation + 1 space before)</li>
</ul></li>
</ul>
<p>Example:</p>
        <p>File: <code>0-gather_data_from_an_API.py</code></p>
  <h3>
    1. Export to CSV
  </h3>
  <p>Using what you did in the task #0, extend your Python script to export data in the CSV format.</p>
<p>Requirements:</p>
<ul>
<li>Records all tasks that are owned by this employee</li>
<li>Format must be: <code>&quot;USER_ID&quot;,&quot;USERNAME&quot;,&quot;TASK_COMPLETED_STATUS&quot;,&quot;TASK_TITLE&quot;</code></li>
<li>File name must be: <code>USER_ID.csv</code></li>
</ul>
<p>Example:</p>
        <p>File: <code>1-export_to_CSV.py</code></p>
  <h3>
    2. Export to JSON
  </h3>
  <p>Using what you did in the task #0, extend your Python script to export data in the JSON format.</p>
<p>Requirements:</p>
<ul>
<li>Records all tasks that are owned by this employee</li>
<li>Format must be: <code>{ &quot;USER_ID&quot;: [ {&quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS, &quot;username&quot;: &quot;USERNAME&quot;}}, {&quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS, &quot;username&quot;: &quot;USERNAME&quot;}}, ... ]}</code></li>
<li>File name must be: <code>USER_ID.json</code></li>
</ul>
<p>Example:</p>
        <p>File: <code>2-export_to_JSON.py</code></p>
  <h3>
    3. Dictionary of list of dictionaries
  </h3>
  <p>Using what you did in the task #0, extend your Python script to export data in the JSON format.</p>
<p>Requirements:</p>
<ul>
<li>Records all tasks from all employees</li>
<li>Format must be: <code>{ &quot;USER_ID&quot;: [ {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, ... ], &quot;USER_ID&quot;: [ {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, ... ]}</code></li>
<li>File name must be: <code>todo_all_employees.json</code></li>
</ul>
<p>Example:</p>
        <p>File: <code>3-dictionary_of_list_of_dictionaries.py</code></p>
