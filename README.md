# Voucher-Generator
Run the script without any arguments to generate a wordlist with the default settings (100,000 mixed-case words of length 6 without a prefix):

_python Voucher_generator.py_
Use the -h or --help argument to show the help message and available options:
_python wordlist_generator.py --help_
Specify the number of words using the -n or --num-words argument. You can use 'k' for thousands and 'm' for millions:
_python wordlist_generator.py -n 500k_
Set the prefix using the -p or --prefix argument:

_python wordlist_generator.py -p GIFT_
Set the case of the wordlist using the -c or --case argument ('L' for lowercase, 'U' for uppercase, 'mix' for mixed case):

_python Voucher_generator.py -c U_

Set the total word length, including the prefix, using the -t or --word-length argument:

_python Voucher_generator.py -t 8_

You can combine multiple arguments as needed:

_python Voucher_generator.py -n 1m -p GIFT -c U -t 8_
This will generate a wordlist with 1 million uppercase words of length 8, with the prefix 'GIFT'.

The generated wordlist will be saved in a file named 'wordlist.txt' in the same directory as the script.
