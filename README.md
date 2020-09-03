# Certificate Generator for IIIT Vadodara

Works with python 3.x

Steps to run

1) Install pygame and Pillow using  - 
```console
foo@bar:~$ pip install pygame
foo@bar:~$ pip install Pillow
```

2) There are 2 files which you have to make, one is the csv file which contains all the entries, and second is an image of the certificate.
 The sample files are```test.csv``` and ```certificate.jpg```
3) Use any name for the csv, but keep the name of the jpeg as certificate.jpg
4) Run the ```generator.py``` file using - 
```console
foo@bar:~$ python generator.py
```
6) Enter the name of the file, the event name and the year when prompted
7) Once the new file is generated, a window will open in your screen, which will display your certificate.
8) Drag the text fields to wherever you would like to place them  
9) Once the fields are set, press enter. The program will automatically close when all certificates are generated.
10) See the generated certificates in the 'certificates' folder. Each certificate will be named after the roll number of the receipient.

# Things to take care of
The first two columns of the csv should be the roll number and the name. That is mandatory
