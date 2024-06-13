Shell Script (DownloadFromTextFile.sh)

Description:
  The shell script download_files.sh is designed to download files listed in a text file containing URLs. 
  It utilizes the wget command-line utility to perform the downloads.

Usage:
  Make sure you have wget installed on your system. If not, you can install it using your package manager (apt, yum, etc.).
  Place the URLs of the files you want to download in a text file, with each URL on a new line.
  Modify the input_file variable in the script to point to your text file containing the URLs.
  Run the script using the command
  bash DownloadFromTextFile.sh textfile.txt

Python Script (getCourseCatalogFromMit.py)
Description:
  The Python script download_mit_catalog.py is designed to download the MIT course catalog webpage and extract specific information using web scraping. It uses the requests library to fetch the webpage and Beautiful Soup for parsing HTML content.

Usage:
  Make sure you have Python installed on your system.
  Install the required libraries using pip
    pip install requests beautifulsoup4
  Run the script using the command
    python getCourseCatalogFromMit.py
  The script will fetch the MIT course catalog webpage, extract the desired information, and save it to an output file.

Author 
  Kirubel Awoke 

Contact 
   leburikplc@gmail.com

