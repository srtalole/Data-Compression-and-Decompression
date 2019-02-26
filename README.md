# Data-Compression-and-Decompression

*********************************************************************************************************************************************************************************************
*  LEMPEL�ZIV�WELCH (LZW) ALGORITHM  *
*********************************************************************************************************************************************************************************************

* INTRODUCTION
* FILE LIST
* Design/Implementation
	A.  Data Structure
	B. Encoder
	    i.  Psuedo Code 
	    ii. Design of code
	C. Decoder
	    i.  Psuedo Code 
	    ii. Design of code
	D. Summary
* Usage Instructions
* References
*********************************************************************************************************************************************************************************************

I. INTRODUCTION
------------------------------

	The Lempel-Ziv-Welch  (LZW) algorithm is a lossless data compression algorithm.

	LZW is an adaptive compression algorithm that does not assume prior knowledge of the input data distribution. This algorithm works well when the input data is sufficiently large and 	there is redundancy in the data.

	Two examples of commonly used file formats that use LZW compression are the GIF image format served from websites and the TIFF image format. LZW compression is also suitable for 	compressing text files, and is the algorithm in the compress Unix file compression utility.

	This algorithm has two modules:
	1. Encoding/Compressing
	2. Decoding/Decompressing


II. FILE LIST
------------------------------

	* Encoder.py		Source code for Compression/Encoding inside LZW Folder
	* Decoder.py		Source code for Decompression/Decoding inside LZW Folder
	* README.txt		Inside LZW Folder


III. DESIGN/IMPLEMENTATION
------------------------------


A.  Data Structure

	The Data Struture used is Lists which is a dynamically increasing array.

	Reason for using Lists is because it is a most versatile datatype available in Python and a dynamic data structure. We can store different data type elements in a list. Moreover, 		the lists can be concatenated, sliced and so on. As list is a sequentially ordered and sequentially searched ADT (Abstract Data Type), it can efficiently utilize the memory and 		hence, I preferred Lists using this over any other.

B. Encoder:

	i. Psuedo Code -

	MAX_TABLE_SIZE=2(bit_length) //bit_length is number of encoding bits
	initialize TABLE[0 to 255] = code for individual characters
	STRING = null
	while there are still input symbols:
	SYMBOL = get input symbol
	if STRING + SYMBOL is in TABLE:
	STRING = STRING + SYMBOL
	else:
	output the code for STRING
	If TABLE.size < MAX_TABLE_SIZE: // if table is not full
	add STRING + SYMBOL to TABLE // STRING + SYMBOL now has a code
	STRING = SYMBOL
	output the code for STRING
	

	ii. Design of Code - 
	
	STEP1:	Starts with importing the sys module of Python which is needed to access command line arguments from list sys.argv.
	STEP2:	To read the input file, the arguments required are input file name and bit length, got from sys.argv.
	STEP3: 	Initialize table to contain one entry for each byte with range 0 to 255.
	STEP4: 	Further move into the logic of the LZW; Start a loop - a FOR loop is used to check if there are still input symbols coming in.
	STEP5: 	Initialise an IF loop to see if String and Symbol (SS) in the table? 
		If (encoded_string + symbol) gives a string that is in the table, then store it to the encoded string. Further, check for incoming symbols.
	STEP6:	Else, If c(encoded_string + symbol) produces a string that is not in the table;	then add the new encoded sting to the table.
	STEP7:	Next check if the Table is not full by comapring with MAX_TABLE_SIZE.
		If so, append the table with (encoded_string + symbol). Assign symbol to encoded_string which contains the output.
	STEP8: 	Use write_input() to store the encoded data as 2 bytes in a file  y using by using UTF-16 Big Endian command named as input1.lzw .
	

C.  Decoder

	i. Psuedo Code - 

	MAX_TABLE_SIZE=2(bit_length)
	initialize TABLE[0 to 255] = code for individual characters
	CODE = read next code from encoder
	STRING = TABLE[CODE]
	output STRING
	while there are still codes to receive:
	CODE = read next code from encoder
	if TABLE[CODE] is not defined: // needed because sometimes the
	NEW_STRING = STRING + STRING[0] // decoder may not yet have code!
	else:
	NEW_STRING = TABLE[CODE]
	output NEW_STRING
	if TABLE.size < MAX_TABLE_SIZE:
	add STRING + NEW_STRING[0] to TABLE
	STRING = NEW_STRING
	

	ii. Design of Code - 
	
	STEP1:	Starts with importing the sys module of Python which is needed to access command line arguments from list sys.argv.
	STEP2:	To read the input file, the arguments required are input file name and bit length, got from sys.argv.
	STEP3:	As did in Encoder, Initialized dictionary to contain one entry for each byte with range 255. 
	STEP4:	Coming to the Decoder logic steps; to start with the first step is to pop up the first code from the input file and assigned to a variable named "code".
		Append it to the table. Then by using FOR loop, read the next code word from the input stream.
	STEP5:	Firstly check if there is code to read. If not, then just concatenate decoded_string + decoded_string[0] and add it to a variable "new_decoded_string".
		Else, read the code from input stream till EOF.
	STEP6:	Next check if the Table is not full. If so, then concatenate the first character in the new_decoded_string to the decoded_string produced by the previous code 
		and add the resulting string to the table by using table.append() command.
	STEP7:	Use write_input() to store the decoded data in txt file named as input1_decoded.txt .

D. Summary

	Programing language used:
	Python. 
	Version: 3.6.4
	IDE: Visual Studio Code

IV. USAGE INSTRUCTIONS
------------------------------

>	Pre Requisites:	Python of specified Version(3.6.4) should be installed.

>	Compression: 

			$ python Encoder.py input1.txt 12

	The Compressed Output file will be created in the current folder. EXAMPLE: input1.lzw

>	Decompression:

			$ python Decoder.py input1.lzw 12

	The Decompressed Output file will be created in the current folder. EXAMPLE: input1_decoded.txt
