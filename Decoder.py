# SNEHAL RAMDAS TALOLE
# 801045237

import sys

#Take input as command line arguments and calls three functions - 1. Read the input file. 2. Decode the input data. 3. Store the decoded data
def run_decoder():

    input_file_name=sys.argv[1]     # Acess input file name as input1.lzw as command line argument
    bit_length=int(sys.argv[2])     # Acess bit_length as command line argument. Bit_length is number of encoding bits

    output_file_name=input_file_name.split("\\")[-1].split(".")[0] + "_decoded.txt"     #Take ouput file name for decode function as input1_decoded.txt

    input_string=read_input(input_file_name)        #Calls read_input(input_file_name) function 

    decoded_list=decode(input_string,bit_length)    #Calls decode(input_string,bit_length) function
  
    final_decoded_string=write_input(decoded_list,output_file_name)    #Calls write_input(decoded_list,output_file_name) function 

# Read the input data and returns it in the form of list of codes
def read_input(input_file_name):
    print('### LZW Decompression ###')
    result=[]
    with open(input_file_name,'r',encoding = 'UTF-16BE') as file:
        input_string=file.read()

        #convert to integer
        for value in input_string:
            result.append(ord(value))
      
    return result

# Decode the input data
def decode(input_string,bit_length):
    MAX_TABLE_SIZE = 2 ** bit_length         # Initialize MAX_TABLE_SIZE

    # Initialise the table
    table = []
    for i in range(0,256):
        table.append(chr(i))

    # The zeroth(first) element in input_string is popped out and assigned to decoded_string
    code = input_string[0]      
    decoded_string = table[code]

    output = decoded_string

    # Get input while there are still codes needs to receive. As we have taken the 0th element, we are starting from index 1
    for code in input_string[1:]:       

        if code >= len(table):          # Check if the Decoder has codes to decode
            new_decoded_string = decoded_string + decoded_string[0]
        else:
            new_decoded_string = table[code]

        output+=new_decoded_string      # Output the new string

        if len(table) < MAX_TABLE_SIZE:   # Check if the Table is not full   
            table.append(decoded_string + new_decoded_string[0])
        decoded_string = new_decoded_string  

    return output 

# Store the decoded data in txt file
def write_input(output_list,output_file_name):
    
    with open(output_file_name,'w') as file:         # Open file to write 
        file.write(output_list)                      # Write decoded data to file

if __name__=="__main__":
    run_decoder()