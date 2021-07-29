# bazaarShopper
## Instructions of how to use
A script for downloading malware samples from [MalwareBazaar](https://bazaar.abuse.ch/).

      Usage: bazaarShopper.py [-h] [--limit LIMIT] [--sample_directory SAMPLE_DIRECTORY] tag

Pull samples from MalwareBazzar by specifying tag associated with the malware and the number of samples to download. If
no number is specified the default 50 samples will be used.



    positional arguments:


        tag                   Specify the tag used on MalwareBazaar to identify malware to download.

    optional arguments:

        -h, --help            show this help message and exit
        
        --limit LIMIT, -l LIMIT
                            Specify the maximum limit for pulling samples. Default is 50

        --sample_directory SAMPLE_DIRECTORY, -s SAMPLE_DIRECTORY
                            Specify a directory for saving the samples. Defaults to current directory.

## Setup
Windows:
Clone the repo and all the included files. Open a command prompt and install the requirements using the python module "pip" using the requirements file. Once requirements are installed, the script can be used.

      python -m pip install -r requirements.txt

Linux / Mac
Clone the repo and all the included files. Open a terminal session and install the requirements using the python3 module "pip" using the requirements file. Once requirements are installed, the script can be used.

      python3 -m pip install -r requirements.txt
      
## Example
The following example will download 10 of the latest samples tagged as "Jupyter" and save them to a direcotry named "SampleDirectory". If SampleDirectory does not exist, it will be created.

    python bazaarShopper.py Jupyter -l 10 -s SampleDirectory
