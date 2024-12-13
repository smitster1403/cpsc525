CLONE OUR APP AND FOLLOW THESE STEPS TO RUN THE FILES

HOW DOES OUR IMPLEMENTATION WORK:
  #
    paragraph goes here
  #

-------------------------------------------------------------------------------------------------------

To run this app:

  cd the the folder
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

You can then connect as many devices that are on the same network at the given localhost url and seamlessly chat with each other.

However, the interceptor knows the port which you will be communicating through!! Make sure to toggle encryption so they can't "listen" to your conversation.

The interceptor will save the chat history in an log file which can be reviewed to see the messages that it intercepted.

To remove the interceptor make sure you cd to the directory if you already aren't in it. Run the following command to remove the log file once done running using the app.
  rm -f intercepted_messages.log
