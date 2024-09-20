Name: Mauricio I. Reyes Villanueva
Due: 09/20/2024

# ===== DAYTIME =====

> I.

Frame Summary:
3 192.168.64.2 129.6.15.28 TCP What do [SYN] and [ACK] mean?

Frame: 3
Source IP: 192.168.64.2
Destination IP: 129.6.15.28
Info: 54 54426 → 13 ACKi Seq=1 Ack=1 Win=32128 Len=0

> II.

Source (Cient) Port: 54426

> III.

The client needs a port because otherwise the server would not know which service on the client side to communicate with, since there are many services found on a client computer.

> IV.

Frame 4 contains the actual date and time response. The frame summary is the following:

4 129.6.15.28 192.168.64.2 DAYTIME Daytime Response

> IV.

SYN and ACK are flags that are often used between a client and a server in a three way handshake. SYN which is short for Synchronize is a TCP packet which initially initiates a connection between a client and server communication. This packet contains a sequence number that is used to keep track of the data being sent. The server then receives this packet and sends back a SYN-ACK (short for Synchonize Acknowledge) packet which contains the servers own sequence number as well as an acknowledgement of of receiving the clients SYN. Finally, the client sends an ACK (Acknowledge) packet back to the server with an established connection.

> V.

It can be noted that the daytime server initiated the closing of the TCP connection. This can be seen because they're the first to initiate the FIN flag, as shown in frame 5.

5 129.6.15.28 129.6.15.28 54 13 → 54426 [FIN, ACK] Seq=52 Ack=1 Win=66368 Len=0

# ===== HTTP =====

> I.
There were three TCP connections opened. You can tell because there are three TCP 3-way handshakes found in the packet log. This can also be found by filtering ip.address = 192.168.64.2 and then sorting by info. It then becomes a little easier to spot where all the handshakes occur.

> II.
The homepage was requested on the seventh frame. You can tell because this is when the GET request is first sent.

7	0.072185934	192.168.64.2	172.233.221.124	HTTP	409	GET /index.html HTTP/1.1 

> III.
The photograph jeff-square-colorado.jpg was requested on the eleventh frame, and you can tell based on the frame's info which provides the GET request alongside what was requested as shown below:

11	0.172671022	192.168.64.2	172.233.221.124	HTTP	382	GET /jeff-square-colorado.jpg HTTP/1.1

# ===== QUESTIONS =====

I still don't fully understand what the sequence number is for exactly.

What does it mean for a TCP connection to be opened? Is it simply whenever a TCP 3 way handshake is established, and for every one of these there's a connection? Additionally, is it true that for each http request there is a tcp connection and handshake?
 
