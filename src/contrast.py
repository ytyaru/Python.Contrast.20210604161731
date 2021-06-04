#!/usr/bin/env python3
# coding: utf8
# 2色のコントラストを返す。4.5以上なら見やすい。
# https://ja.wikipedia.org/wiki/Help:%E9%85%8D%E8%89%B2%E3%81%AE%E3%82%B3%E3%83%B3%E3%83%88%E3%83%A9%E3%82%B9%E3%83%88%E6%AF%94
def contrast(*args):
    if 1 < len(args):
        if args[1] == 0: return '0;0;0'
        if args[1] == 1: return '255;255;255'
        lum1 = _contrast(args[0])
        lum2 = _contrast(args[1])
        def test(high, low): return (high + 0.05) / (low + 0.05)
        return test(lum1, lum2) if lum1 > lum2 else test(lum2, lum1)
    else: return rgb2luminance(**args[0].split(','));

def _contrast(color):
    return rgb2luminance(color.split(','));

def rgb2luminance(rgb):
    r = luminance_x(int(rgb[0]))
    g = luminance_x(int(rgb[1]))
    b = luminance_x(int(rgb[2]))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def luminance_x(x):
    x /= 255;
    return (x/12.92) if x <= 0.03928 else pow((x+0.055)/1.055, 2.4)

if __name__ == "__main__":
    import sys
    print('%f' % contrast(sys.argv[1], sys.argv[2]))

