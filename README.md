# HexImage
HexImage - new innovation image format.
No signature. No blocks. Only pixels.

## HexImage 1.0
Only print pixels. In file ordinary text separated of spaces.

## HexImage 2.0
Only print pixels too. In file text with length and color. For example:

Two red pixels in a row:
```2,ff0000```

Pixels also separated of spaces.

## HexImage 2.1 (In developing)
New ability: add to file transparent pixels.
They have a special code, which not hexadecimal color.

## HexImage 3.0 (In mega-long-developing)
File will not ordinary text, file will colors from bytes.
Every color - 3 bytes:

First byte - red channel
Second byte - green channel
Third byte - blue channel

In start every HI-file will 8 bytes of size:
4 bytes - width
4 bytes - height




Created with (Rich)[https://github.com/Textualize/rich?tab=readme-ov-file]
