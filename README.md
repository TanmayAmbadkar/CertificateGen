# Certificate Generator for IIIT Vadodara

Works with python 3.x

Steps to run

1) Install pygame and Pillow using  - 
```console
foo@bar:~$ pip install pygame
foo
```
```console
foo@bar:~$ pip install Pillow
foo
```
 
2) There are 2 files which you have to make, one is the csv file which contains all the entries, and second is an image of the certificate.
 The sample files are test.csv and certificate.jpg
3) Use any name for the csv, but keep the name of the jpeg as certificate.jpg
4) Open the CertiGen.py file and read the docstring to know more about how to change fonts, size etc
5) Run the CertiGen.py file using - 
```console
foo@bar:~$ python CertiGen.py
foo
```
6) Enter the name of the file, the event name and the year when prompted
7) Once the new file is generated, a window will open in your screen, which will display your certificate.
8) Draw a rectangle wherever you want the field to be displayed. See the generated.csv to know what fields are available for drawing.
9) Once done drawing, press enter. The program will automatically close when all certificates are generated.
10) See the generated certificates in the 'certificates' folder 
