*Plumbing* is a reference to the act of pipe-ing commands. Combining two processes with eachother to create 
convenient one-liners where you run multiple commands.

Running netcat to connect to the server it gives us a wall of text in return. Somewhere in this I guess we
have our flag so it can be found in a number of ways, but for the sake of piping we can pipe the netcat
command to a grep search for the flag:
"**nc 2019shell1.picoctf.com 63345 | grep picoCTF**"

Flag:
**picoCTF{digital_plumb3r_4e7a5813}**
