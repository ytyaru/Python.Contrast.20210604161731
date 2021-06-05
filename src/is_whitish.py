#!/usr/bin/env python3
# coding: utf8
# 引数の色が白系なら0を返し、黒系なら1を返す。返される白／黒のコントラスト値が指定したレベルやコントラスト値より低ければ2を返す。
if __name__ == "__main__":
    import argparse, contrast
    parser = argparse.ArgumentParser(description='引数の色が白系なら0を返し、黒系なら1を返す。色は第一引数にてRGB値(255,255,255)形式で受け付ける。')
    parser.add_argument('rgb', help='色。R,G,Bのようにカンマ区切りで渡す。0<=R,G,B<=255')
    parser.add_argument('-l', '--level', help='保障レベル。1,2,3(A,AA,AAA)のいずれかを指定する。')
    parser.add_argument('-c', '--over-contrast', help='保障コントラスト値')
    args = parser.parse_args()
    con0 = contrast.contrast(args.rgb, '0,0,0')
    con1 = contrast.contrast(args.rgb, '255,255,255')
    exit(0) if con0 > con1 else exit(1)

