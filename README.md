# Voucher-Generator
Run the script without any arguments to generate a wordlist with the default settings (100,000 mixed-case words of length 6 without a prefix):

Use the -h or --help argument to show the help message and available options:

    python wordlist-Generator.py --help

Specify the number of words using the -n or --num-words argument. You can use 'k' for thousands and 'm' for millions:

    python wordlist-Generator.py -n 500k
    

OUTPUT

            oeC
            aJs
            jGH
            cSY
                496k more :)

Set the prefix using the -p or --prefix argument:

    python Voucher-Generator.py -p GIFT

OUTPUT

        GIFTdwL
        GIFTkgl
        GIFTmNQ
        GIFTrnH
        GIFTwEU
        GIFTjI5
        GIFTyeh
        GIFTt5c
Set the case of the wordlist using the -c or --case argument ('L' for lowercase, 'U' for uppercase, 'mix' for mixed case):

    python Voucher-Generator.py -c U -p ABC

OUTPUT

        ABCA8JI
        ABCKTV
        ABCHX4
        ABCA8JF
        ABCA7C
        ABCVHP
        ABCAWJW
        ABC0RY
        ABCAP4Z
        ABCALA5

Set the total word length, including the prefix, using the -t or --word-length argument:

    python Voucher-Generator.py -t 8
OUTPUT

        bwMcILlm
        jAn14aue
        TBNeTFFj
        RVcEsKNO
        ATBmwHSc
        WbxOcyvw
You can combine multiple arguments as needed:

    python Voucher-Generator.py -n 1m -p GIFT -c U -t 8
OUTPUT

        GIFTFJRN
        GIFTVIQ8
        GIFT6JRQ
        GIFTBMIT
        GIFTPBMJ
        GIFTT9QW
This will generate a wordlist with 1 million uppercase words of length 8, with the prefix 'GIFT'.

You can also use the -hp and -hr arguments to control the placement of hyphens in the generated wordlist.

    python Voucher-Generator.py -n 50k -p GIFT -t 10 -w a -o gift_vouchers.txt -hp 3,5
OUTPUT

        GIF-T-NcuM
        GIF-T-WRbw
        GIF-T-CTZD
        GIF-T-qWLr
        GIF-T-ngRk
        GIF-T-cMuk
        GIF-T-xhKb

    python Voucher-Generator.py -n 50k -p GIFT -t 10 -w a -hr 3 -o wordlist.txt
OUTPUT

        GIF-TZZ-fa
        GIF-TZC-eU
        GIF-Tbv-qb
        GIF-TYh-vZ
        GIF-TiT-xT
        GIF-TQT-aQ
        GIF-Tmr-zR
        GIF-TDs-Aa
The generated wordlist will be saved in a file named 'wordlist.txt' in the same directory as the script.
