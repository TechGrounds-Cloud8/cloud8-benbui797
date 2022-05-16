# SEC-04 Symmetric Encryption
Symmetric Encryption: Encryption using a single key that has to be shared between the encrypter (sender) and decrypter (receiver). The algorithm that is used to encrypt and decrypt should be publicly known (because then it has been well tested). The key is the only thing that is kept secret.  

<img src="../00_includes/SEC/SEC-04_symkey.png" alt="symmetric key" width=60%>  
  
There are systems that use a key only once (email will generate a new key for every email you sent) and systems that use a key multiple times (file encryption).  

Caesar cipher: shifting the letters of the alfabet by x amount. All letters are shifted by the same amount (it's therefor technically not a cipher).  
Substitution cipher: for every letter in the alfabet, there is a key-map where the replacement value for every input value is noted.  

**How to crack weak ciphers?**  
We can analyse a cipher text and compare the content to the most common letters (in English "e": 12.7%, "t": 9.1%. "a": 8.1% ). Which letter is the most frequent in the cipher text? That one has a very high probability of being "e" and we can continue to do this for the next letters too.  
Furthermore, we can search the ciphertext for digrams (common combination of two letters; "he", "an", "in", "th)  and trigrams.  
In computers, we can convert alfabetical letters to numerical values by using the ASCII encoding (how letters are stored in a byte) to perform these operations easier.  
  

Modern encryption using computers works a little bit different; the computer performs an XOR operation on the bits to encrypt or decrypt the message. A cipher has perfect secrecy (the ciphertext doesn't reveal anything about the plaintext) if for any given cipher text, there exists only 1 key. The "One Time Pad" is such a method, but the downside of OTP is that the key needs to be atleast as long as the text, therefor it's not efficient.  
  

In simple terms, good cryptography is not about being perfectly secure, but to make it as hard as possible to crack, whilst still being efficient to encrypt/decrypt. There are a couple of mathemetical problems, that take an incredible amount of processing power, such as prime factorisation and discrete logarithms problems. By using a key with a long enough length, it's not impossible to crack a key, but with today's processing powers, it would take 1000's of years to do so (and therefor it is considered safe).

## Key terminology
- Plaintext: original/input text
- Ciphertext: encrypted text
- Encrypt: Convert plaintext into ciphertext
- Decrypt: Convert ciphertext into plaintext
- key: the input variable into a function that encrypts/decrypts data.
- keyspace: all possible valid and distict variations in a specific cryptosystem. This is also the amount of attempts required by a brute-force attack to crack a cipher.
- Caesar cipher: shifting all letters in the alfabet by the same amount.
- Vigenère cipher: Repeating a key for the for the length of the full message to match both lengths. Then you add both letters together (mod 26) to get the ciphertext. This was used in the 16th century.
- Rotor Machines: machines that use a rotating disc that turns for every character typed. Therefor the keymap is shuffled and contains less patterns. Hebern machine (single rotor) and the Enigma machine (3-5 rotors) are examples. These were used from 1870 - 1943.
- DES: Data Encryption Standard (1974). After the enigma machina, digital encryption came into play. DES was a standard requirement (kind of like a protocol). AES (2001) and Salsa20(2008) are other examples.
- Block cipher: Enciphers input in blocks of plaintext.
- Stream cipher: Enciphers input by individual character.


## Exercise
### Sources
- https://www.coursera.org/learn/cryptography#about (too mathemathical lol, I started some maths course to improve that first)
- CS50
- Computerphile Youtube Channel
- https://en.wikipedia.org/wiki/Cryptography
- https://www.asciichart.com/

### Overcome challenges
- I am interested in cryptography, so I had already looked most of it up. I thought it was a good idea to dive deeper this time and start a cryptography course, but it was pretty much only mathemetical formula's and got me confused about a lot of simple concepts... I think that was an example of diving too deep.

### Results
[Describe here the result of the exercise. An image can speak more than a thousand words, include one when this wisdom applies.]
