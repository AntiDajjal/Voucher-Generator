import argparse
import itertools
import string

def generate_wordlist(prefix, num_words, case, total_length, charset, hyphen_placements, hyphen_repetitive):
    if case == 'L':
        charset = charset.lower()
    elif case == 'U':
        charset = charset.upper()
    
    max_generated_length = total_length - len(prefix) - len(hyphen_placements)
    
    words = set()
    for combination in itertools.product(charset, repeat=max_generated_length):
        word = prefix + ''.join(combination)
        
        if hyphen_placements:
            for placement in hyphen_placements:
                if placement < len(word):
                    word = word[:placement] + '-' + word[placement:]
        
        if hyphen_repetitive:
            word_parts = [word[i:i+hyphen_repetitive] for i in range(0, len(word), hyphen_repetitive)]
            word = '-'.join(word_parts)
        
        if len(word) == total_length:
            words.add(word)
            if len(words) == num_words:
                return words
    
    return words

def parse_num_words(num_words_str):
    num_words_str = num_words_str.lower()
    if num_words_str.endswith('k'):
        num_words = float(num_words_str[:-1]) * 1000
    elif num_words_str.endswith('m'):
        num_words = float(num_words_str[:-1]) * 1000000
    else:
        num_words = int(num_words_str)
    return int(num_words)

def main():
    parser = argparse.ArgumentParser(description='Voucher Wordlist Generator')
    parser.add_argument('-n', '--num_words', type=str, default='100k', help='Number of words in wordlist (e.g. 100, 100k, 10000k, 1m)')
    parser.add_argument('-p', '--prefix', type=str, default='', help='Prefix for each word')
    parser.add_argument('-c', '--case', type=str, default='', choices=['L', 'U'], help='L for lowercase, U for uppercase, By Default it contains Both')
    parser.add_argument('-t', '--total_length', type=int, default=8, help='Total number of characters in each word including prefix and hyphens')
    parser.add_argument('-w', '--charset', type=str, default='an', choices=['a', 'n', 'an'], help='a for alphabet, n for numbers, an for both')
    parser.add_argument('-o', '--output', type=str, default='wordlist.txt', help='Output file name')
    parser.add_argument('-hp', '--hyphen_placements', type=str, default='', help='Comma-separated list of hyphen placements (e.g. 3,5)')
    parser.add_argument('-hr', '--hyphen_repetitive', type=int, default=0, help='Add hyphen after every N characters')
    
    parser.epilog = "Sample Usage:\npython Voucher-Wordlist-Generator.py -n 50k -p GIFT -t 13 -w a -o gift_vouchers.txt -hp 3,5,8"
    
    args = parser.parse_args()
    
    num_words = parse_num_words(args.num_words)
    prefix = args.prefix
    case = args.case if args.case else ''
    total_length = args.total_length
    output_file = args.output
    hyphen_placements = [int(p) for p in args.hyphen_placements.split(',')] if args.hyphen_placements else []
    hyphen_repetitive = args.hyphen_repetitive
    
    if args.charset == 'a':
        charset = string.ascii_letters
    elif args.charset == 'n':    
        charset = string.digits
    else:
        charset = string.ascii_letters + string.digits
    
    wordlist = generate_wordlist(prefix, num_words, case, total_length, charset, hyphen_placements, hyphen_repetitive)
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(wordlist))
    
    print(f"Generated {len(wordlist)} words and saved to {output_file}")

if __name__ == '__main__':
    main()
