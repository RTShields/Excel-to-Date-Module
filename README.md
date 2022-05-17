# Excel-to-Time-Module
A python 3.0 module to convert dates between Excel and Gregorian format

There are two functions to this module for now.

1.) X2T(number, format, doubling)
The number, being MS Excel's numeric value for any date past 12/31/1899. This function will calculate the Gregorian date in one one of the given formats:
Option 1: MM/DD/YYYY (Default)
Option 2: MM/DD/YY
Option 3: YYYY/MM/DD
Option 4: YY/MM/DD

2.) T2X(date)
This will date a given Gregorian Date (in any format listed in X2T's options), and calculate the MS Excel's numeric value for it.

1.2) Sub function: Doubling Digit
For the shake of aesthics, should any of the digits be less than ten (10), a zero (0) will be concatenated before the digit when placed in the final string. This is set as the default setting
