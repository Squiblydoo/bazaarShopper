#!/usr/bin/python


# Pulls samples from MalwareBazaar for Jupyter malware

import requests
import json
import argparse
import os
import pyzipper
from pathlib import Path

parser = argparse.ArgumentParser(description = "Pull samples from MalwareBazzar by specifying tag associated with the malware and the number of samples to download. If no number is specified the default 50 samples will be used. ")
parser.add_argument("tag", help="Specify the tag used on MalwareBazaar to identify the malware to download.")
parser.add_argument("--limit", "-l", default="50", type=int, help="Specify the maximum limit for pulling samples. Default is 50")
parser.add_argument("--sample_directory", "-s", default=".", help="Specify a directory for saving the samples. Defaults to current directory.")
parser.add_argument("--unzip", "-u",  help="Specify a directory  for saving unzipped samples. Defaults to creating a directory named Unzipped.")
parser.add_argument("--password", "-p", default="infected", help="Specify a password for unzipping files. Defaults to 'infected'")
args = parser.parse_args()

#Make request for Data
query = {"query": "get_taginfo", "tag": args.tag, "limit": args.limit}
dataRequest = requests.post("https://mb-api.abuse.ch/api/v1/", data=query)

#Throw error if request did not complete successfully
dataRequest.raise_for_status()

#Convert response to form usable by python script
jsonString = dataRequest.text
jsonPythonValue = json.loads(jsonString)

#Save the current directory incase we need it later
cwd = os.getcwd()

# If a directory was specified for saving samples, check if it exists. If it does not exist
# create the directory and then move into the directory.
if (args.sample_directory != None):
    if (os.path.isdir(args.sample_directory) != True):
         os.mkdir(args.sample_directory)
    os.chdir(args.sample_directory)

resultsSHA = []
for i in range(len(jsonPythonValue["data"])):
    resultsSHA.append(jsonPythonValue["data"][i]["sha256_hash"])
    query = {"query": "get_file", "sha256_hash": jsonPythonValue["data"][i]["sha256_hash"] }
    fileRequest = requests.post("https://mb-api.abuse.ch/api/v1/", data=query)
    filetosave = open(jsonPythonValue["data"][i]["sha256_hash"], "wb")
    filetosave.write(fileRequest.content)
    filetosave.close()

if (args.unzip != None):
    if (os.getcwd != cwd):
        os.chdir(cwd)
    for zippedfile in os.listdir(args.sample_directory):
        with pyzipper.AESZipFile(args.sample_directory + "\\"+ zippedfile, 'r') as zf:
            zf.pwd = bytes(args.password, "UTF-8")
            zf.extractall(args.unzip)

