#!/usr/bin/env python3
# coding: utf8
# コントラストレベルを返す。
# https://ja.wikipedia.org/wiki/Help:%E9%85%8D%E8%89%B2%E3%81%AE%E3%82%B3%E3%83%B3%E3%83%88%E3%83%A9%E3%82%B9%E3%83%88%E6%AF%94
if __name__ == "__main__":
    import argparse, contrast
    from argparse import RawTextHelpFormatter
    description = '''コントラストレベルを返す。
  contrast  level(n,a,w)
  1.0~      0  D 
  3.0~      1  C  A
  4.5~      2  B  AA
  7.0~      3  A  AAA
'''
    parser = argparse.ArgumentParser(description=description, formatter_class=RawTextHelpFormatter)
    parser.add_argument('contrast', type=float, help='コントラスト比。0~21までの実数値。')
    parser.add_argument('-t', '--output-type', default='number', choices=['n', 'a', 'w', 'number', 'alphabet', 'w3c'], help='戻り値の種類。')
    args = parser.parse_args()
    if 'n' == args.output_type: args.output_type = 'number'
    if 'a' == args.output_type: args.output_type = 'alphabet'
    if 'w' == args.output_type: args.output_type = 'w3c'
    def level():
        if args.contrast < 3.0 and args.output_type == 'number': return '0'
        if args.contrast < 3.0 and args.output_type == 'alphabet': return 'D'
        if args.contrast < 3.0 and args.output_type == 'w3c': return ' '
        if args.contrast < 4.5 and args.output_type == 'number': return '1'
        if args.contrast < 4.5 and args.output_type == 'alphabet': return 'C'
        if args.contrast < 4.5 and args.output_type == 'w3c': return 'A'
        if args.contrast < 7.0 and args.output_type == 'number': return '2'
        if args.contrast < 7.0 and args.output_type == 'alphabet': return 'B'
        if args.contrast < 7.0 and args.output_type == 'w3c': return 'AA'
        if 7.0 <= args.contrast and args.output_type == 'number': return '3'
        if 7.0 <= args.contrast and args.output_type == 'alphabet': return 'A'
        if 7.0 <= args.contrast and args.output_type == 'w3c': return 'AAA'
        raise Error('プログラムエラー。')
    print(level())

