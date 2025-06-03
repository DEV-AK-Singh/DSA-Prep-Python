def print_formatted(number):
    width = len(bin(number)[2:]) 
    for i in range(1, number+1):
        dec_num = i
        oct_num = oct(i)[2:]
        hex_num = hex(i)[2:].upper()
        bin_num = bin(i)[2:]
        print(f"{str(dec_num).rjust(width)} {str(oct_num).rjust(width)} {str(hex_num).rjust(width)} {str(bin_num).rjust(width)}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)