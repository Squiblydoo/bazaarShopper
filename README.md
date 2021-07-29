# bazaarShopper
A script for downloading malware samples from MalwareBazaar.


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
