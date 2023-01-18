https://github.com/reza1615/PersianOcr

Steps to reproduce this test:

First install tesseract
Copy lastest try per.* files to tessdata folder of installed tesseract
Make an png input image using arial font. Try to run boxmaker and make from it or simply make your image with 40px font size.
Copy your png here and run PngTiff.exe to have .tiff file (You must have .NET 3.5 or Windows 7 or later to run it)
Run tesseract with this command: tesseract Gho-Wikipedia.tiff output -l per
Now you may have your output file :)

