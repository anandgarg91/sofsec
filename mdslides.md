# Overview

## General Description

* Presenting paper "Security Flaws Induced by CBC Padding"
    * Author of the paper "Serge Vaudevan" from "EPFL"
    * Published in International Conference of Theory and Application of cryptographic techniques
    * Publisher Springer Berlin Heidelberg in the year 2002


### Summary

* In this paper is showed an efficient side-channel attack on CBC encryption mode. It use the concept of padding to leak easily information in a cryptographic implementation.

* It includes potencial vulnerable applications and some solutions are propused to fix and prevent the attack.

# Introduction

## Block Cipher Cryptography

* It is a deterministic algorithm
* Operates on fixed-length (denote by $b$) input called blocks.
* Messages are divided in $N$ blocks, such that $M = \{P_1,\dots, P_N\}$.
* Any plaintext block $P_i$ has to strictly have the fixed block size length before to apply encrypting/decrypting function.

\centerline{\includegraphics[width=.5\linewidth]{figs/block-cipher-entropy}}

### Operation modes

* For increasing the entropy, there are different modes to operate block ciphers, such as ECB, CBC, PCPC, CFB, and others.


## CBC - Cipher block chaining

\centerline{\includegraphics[width=1\linewidth]{figs/cbc-enc-dec}}

* CBC mode works:
    * Every plaintext block to be encrypted $P_i$ is XOR-ed with the previous ciphertext $C_{i-1}$.
    * The ciphertext $C_0$ is an initialization vector.
    * When the length of the last plaintext block is not equal to the fixed block size, padding techniques are required (i.e.: PKCS7).
    * Encryption $C_i = E_k(C_{i-1} \oplus P_i); C_0 = IV; i = 2,\dots, N$
    * Decryption $P_i = E^{-1}_k(C_i) \oplus C_{i-1}; C_0 = IV; i = 2,\dots, N$

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

# Padding

## PKCS7 - Padding technique

* In case of a message doesn't a length multiple of $b$, it is necessary to apply padding techniques on the last block.

* The are different thechnique for padding, such as ANSI X.923, ISO 10126, Zero padding.

* PKCS7 is one of the most commonly used and it consists to add bytes with value number of bytes that are added.

* Example:
\centerline{block $P_{N-1}$ | dd dd dd dd dd dd dd dd |\break}
\centerline{block $P_{N} $ | dd dd 06 06 06 06 06 06 |}

    <!--- * add pauses -->
    <!--- * check `pdfpc` -->
<!--- * NOTE: 20-22 min talk + 5 min Q&A -->

# Realization

## Mind Map

* \checkmark represents work done

* $\times$ represents work not done.

\centerline{\includegraphics[width=.5\linewidth]{figs/map}}

\centerline{Mind Map}


#  Attack

## Side Channel Attack

* What is Side Channel Attack ?
    * Attack based on information gained from implementation.
    * Rather than Brute force looking for attribute which leaks useful information.
    * Mostly side channel attacks are based on statistical analysis.
    * Example: Acoustic cryptoanalysis - attacks that exploit sound produced during a computation.

## Padding of oracle Attack

\centerline{\includegraphics[width=0.4\linewidth]{figs/oracle-attack-before-plaintext}}

* This attack is able to "guess" the plaintext from ciphertext in a crypto-system implementation where there is an __oracle__ (denote by $O$) and within it is possible to distinguish padding error to the others.

* Through this attack, the complexity of this attack is significantly less than others attacks (i.e.: brute force on the private key).

## How it works?


* Side channel attack use side information from the system to unevil some secret information
    * The CBC mode of a block cipher with the combination of well-known PKCS7 padding method
is defacto stnadard CBC usage.

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
