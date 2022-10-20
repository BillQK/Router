This is an BGP router. The router has a fowarding tables, generating route announements, and forwarding data packets from internet users. Our high-level approach to a router is that when receiving a packet, the router need to determines what is the type of the message update|withdraw|data|no route|dump|table|handshake. Then the request is handle by a each of its own function. The challenges that we faced is implement the levels of IP address, aggregating and disaggregating entries in foward table. We are able to overcome this challenge by writing own config file to test have a better understanding of the system. 

List of properties/features of your design: 
    - Boardcast Update 
    - Send Data 
    - Handles Withdraw Messages
    - Dump Table Messages
    - Handles Bad Route
    - Aggregate Table
    - Disaggregrate table

To ensure the correctness of our code, we created a custom Json configuration file and the desired results. Having this knowledge helps us figure how how a router really should function.


