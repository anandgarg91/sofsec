# Overview


## General Description 

* Presenting paper " Security Flaws Induced by CBC Padding"
    * Author of the paper "Serge Vaudevan" from "EPFL"
    * Published in International Conf. of Theory and Application of cryptographic techniques
    * Publisher Springer Berlin Heidelberg in the year 2002


### Abstract

* Messages are preformated and encrypted in CBC block cipher
    * Decryption validate the format
    * Receiver sends the validity of format (Ack)

* Side channel attack is performed 
    * Using the concept of padding
    * Other padding techiniques is discussed to fix
      the problem
  

# Introduction

## Block Cipher Cryptography

* TODO
    * TODO

## Working of CBC
  	
* RC5-CBC_PAD algorithm is used to encrypt
    * Encryption of blocks b (8 words)
    * Each word is of one byte
    * Padding technique used is PKCS7
    * Pad the word sequence with n words
    * Every padded word is equal to n
    * Padded sequence make length multiple of b
    * Divide the padded word sequence into blocks ($x_1$ .... $x_N$)
    * Each block consists of b words
    * Encrytion technique used is CBC
$y_1 = C(IV \oplus x_1), y_i = C(y_{i-1} \oplus x_i); i = 2,.... N$


### How Receiver Behaves

* How Reciever behaves if padding is not correct?
    * This question leads to oracle attack
    * Attack works with complexity O(NbW)
* Where W is Number of possible Words


    <!--- * add pauses -->
    <!--- * check `pdfpc` -->
<!--- * NOTE: 20-22 min talk + 5 min Q&A -->


# Properties

## CBC properties

  * Efficiency 
    * Constant memory used for infinite length message
    * On ECB simple ciphertext manipulation attack possible
    * CBC bring higher message entropy
    * Exhaustive search on CBC mode depends on length of key


  * Confidentiality Limits

    * Due to fix IV, Easy to decode prefix block
    * In case two ciphertext are same
    * If Two ciphertext $y_i$ and $y_j$ are equal
      $y_{i-1} \oplus y_{j-1} = x_i \oplus x_j$
    * Redundancy in plaintext can help to get $x_i and x_j$
    * Two words are equal out of N 
    * According to Birthday Paradox can be given as
      $P = 1 - e^{-1/2N^2.W^{-b}}$

  * Authentication Limits
    * CBC can be used to create MAC
    * One can forge the MAC by analysing the augmented pattern 
    * To fix it CBS-MAC is encrypted
    * Still it can be attack with complexity of $W^{b/2}$


#  Attacks

## Side Channel Attack

* What is Side Channel Attack ?
    * TODO




## Oracle Attack

### Let b the block length in words and W be the number of possible words then Oracle 'O' will yield 1, if decrytion in CBC has correct padding. Oracle 'O' is defined by C and IV.

  * Last Word Oracle 
    * Need to compute last word of $C^{-1}$(y)
    * Let $r_1.....r_b$ be random words
    * We forge a ciphertext and perform $C^{-1} \oplus r$
    * If $C^{-1} \oplus r$ = 1 then its a valid padding
    * Resulting $C^{-1}$(y) is $r_b \oplus 1$
      
  * Block Decryption oracle
    * Let $a_1....a_b$ be the word sequence of $C^{-1}(y)$.
    * Get $a_b$ by last word  oralce
    * Iterate until recover whole sequence
    * Need W/2 trials on average, since b words/block need bW/2

# Padding scheme

## Discussion of different padding scheme

  * TODO
    * here you can change

# Evaluation

## Testing the launch attack

* How we test our launched attack?
    * TODO
 
