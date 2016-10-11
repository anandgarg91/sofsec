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
    * Divide the padded word sequence into blocks
    * Each block consists of b words
    * Encrytion technique used is CBC


* Address the problem of side channel
    * Satisfying both, traditional and ICS requirements
    * Like cost, maintainability, time, and determinism

* Present the Usuage of CBC technique
    * Cipher block text
    	
* Show a limitation of such technique
    * Oracle attack


    <!--- * add pauses -->
    <!--- * check `pdfpc` -->
<!--- * NOTE: 20-22 min talk + 5 min Q&A -->



# Motivation

## Industrial Control Systems (ICS)


