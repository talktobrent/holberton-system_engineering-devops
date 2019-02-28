<h1>0x07. Networking basics #0</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>OSI Model</h3>

<ul>
<li>What it is</li>
<li>How many layers it has</li>
<li>How it is organized</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. OSI model
  </h3>
  <p>OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.</p>
<p>It is organized from the lowest level to the highest level:</p>
<ul>
<li>The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal</li>
<li>The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc</li>
</ul>
<p>Keep in mind that the OSI model is a concept, it&rsquo;s not even tangible. The OSI model doesn&rsquo;t perform any functions in the networking process.
It is a conceptual framework so we can better understand complex interactions that are happening.
Most of the functionality in the OSI model exists in all communications systems.</p>
<p>In this project we will mainly focus on:</p>
<ul>
<li>The Transport layer and especially TCP/UDP</li>
<li>On the Network layer with IP and ICMP</li>
</ul>
<p>The image bellow describes more concretely how you can relate to every level.</p>
<p>Questions:</p>
<p>What is the OSI model?</p>
<ol>
<li>Set of specifications that network hardware manufacturers must respect</li>
<li>The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology</li>
<li>The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology</li>
</ol>
<p>How is the OSI model organized?</p>
<ol>
<li> Alphabetically</li>
<li>From the lowest to the highest level</li>
<li>Randomly</li>
</ol>
        <p>File: <code>0-OSI_model</code></p>
  <h3>
    1. Types of network
  </h3>
<p>LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.</p>
<p>Questions:</p>
<p>What type of network are Holberton iMacs connected to?</p>
<ol>
<li>Internet</li>
<li>WAN</li>
<li>LAN</li>
</ol>
<p>What type of network could connect an office in one building to another office in a building a few streets away?</p>
<ol>
<li>Internet</li>
<li>WAN</li>
<li>LAN</li>
</ol>
<p>What network do you use when you browse www.holbertonschool.com from your smartphone (not connected to the Wifi)?</p>
<ol>
<li>Internet</li>
<li>WAN</li>
<li>LAN</li>
</ol>
        <p>File: <code>1-types_of_network</code></p>
  <h3>
    2. MAC and IP address
  </h3>
<p>Questions:</p>
<p>What is a MAC address?</p>
<ol>
<li>The name of a network interface</li>
<li>The unique identifier of a network interface</li>
<li>A network interface</li>
</ol>
<p>What is an IP address?</p>
<ol>
<li>Is to devices connected to a network what postal address is to houses</li>
<li>The unique identifier of a network interface</li>
<li>Is a number that network devices use to connect to networks</li>
</ol>
        <p>File: <code>2-MAC_and_IP_address</code></p>
  <h3>
    3. UDP and TCP
  </h3>
<p>Let&rsquo;s fill the empty parts in the drawing above.</p>
<p>Questions:</p>
<ul>
<li>Which statement is correct for the TCP box:
<ol>
<li><code>It is a protocol that is transferring data in a slow way but surely</code></li>
<li><code>It is a protocol that is transferring data in a fast way and might loss data along in the process</code></li>
</ol></li>
<li>Which statement is correct for the UDP box:
<ol>
<li><code>It is a protocol that is transferring data in a slow way but surely</code></li>
<li><code>It is a protocol that is transferring data in a fast way and might loss data along in the process</code></li>
</ol></li>
<li>Which statement is correct for the TCP worker:
<ol>
<li><code>Have you received boxes x, y, z?</code></li>
<li><code>May I increase the rate at which I am sending you boxes?</code></li>
</ol></li>
</ul>
        <p>File: <code>3-UDP_and_TCP</code></p>
  <h3>
    4. TCP and UDP ports
  </h3>
  <p>Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.</p>
<p>If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.</p>
<p>While the full list of ports should not be memorized, it is important to know the most used ports, let&rsquo;s start by remembering 3 of them:</p>
<ul>
<li><strong>22</strong> for SSH</li>
<li><strong>80</strong> for HTTP</li>
<li><strong>443</strong> for HTTPS</li>
</ul>
<p>Note that a specific IP + port = socket.</p>
<p>Write a Bash script that displays listening ports:</p>
<ul>
<li>That only shows listening sockets</li>
<li>That shows the PID and name of the program to which each socket belongs</li>
</ul>
        <p>File: <code>4-TCP_and_UDP_ports</code></p>
  <h3>
    5. Is the host on the network
  </h3>
<p>The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command <code>ping</code> uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network. </p>
<p>Write a Bash script that pings an IP address passed as an argument.</p>
<p>Requirements: </p>
<ul>
<li>Accepts a string as an argument</li>
<li>Displays <code>Usage: 5-is_the_host_on_the_network {IP_ADDRESS}</code> if no argument passed</li>
<li>Ping the IP 5 times</li>
</ul>
<p>It is interesting to look at the <code>time</code> value, which is the time that it took for the ICMP request to go to the <code>8.8.8.8</code> IP and come back to my host. The IP <code>8.8.8.8</code> is owned by Google, and the quickest roundtrip between my computer and Google was 7.57 ms which is pretty fast, which is a sign that the network path between my computer and Google&rsquo;s datacenter is in good shape. A slow ping would indicate a slow network.</p>
<p>Next time you feel that your connection is slow, try the <code>ping</code> command to see what is going on!</p>
        <p>File: <code>5-is_the_host_on_the_network</code></p>
