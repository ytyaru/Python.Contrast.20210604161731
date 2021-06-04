#!/usr/bin/env python3
# coding: utf8
# 2色のコントラストを返す。4.5以上なら見やすい。
# https://ja.wikipedia.org/wiki/Help:%E9%85%8D%E8%89%B2%E3%81%AE%E3%82%B3%E3%83%B3%E3%83%88%E3%83%A9%E3%82%B9%E3%83%88%E6%AF%94
def contrast(color1, color2):
    lum1 = rgb2luminance(color1.split(','))
    lum2 = rgb2luminance(color2.split(','))
    def test(high, low): return (high + 0.05) / (low + 0.05)
    return test(lum1, lum2) if lum1 > lum2 else test(lum2, lum1)

def rgb2luminance(rgb):
    r = luminance_x(int(rgb[0]))
    g = luminance_x(int(rgb[1]))
    b = luminance_x(int(rgb[2]))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def luminance_x(x):
    x /= 255;
    return (x/12.92) if x <= 0.03928 else pow((x+0.055)/1.055, 2.4)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='2色のコントラスト比を返す。')
    parser.add_argument('color1', help='色1。R,G,Bのようにカンマ区切りで渡す。0<=R,G,B<=255')
    parser.add_argument('color2', help='色2。R,G,Bのようにカンマ区切りで渡す。0<=R,G,B<=255')
    args = parser.parse_args()
    print('%f' % contrast(args.color1, args.color2))

