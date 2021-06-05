#!/usr/bin/env python3
# coding: utf8
# 引数の色が白系なら0を返し、黒系なら1を返す。返される白／黒のコントラスト値が指定したレベルやコントラスト値より低ければ2を返す。
# is_whitish_level.py -l 3 128,128,128 && echo 'W' || echo "B$?"    # B2
# is_whitish_level.py -l 3 0,0,0 && echo 'W' || echo "B$?"          # B1
# is_whitish_level.py -l 3 255,255,255 && echo 'W' || echo "B$?"    # W
# contrast.py 128,128,128 0,0,0        # 5.317210
# contrast.py 128,128,128 255,255,255  # 3.949440
if __name__ == "__main__":
    import argparse, contrast
    parser = argparse.ArgumentParser(description='引数の色が白系なら0を返し、黒系なら1を返す。色は第一引数にてRGB値(255,255,255)形式で受け付ける。')
    parser.add_argument('rgb', help='色。R,G,Bのようにカンマ区切りで渡す。0<=R,G,B<=255')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-l', '--level', type=int, default=0, help='保障レベル。1,2,3(A,AA,AAA)のいずれかを指定する。')
    group.add_argument('-c', '--contrast', type=float, default=0, help='保障コントラスト値')
    args = parser.parse_args()
    if '1' == args.level or 'A' == args.level: args.level = 1
    elif '2' == args.level or 'AA' == args.level: args.level = 2
    elif '3' == args.level or 'AAA' == args.level: args.level = 3
    else: args.level = 0
    con0 = contrast.contrast(args.rgb, '0,0,0')
    con1 = contrast.contrast(args.rgb, '255,255,255')
    def jadge_level():
        if 0 < args.level:
            import contrast_level
            actual = contrast_level.contrast_level(max(con0, con1))
            expected = args.level
            if actual < expected: exit(2)
    def jadge_contrast():
        if 0 < args.contrast:
            if max(con0, con1) < args.contrast: exit(2)
    jadge_level()
    jadge_contrast()
    exit(0) if con0 > con1 else exit(1)

