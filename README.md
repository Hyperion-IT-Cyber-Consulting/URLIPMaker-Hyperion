# URLIPMaker-Util

Welcome to the URLIPMaker-Util! This utility program is designed to generate URLs for various IP lookup services based on a user-provided IP address. The program validates the IP address format and then constructs URLs for services such as Whois, SecurityTrails, MXToolbox, and AbuseIPDB.

## Table of Contents

- [About The Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)
- [Author](#author)
- [Acknowledgments](#acknowledgments)

## About The Project

URLIPMaker-Util is a simple command-line tool that helps users generate URLs for IP lookup services. It ensures that the provided IP address is valid and then constructs URLs for various services to check the IP address.

## Features

- **IP Address Validation**: Ensures the entered IP address is in the correct format.
- **URL Generation**: Constructs URLs for multiple IP lookup services.
- **Interactive Command Line Interface**: User-friendly interface for entering IP addresses and viewing results.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. **Clone the repo**:
   git clone https://github.com/your_username/URLIPMaker-Util.git
   cd URLIPMaker-Util
2. **Run the Program**:
    python urlipmaker_util.py
   
### Usage
    Enter an IP Address:
    The program will prompt you to enter an IP address in the format *.*.*.*.
    Example: 192.168.1.1
    If the IP address is valid, the program will display URLs for the following services:
    Whois
    SecurityTrails
    MXToolbox
    AbuseIPDB
    Exit the Program:
    Type quit to exit the program.
### example
    $ python urlipmaker_util.py
    Welcome to the URLIPMaker-Util!

    Please enter an IP address (*.*.*.* format) or 'quit' to exit: 192.168.1.1

    Generated URLs:
    https://www.whois.com/whois/192.168.1.1
    https://securitytrails.com/list/ip/192.168.1.1
    https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a192.168.1.1&run=toolpage
    https://www.abuseipdb.com/check/192.168.1.1

    Press Enter to continue...

### License
    This uses the GPL 3.0 License, which can be viewed in the repo

### Author
    Nate P. Principal Consultant

### Acknowledgments
    Whois lookup service: Whois.com
    SecurityTrails: SecurityTrails.com
    MXToolbox: MXToolbox.com
    AbuseIPDB: AbuseIPDB.com
