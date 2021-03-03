# AudioAnalyzer

Acquisition and plotting software for various audio analyzer.
The curent version support the folowing instruments
- HP 8903A/B

Any Audio Analyser with an GPIB interface can be added. 
Support for additional instrument will be added later :
- Panasonic VP7722P
- Neutrik TT402

The comunication is done using GPIB interface and PyVISA.

This software is currently only tested with Linux but should work on
Windows and Mac OS X as well.

This project was motivated by Pete Millett's HP 8903 software
(http://www.pmillett.com/hp_8903_software.htm) which only supports
Windows and Nicholas Nell's HP8903 software (https://github.com/cosmonaut/hp8903)

Dependencies
=====

* python (>= 3.2)
* matplotlib
* numpy
* wxPython
* pyvisa

Features
=====

* THD+n vs frequency
* Amplitude vs frequency
* Ratio-type sweeps
* Control of filters
* multi plotting 

Future features may include: 

* Save plots and raw data
* Generate standardised report
* THD+n vs Power and THD+n vs voltage.


