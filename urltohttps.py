# how to run : python3 urltohttps.py -list list.txt
import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description="Add 'https://' to a list of URLs.")

# Add an argument for the input 
parser.add_argument("-list", type=str, help="Input filename URLS")

args = parser.parse_args()

# Check '-list' 
if args.list:
    # Read the list of URLs
    with open(args.list, "r") as file:
        urls = file.readlines()

    # Strip any leading or trailing whitespace and add "https://"
    https_urls = ["https://" + url.strip() if not url.startswith(("http://", "https://")) else url.strip() for url in urls]

    # Print the updated URLs
    for url in https_urls:
        print(url)
else:
    print("Please provide with using the '-list' argument.")
######################### 0xs4m #########################

