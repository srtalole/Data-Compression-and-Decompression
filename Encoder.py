# SNEHAL RAMDAS TALOLE
# 801045237

import sys

#Take input as command line arguments and calls three functions - 1. Read the input file. 2. Encode the input data. 3. Store the encoded data
def run_encoder():

    input_file_name=sys.argv[1]    #Acess input file name as input1.txt as command line argument
    bit_length=int(sys.argv[2])    #Acess bit_length as command line argument. Bit_length is number of encoding bits

    output_file_name=input_file_name.split("\\")[-1].split(".")[0] + ".lzw"     #Take ouput file name for encode function as input1.lzw

    input_string=read_input(input_file_name)        #Calls read_input(input_file_name) function 

    encoded_list=encode(input_string,bit_length)    #Calls encode(input_string,bit_length) function 

    resulted_list=write_input(encoded_list,output_file_name)     #Calls write_input(encoded_list,output_file_name) function 
    
# Read the input data and returns it in string.
def read_input(input_file_name):
    print('### LZW Compression ###')
    with open(input_file_name,'r') as file:
        input_string=file.read()
    return input_string

# Encode the input data
def encode(input_string,bit_length):
    MAX_TABLE_SIZE = 2 ** bit_length        # Initialize MAX_TABLE_SIZE

    # Initialise the table
    table = []                              
    for i in range(0,256):
        table.append(chr(i))

    encoded_string=''
    output=[]
    for symbol in input_string:
        SS = encoded_string + symbol        # Get input symbol while there are input symbols left
        if SS in table:                     # If SS is in TABLE
            encoded_string = SS
        else:
            output.append(table.index(encoded_string))    # Output the code for encoded_string

            if len(table) < MAX_TABLE_SIZE:               # Check if the table is not full
                table.append(encoded_string + symbol)    
            encoded_string = symbol

    output.append(table.index(encoded_string))            # Output the code for encoded_string
    return output      

# Store the encoded data in a file
def write_input(output_list,output_file_name):
    
    with open(output_file_name,'wb') as file:             # Open file to write in binary

        for value in output_list:
            b=chr(value)              # Convert number to character
            c=b.encode('utf-16BE')    # Convert stored character to 16-bit 16 Bit format by using UTF-16 Big Endian command
            file.write(c)             # Write converted number to file


if __name__=="__main__":
    run_encoder()