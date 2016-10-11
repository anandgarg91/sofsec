# Abstract

## Side Channel Attacks on CBC 

* Messages are preformated and encrypted in CBC block cipher
    * Decryption validate the format
    * Receiver sends the validity of format (Ack)

* Side channel attack is performed 
    * Using the concept of padding
    * Other padding techiniques is discussed to fix
      the problem
  

# Introduction

## Working of CBC
  	
* RC5-CBC_PAD algorithm is used to encrypt
    * Encrytion of blocks b (8 words)
    * Each word is of one byte
    * Padding technique used is PKCS7
    * Pad the word sequence with n words
    * Every padded word is equal to n
    * Padded sequence make length multiple of b
    * Divide the padded word sequence into blocks ($x_1$ .... $x_N$)
    * Each block consists of b words
    * Encrytion technique used is CBC
$y_1 = C(IV \oplus x_1), y_i = C(y_{i-1} \oplus x_i); i = 2,.... N$




    <!--- * add pauses -->
    <!--- * check `pdfpc` -->
<!--- * NOTE: 20-22 min talk + 5 min Q&A -->


# Motivation

## How Receiver Behaves

* How Reciever behaves if padding is not correct?
    * This question leads to oracle attack
    * Attack works with complexity O(NbW)
* Where W is Number of possible Words

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


#  TODO
 
