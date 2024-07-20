# Domain Checker 

**This Python script automates the process of checking the availability of domain names from a specified website. It uses threading for concurrent requests, BeautifulSoup for HTML parsing, and handles both accepted and denied domain names.**


## Features

* Random Domain Generation: Generates random domain names of a specified length using an alphabet list.

* Concurrent Requests: Utilizes threading to perform multiple domain checks simultaneously.

* Result Logging: Logs accepted and denied domain names to the console and saves accepted ones to a file.

* Customizable: Allows customization of the domain name length and the number of concurrent threads.


## Usage

Set your authorization cookie in the **AUTH_COOKIE** variable.
Adjust **DOMAIN_LEN** to set the length of the domain names.
Run the script to start checking domain names.

