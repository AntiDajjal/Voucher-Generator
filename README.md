# Voucher-Generator
Run the script without any arguments to generate a wordlist with the default settings (100,000 mixed-case words of length 6 without a prefix):

Use the -h or --help argument to show the help message and available options:

    python wordlist_generator.py --help

Specify the number of words using the -n or --num-words argument. You can use 'k' for thousands and 'm' for millions:

    python wordlist_generator.py -n 500k

Set the prefix using the -p or --prefix argument:

    python wordlist_generator.py -p GIFT

Set the case of the wordlist using the -c or --case argument ('L' for lowercase, 'U' for uppercase, 'mix' for mixed case):

    python Voucher_generator.py -c U

Set the total word length, including the prefix, using the -t or --word-length argument:

    python Voucher_generator.py -t 8

You can combine multiple arguments as needed:

    python Voucher_generator.py -n 1m -p GIFT -c U -t 8

This will generate a wordlist with 1 million uppercase words of length 8, with the prefix 'GIFT'.

You can also use the -hp and -hr arguments to control the placement of hyphens in the generated wordlist.

    python Voucher-Wordlist-Generator.py -n 50k -p GIFT -t 10 -w a -o gift_vouchers.txt -hp 3,5

The generated wordlist will be saved in a file named 'wordlist.txt' in the same directory as the script.
