#!/usr/bin/env python3
# coding: utf8
# 引数の色が白系なら0を返し、黒系なら1を返す。
if __name__ == "__main__":
    import argparse, contrast
    parser = argparse.ArgumentParser(description='引数の色が白系なら0を返し、黒系なら1を返す。色は第一引数にてRGB値(255,255,255)形式で受け付ける。')
    parser.add_argument('rgb', help='色。R,G,Bのようにカンマ区切りで渡す。0<=R,G,B<=255')
    args = parser.parse_args()
    lum0 = contrast.contrast(args.rgb, '0,0,0')
    lum1 = contrast.contrast(args.rgb, '255,255,255')
    exit(0) if lum1 < lum0 else exit(1)

