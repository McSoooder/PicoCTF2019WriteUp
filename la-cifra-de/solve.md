When connecting we get prompted with a ciphertext. Before checking into it, googling "la cifra de" takes us
to the Wikipedia page about "La cifra" which doesn't seem to give us any clue. 
Looking at the ciphertext then. The brackets {} are not encrypted so it seems the flag is pasted into 
the middle of a text and then encrypted. If the special characters isn't encrypted, then perhaps the numbers
are also unencrypted. Searching for "la cifra 1508" (1508 coming from the ciphertext) gives us a hit on the 
trusty ol' Vigenére cipher on the site cryptomuseum.com where the text seems familiar. The book
*La cifra del.* is referenced, which further proves we hit the jackpot.

Vigenére ciphers use some kind of key, so to figure it out instead of brute-forcing I copy the ciphertext
that corresponds for "picoCTF" and decrypts them by hand using a Vigenére cipher table. Luckily the key was
short. Starting at the 'p' we see the key is "AGFL" (FLAG, but since how the cipher works the key repeats itself)
So now I use an online tool like <dcode.fr/vigenere-cipher> to decrypt the flag:

**picoCTF{b311a50_0r_v1gn3r3_c1ph3r1119c336}**


