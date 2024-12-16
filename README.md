<h1>CWE-446 | UI DISCREPANCY FOR SECURITY FEATURE</h1>


<h3>CLONE OUR REPOSITORY AND FOLLOW THESE STEPS TO RUN THE PROGRAMS</h3>

<h2>HOW DOES OUR IMPLEMENTATION WORK:</h2>
  
  <h3>The code:</h3>
  <p>The code implementation is a web absed iplenetation of a chatroom using python and the flask framework. It allows for many unsers to join the same chat room to cht with each other over the same network.

  Each user can have their own unique username within the chatroom.

  The chatroom allows you to see which user is who through their usernames and colour coding your messages and others messages differently.

  There is also the ability to enable encryption anytime in the chat for any duration of time during your time within the chatroom. This allows you to have a "secure" chatting experience with other members within the chatroom.</p>

  <h3>The exploit:</h3>
  <p>The exploit is a python code that connects to the port at which the communication occurs in the chatroom. It "listens" in on the conversation and is able to read and log the chats in a log file.

  The exploit code called interceptor.py just listens into the conversation that is occuring amongst the other users in the chatroom at that time. In order for the users to not be made aware of a "stranger" listening in on their chat, they are not notified of a new user connection on the UI end of the system. This raises less suspicion to the users of the existence of a bad actor connected to the system.</p>
  

-------------------------------------------------------------------------------------------------------

<h3>To run this app:</h3>

  cd the the folder:
  #
    cd cpsc525
  #
  
  -------------------------------------------------------------------------------------------------------
  
  run the server in the terminal:
  #
    python3 server.py    
  #
  OR
  #
    python server.py
  #

  -------------------------------------------------------------------------------------------------------
  
  run the exploit in an adjacent terminal:
  #
    python3 interceptor.py
  #
  OR
  #
    python interceptor.py
  #
  
  -------------------------------------------------------------------------------------------------------

<p>You can then connect as many devices that are on the same network at the given localhost url and seamlessly chat with each other. Specifically a url that is in the following format:

  #
     * Running on http://192.168.1.86:5555
  #

However, the interceptor knows the port which you will be communicating through!! Make sure to toggle encryption so they can't "listen" to your conversation.

The interceptor will save the chat history in an log file which can be reviewed to see the messages that it intercepted. Saves as "intercepted_messages.log"

To remove the interceptor log file make sure you cd to the "cpsc525" directory if you already aren't in it. Run the following command to remove the log file once done running using the app.</p>
#
    rm -f intercepted_messages.log
#

Here is a link to the video summary of the blog post: <link>https://youtu.be/5XyE8JMs2T8</link>

