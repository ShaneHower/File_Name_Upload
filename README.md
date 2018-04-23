# File_Name_Upload
This script will take the all of the file names in a folder and upload them onto an excel spreadsheet. 
## Before Starting 
you will need to download Anaconda with python 3.  This includes python 3 along with many great packages used in data analysis. 
Follow the link to download: https://www.anaconda.com/download/

## Download and Run
First click the green "clone/download" button in the top right of the repository.  once you've downloaded the zip open your command prompt. Type these commands
```
> python 
>>> from XL_Sync import XLSync 
>>> XLSync("/../../desired_path","name_of_the_file").execute()
```

