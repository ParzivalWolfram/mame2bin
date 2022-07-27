# mame2bin

Program released under the MIT license, see https://opensource.org/licenses/MIT
or https://web.archive.org/web/20220726165438/https://opensource.org/licenses/MIT

Usage: `mame2bin <input dump> <output binary>`

this takes the MAME text hex dump format, eg:

```
0000:  00 00 F3 C3 15 00 25 00 DD 2B DD 70 00 DD 2B DD  ......%..+.p..+.
0010:  71 00 C1 FD E9 F3 ED 46 01 F4 00 ED 41 79 D6 01  q......F....Ay..
0020:  4F D2 1B 00 3E 01 D3 08 01 15 00 ED 78 0E 14 ED  O...>.......x...
etc.
```

and converts to a raw dump, which can be manipulated in a hex editor or similar.
I tried to keep this short and sweet, as it has a very simple job to do.
