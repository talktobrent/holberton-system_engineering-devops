# Front Page Update Delay
## Issue Summary
At 3:00 PM Eastern time, the "Hello World" home page was due to be updated to say, "Hello Earth". This update was not properly implemented, resulting in a delay of the rollout of the new home page, until 5:01 PM Eastern time. Users who landed on the home page during this time (12 unique visitors), received the old "Hello World" string, rather than the newly implemented "Hello Earth" string. This resulted in 7 inquiries to customer support, about the status of the home page, and why customers were not receiving the new string. The root cause of this failure was the breakage of a symbolic link in the sites-enabled directory.
## Timeline
- At 3:15 PM Eastern time, customer support recieved a complaint from a user in Australia, that the scheduled "Hello Earth" string was not appearing on the home page, and the old, "Hello World" string was still being displayed.
- Customer service forwarded this ticket to the SRE team at 3:17 PM Eastern time. The SRE team immediately confirmed that the home page was indeed serving the old string to users.
- At 3:25 PM, Jimbo Jimberson was identified as the SRE member tasked with updating the string being served on the default home page. Jimbo confirmed that at 11:59 PM he ran the newly implemented BASH script to change the content served on the default home page.
- At 3:26 PM, another member of the SRE team confirmed that the default file in the sites-available directory was last updated at 11:59 PM and was configured to serve the new string. 
- At 3:27 PM The sites-enabled directory was verified, in which it was discovered that the default file was in fact a copy of the previous version, and not a symbolic link to the sites-available default file, as is its intended use.
- At 4:30 PM Eastern time, the default file in the sites-enabled directory was replaced with a symbolic link to the updated version in the sites-available directory.
- At 5:00 PM Eastern time, the Nginx server was restarted
- At 5:01 PM Eastern time, the SRE team confirmed that the webpage was now serving the new string to the public
## Root Cause
As part of the ongoing efforts to streamline management and updates, two weeks ago the SRE team created a BASH script to easily change the string displayed by our default home page. In the past, this was manually done by a now departed employee. In the midst of our investigation, an email was sent to this past employee to confirm our suspicions about how the symbolic link to the sites-available file was broken. This past employee confirmed that they used GNU sed to edit the sites-enabled files previously. The SRE team quickly confirmed that GNU sed indeed breaks symbolic links when used to edit a file. Therefor, the symbolic link was already broken, and while the BASH script properly edited the sites-available file, it did not verify the symbolic link.
## Corrective measures and prevention
- The BASH script was updated to recreate the symbolic link every-time it runs.
- A memo was sent out to all Engineering staff, informing them of this issue with GNU sed, and the proper way to edit the sites-enabled files.
- Training materials were updated to inform new hires of this potential issue.
- A README was placed in the sites-enabled directory, reminding engineers that only symbolic links are to be placed here, and files should be edited in the sites-available directory.
