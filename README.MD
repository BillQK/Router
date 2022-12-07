High Level Approach:
    In order to complete this assignment in addition to the starter code given with the class for the router, we implemented a Forwarding Table class, which in there had many important methods which include: handling tie breaks among entries in our table, aggregating, and disaggregating our forwarding table(and the numerous functions required for those operations), and handling bitwise logic. Then within our Router class, we would delegate to an instance of this forward table class when required.

    Walking through the design of the code, after we connected to the correct ports, whenever we recieved a message from the sockets we would check the type of the message, and given the type we would then correctly process it to other methods within our routing tables class. Then when necessary we would delegate to our Forwarding table, or store the information within our given list of announcement. 

    Our router class correctly handles the given types:
    update - where it would forward the given message to the correct neighbors, and store the message in its list of announcements, and then add that entry to our ForwardTable
    withdraw - similar to the update, but instead calls for the forward table to remove a given entry
    data - which correctly forwards data messages to correct ips, (only if the relationship is favorable)
    dump - which returns our forwarding table.

Challenges Faced:
    One of the main challenges faced was sending specific table messages in the correct order, and not accidentially mutate our arguments in our messages.

List of properties/features:
    The main feature that I think is good was how we used the python library to convert our given dotted decimal value into binary, I felt our approach was unusual however, something still very good. Futhermore, our overall design in delegating to multiple helper methods to complete our code.

Testing:
    The main way that we tested our code was littering print statements of the values that we needed, furthermore prior to implementing our code, I would test specific methods in a separate file to ensure the correctness there. In addition to running the supplied config files multiple times.    




