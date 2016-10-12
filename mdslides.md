# Overview


## General Description

* Presenting paper " Security Flaws Induced by CBC Padding"
    * Author of the paper "Serge Vaudevan" from "EPFL"
    * Published in International Conf. of Theory and Application of cryptographic techniques
    * Publisher Springer Berlin Heidelberg in the year 2002


### Abstract

* In this paper is showed an efficient side-channel attack on CBC encryption mode. It use the concept of padding to leak easily information in a cryptographic implementation.

* It include potencial vulnerable applications and some solutions are propused to fix and prevent the attack.

* Messages are preformated and encrypted in CBC block cipher
    * Decryption validate the format
    * Receiver sends the validity of format (Ack)

* Side channel attack is performed
    * Using the concept of padding
    * Other padding techiniques is discussed to fix
      the problem

# Introduction

## Block Cipher Cryptography

* Block cipher is a deterministic algorithm
    * Operates on fixed-length input called blocks.
    * It has Encryption (E) and Decryption (D) function on sender and reciever side respectively.
    * Both function take at least two arguements, input (plaintext or message) and key 'k'.
    * Decryption function is defined as D = $E^{-1}$.
    * Any block to be encrypted or decrypted has to have the defined length size strictly.

\centerline{\includegraphics[width=.3\linewidth]{figs/block-cipher}}

\centerline{Encrytion in Block-Cipher}

* Block cipher is defined by an Encryption function as
    * $E_k(P) := E(k,P) : \{0,1\}^k * \{0,1\}^n -> \{0,1\}^n$ where n is length of bit string p

## Working of CBC

\centerline{\includegraphics[width=.6\linewidth]{figs/cbc}}

\centerline{Cipher Block Chaining}


* CBC mode is used to encrypt
    * Encryption of blocks of size b (i.e.: 8 words)
    * Each word is of one byte
    * Padding techniques are required. (i.e.: PKCS7)
    * Pad the word sequence with n words
    * Every padded word is equal to n
    * Padded sequence make length multiple of b
    * Divide the padded word sequence into blocks ($x_1$ .... $x_N$)
    * Each block consists of b words
    * Encrytion technique used is CBC
$y_1 = C(IV \oplus x_1), y_i = C(y_{i-1} \oplus x_i); i = 2,.... N$

## PKCS7 - Padding technique

* In case of a message doesn't length multiple of b, it is necessary to apply padding techniques on the last block.

* PKCS7 consists to add bytes with value number of bytes that are added.

* Example:
| DD DD DD DD DD DD DD DD | DD DD 06 06 06 06 06 06 |


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
    * To fix it CBc-MAC is encrypted
    * Still it can be attack with complexity of $W^{b/2}$

# Realization

## Mind Map

* \checkmark represents work done

* $\times$ represents work not done.

\centerline{\includegraphics[width=.5\linewidth]{figs/map}}

\centerline{Mind Map}


#  Attacks

## Side Channel Attack

* What is Side Channel Attack ?
    * Attack based on information gained from physical implementation
    * Rather than Brute force looking for attribute which leaks useful information
    * Mostly side channel attacks are based on statistical analysis

* Side channel attack use side information from the system to unevil some secret information
    * The CBC mode of a block cipher with the combination of well-known PKCS7 padding method
is defacto stnadard CBC usage.


### How Receiver Behaves on such attack ?

* How Reciever behaves if padding is not correct?
    * This question leads to oracle attack
    * Attack works with complexity O(NbW)
* Where W is Number of possible Words



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
