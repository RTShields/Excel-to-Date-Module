# Excel-to-Date-Module
A python 3.0 module to convert dates between Excel and Gregorian format

There are two functions to this module for now.

<p><b>1.) X2D(number, format, doubling)</b>
<br>The number, being MS Excel's numeric value for any date past 12/31/1899. This function will calculate the Gregorian date in one one of the given formats:
<ul>
  <li>Option 1: MM/DD/YYYY (Default)</li>
  <li>Option 2: MM/DD/YY</li>
  <li>Option 3: YYYY/MM/DD</li>
  <li>Option 4: YY/MM/DD</li>
</ul>
<p>By default, the doubling of single digitis via string is set to True, input False to switch off.

<p><i>1.2) Sub function: Doubling Digit</i>
<br>For the shake of aesthics, should any of the digits be less than ten (10), a zero (0) will be concatenated before the digit when placed in the final string.

<p><b>2.) D2X(date)</b>
<br>This will date a given Gregorian Date in either MM/DD/YYYY, MM/DD/YY, YYYY/MM/DD, or YY/MM/DD format, and convert it into the Excel numeric format.
<br> Examples: 1/1/1900 will be converted to 1, 12/25/2000 gets converted to 36885

