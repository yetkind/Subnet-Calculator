# Simple Python Subnet Calculator

This Python script provides a basic command-line tool for network subnetting tasks. It allows you to analyze an existing IP network or calculate subnetting parameters based on host and subnet requirements.

## Features

* **Analyze Network:** Enter an IP address with CIDR notation (e.g., `192.168.1.0/24`) to see details like network address, broadcast address, subnet mask, usable host range, and more.
* **Calculate Subnets:** Specify the required number of subnets and the minimum number of hosts per subnet. The script will calculate the appropriate subnet mask (CIDR) and list the first few resulting subnets based on an optional starting network.

## Requirements

* Python 3.x
* The `ipaddress` module (usually included in standard Python libraries).
* The `math` module (usually included in standard Python libraries).

## How to Run

1.  Save the code as a Python file (e.g., `subcal.py`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script using the command:

    ```bash
    python subcal.py
    ```
5.  Follow the on-screen menu prompts to choose between analyzing a network or calculating subnets.

PS: it is not perfect, but it is better than pen and paper enjoy! - Yetkin
