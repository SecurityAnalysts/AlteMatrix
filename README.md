# AlteMatrix
================

This tool lets you convert strings and numbers between number bases (2, 8, 10 and 16) as well as ASCII text.
You can use the IP address analyzer to find out details on IPv4 and perform abbreviation as well as expansion on IPv6 addresses.It can also perform a two's complement calculation as well.

You can visit [CodingPeps](https://codingpeps.com) to learn more about how to use it.

## Installation
================

```bash
$ rm -rf AlteMatrix/
$ git clone https://github.com/Ir0n-c0d3X/AlteMatrix
$ cd AlteMatrix
$ python setup.py install

OR

$ pip install AlteMatrix
```

## Usage

**Windows**

```bat
> cd altematrix
> python AlteMatrix.py -h
```

**Linux**

```bash
$ cd altematrix
$ python3 AlteMatrix.py -h
```

### "converter" module
_$ python3 converter.py -h_

Call | Function
---- | --------
b2o, bin-oct | Convert binary to octal.
b2d, bin-dec | Convert binary to decimal.
b2h, bin-hex | Convert binary to hexadecimal.
b2t, bin-txt | Convert binary to ASCII text.
d2b, dec-bin | Convert decimal to binary.
d2o, dec-oct | Convert decimal to octal.
d2h, dec-hex | Convert decimal to hexadecimal.
d2t, dec-txt | Convert decimal to ASCII text.
o2b, oct-bin | Convert octal to binary.
o2d, oct-dec | Convert octal to decimal.
o2h, oct-hex | Convert octal to hexadecimal.
o2t, oct-txt | Convert octal to ASCII text.
h2b, hex-bin | Convert hexadecimal to binary.
h2o, hex-oct | Convert hexadecimal to octal.
h2d, hex-dec | Convert hexadecimal to decimal.
h2t, hex-txt | Convert hexadecimal to ASCII text.
udf, user-defined | Convert from any number base to another.
udt, udef-text | Convert from text to any number base or vice-versa.

**NOTE:** No arguments are required when function involves conversion of text or udf/udt.

### "ipanalyzer" module
_$ python3 ipanalyzer.py -h_

ipv4 - Perform analysis on IPv4 addresses.

ipv6 - Perform analysis on IPv6 addresses.

        options: [-a, --abbreviate]   Abbreviate full length IPv6 addresses.
                 [-e, --expand]   Expand shortened IPv6 addresses.

### "2comp" module
*$ python3 twos_complement.py -h*

com2 - Perform two's complement test on a number with a multiplier.

To convert back to final decimal result:

**Windows**
```bat
> cd twos_complement/final-convert_win32.exe
```

**Linux**
```bash
$ cd twos_complement/
$ chmod 777 final-convert.out
$ ./final-convert.out
```

## Support Teams
* CodingPeps - [https://www.codingpeps.com](https://www.codingpeps.com/) 
* [BrownBear](https://github.com/Brown-Bear-2021)
* BearSec

Follow [@codingpeps](https://www.instagram.com/codingpeps/) 

:octocat:
