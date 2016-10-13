# Overview

## General Description

* Presenting paper "Security Flaws Induced by CBC Padding"
    * Author: Serge Vaudenay, Affiliated with Swiss Federal Institute of Technology
    * Published in: EUROCRYPT
    * Year: 2002

### Summary

* In this paper, the author shows an efficient side-channel attack on CBC encryption mode. he uses the concept of padding to leaks easily information in a cryptographic implementation.

* It includes a list of potencial vulnerable applications and some solutions are propused to fix and prevent the attack.

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
    * Encryption $C_i = E_k(C_{i-1} \oplus P_i); C_0 = IV; i = 1,\dots, N$
    * Decryption $P_i = E^{-1}_k(C_i) \oplus C_{i-1}; C_0 = IV; i = 1,\dots, N$


# Padding

## PKCS7 - Padding technique

* In case of the message length is not a multiple of $b$, it is necessary to apply padding techniques on the last block.

* The are different thechnique for padding, such as ANSI X.923, ISO 10126, Zero padding.

* PKCS7 is one of the most commonly used and it consists to add bytes with value number of bytes that are added.

    * Example six bytes for padding:
\centerline{block $P_{N-1}$ |dd dd dd dd dd dd dd dd|}
\centerline{block $P_{N} $ |dd dd \bf{06 06 06 06 06 06}|}

    * Example one byte for padding:
\centerline{block $P_{N-1}$ |dd dd dd dd dd dd dd dd|}
\centerline{block $P_{N}$ |dd dd dd dd dd dd dd \bf{01}|}

    * Example NO padding:
\centerline{block $P_{N-1}$ |dd dd dd dd dd dd dd dd|}
\centerline{block $P_{N}$ |\bf{08 08 08 08 08 08 08 08}|}

#  Attack



## Side Channel Attack

* What is Side Channel Attack ?
    * Attack based on information gained from implementation.
    * Rather than Brute force looking for attribute which leaks useful information.
    * Mostly side channel attacks are based on statistical analysis.
    * Example: Acoustic cryptoanalysis - attacks that exploit sound produced during a computation.

## Padding of oracle Attack

\centerline{\includegraphics[width=0.4\linewidth]{figs/oracle-attack-before-plaintext}}

* This attack is able to "guess" the plaintext from ciphertext in a crypto-system implementation where there is an __oracle__ (denote by $\Theta$) and within it is possible to distinguish padding error to the others when it try to decrypt messages.

* The complexity of this attack is significantly less than others attacks (i.e.: brute force on the private key).

## Crypto-system implementation

\centerline{\includegraphics[width=.6\linewidth]{figs/crypto-system}}

* Let's suppose that Lisa is sending messages to Nelson. They are using RC5/CBC/PKCS7 to encrypt the messages with a pre-shared private key; Milhouse is able to see and store the encrypted messages, but he doesn't know the key.

* To do the padding oracle attack possible, it is required that Nelson does a distinguished behaviour when he receives encrypted messages $C_m$ with padding errors.


## How it works?

\centerline{\includegraphics[width=.6\linewidth]{figs/crypto-system}}

* In the above scenario, we have the next elements:
    * $b$: block size, 8 words (bytes)
    * $W$: possible values of each word, $\{0,\dots, 255\}$
    * $N$: Number of blocks generated for the message. Let's suppose the encrypted message is compused by $C_m = \{IV, C_1, C_2, C_3\}$ Then $N = 3$.
    * $IV$: Initialization vector, commonly it is random and public.
    * $\Theta$: Oracle, in this case is Nelson.

## How it works?

\centerline{\includegraphics[width=.3\linewidth]{figs/crypto-system}}

* To perform the attack, Milhouse will do the next general steps:
    1. Take the last encrypted block, $C_3$, it is composed by $\{r_0,\dots,r_b\}$.
    2. Create a random fake block called $C_\theta = \{y_0,\dots, y_b\}$, he will change the values byte to byte, since the last one to the first one.
    3. Concatenate the fake block with the encrypted block, $C_m' = \{C_\theta | C_3\}$.
    4. Send $C_m'$ to Nelson and wait for his answer (error behaviour) when he tries to decrypt the message.
      * If Nelson says there is error in padding, Milhouse will return step 2 changing the value of the actual worked byte $y_b$.
      * If Nelson doesn't show padding error, Milhouse will return step 2 working on the next byte $y_{b-1}$.

## No padding error means ...

\centerline{\includegraphics[width=0.3\linewidth]{figs/oracle-attack-before-plaintext}}

* Remember how the padding PKCS7 works.

    * Example six bytes for padding:
\centerline{block $P_{N-1}$ |dd dd dd dd dd dd dd dd|}
\centerline{block $P_{N}$ |dd dd \bf{06 06 06 06 06 06}|}

    * Example one byte for padding:
\centerline{block $P_{N-1}$ |dd dd dd dd dd dd dd dd|}
\centerline{block $P_{N}$ |dd dd dd dd dd dd dd \bf{01}|}

    * Example NO padding:
\centerline{block $P_{N-1}$ |dd dd dd dd dd dd dd dd|}
\centerline{block $P_{N}$ |\bf{08 08 08 08 08 08 08 08}|}


## The aim of the attack

\centerline{\includegraphics[width=0.3\linewidth]{figs/oracle-attack-before-plaintext}}

* First cycle, to find $\{y_b\} \in C_\theta$ such that:
\centerline{$C_\theta \oplus E^{-1}_k(C_3) =$ \{$d_r$ $d_r$ $d_r$ $d_r$ $d_r$ $d_r$ $d_r$ 01\}}

* Second cycle, to find $\{y_{b-1} \oplus 2, y_b \oplus 2\} \in C_\theta$ such that:
\centerline{$C_\theta \oplus E^{-1}_k(C_3) =$ \{$d_r$ $d_r$ $d_r$ $d_r$ $d_r$ $d_r$ 02 02\}}

*

* Last cycle, to find $\{y_0 \oplus 8,\dots, y_{b-1} \oplus 8, y_b \oplus 8\} \in C_\theta$ with such that:
\centerline{$C_\theta \oplus E^{-1}_k(C_3) =$ \{08 08 08 08 08 08 08 08\}}

## Getting the plaintext

\centerline{\includegraphics[width=0.3\linewidth]{figs/oracle-attack-before-plaintext}}

* For getting the plaintext, Milhouse only has to do:
\centerline{$P_i=C^\theta_i \oplus C_{i-1}$}

* To decrypt completely the message, Milhouse has to calculate a $C^\theta$ for each $C_i$ in the encrypted message.

\centerline{\includegraphics[width=0.1\linewidth]{figs/milhouse}}


# Realization

## Mind Map

* \checkmark represents work done

* $\times$ represents work not done.

\centerline{\includegraphics[width=.5\linewidth]{figs/map}}

\centerline{Mind Map}
