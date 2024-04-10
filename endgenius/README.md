# EndGenius
<a name = "introduction"></a>

# Introduction #
#### GenAI backend for E2E team

# Table of Contents
**Getting Started**
* [Prerequisites](#prerequisites)
* [Python Environment Set Up](#environment)
* [Necessary Package Installing](#package)
* [Running the Server](#run)
* [Common Error](#error)

**Others**
* [Optimization](#optimization)
* [FrontEnd Set Up](#frontend)
* [Useful Reference](#reference)


# Getting Started #

<a name = "prerequisites"></a>

# Prerequisites #
* Download the Python extension in Visual Studio Code:
  * Click on 'Extensions'(⇧⌘X), search for 'Python', and install the one from Microsoft

<a name = "environment"></a>

# Python Environment Set Up #

* This section will talk about how to create a virtual environemnt for python in your local:

## Create the virtual environment through visual studio code: ##
  1. Open the Command Palette (⇧⌘P), search for the **Python: Create Environmen**t command, and select it.
  2. If you are creating an environment using Venv, the command presents a list of interpreters that can be used as a base for the new virtual environment.
  3. Choose the latest version of python( For now, I am using the **python 3.9.6**. We can make the arrangement for the python version if necessary )
  4. If you would prefer to select a specific environment after creation, use the **Python: Select Interpreter** command from the Command Palette (⇧⌘P).
    
  ```Difference between conda and venv: ```
  * They are both python environment tool.
  * **Venv**:Allows you to manage separate package installations for different projects and is installed with Python 3 by default (unless you are on a Debian-based OS; install python3-venv in that case)
  * **conda**	Installed with **Miniconda**. It can be used to manage both packages and virtual environments. Generally used for data science projects.
  * **Reference**:https://code.visualstudio.com/docs/python/environments

## Create the virtual environment through terminal: ##
``` Note: This part hasn't been tested on my local, let me know if there is any issues```
* If you choose to create a virtual environment manually, use the following command (where ".venv" is the name of the environment folder):
   ```bash 
  $ python3 -m venv .venv
  ``` 
  * You may need to run following command first on **Debian-based OSs**:
  ```bash 
  $ sudo apt-get install python3-venv
  ``` 


<a name = "package"></a>

# Necessary Package Installing #
1. Update the pip package manager for Python 3 to the latest version available.
  ```bash
  $ pip3 install --upgrade pip
  ```
2. Install the package for making HTTP requests in Python scripts or applications:
  ```bash
  $ pip3 install requests
  ```
3. Install the PyCryptodome that provides cryptographic functions and protocols.
  ```bash
  $ pip3 install pycryptodome==3.10.1
  ```
  * Note: if you have installed the pycrypto,uninstall it since we shouldn't have pycrypto and pycryptodome installed at the same time as they will interfere with each other
  ```bash
  $ pip3 uninstall pycrypto
  ```
4. (Optional) If python can't find the dependency, use **python interpreter** to select the **global** environment

5. Install the package for using Milvus, an open-source vector database.
  ```bash
  $ pip3 install pymilvus
  ```
  
<a name = "run"></a>

# Running the Server
* After installing everything, you should now be able to run it locally. Remember to turn the VPN on so that we can connect to the Walmart LLM gateway. You should see the response in your terminal.
 
# Others #
Some other information and notice outside of the server environmnt build.
 
<a name = "optimization"></a>

# Optimization
* Noting that the credentials are currently hardcoded into our repository, we should either use a third-party provider or save them more securely later by using a .env file

<a name = "frontend"></a>

# FrontEnd Set Up #
* User Interface (UI) for interacting with the application.
* Input fields for specifying parameters and requirements for the automation script.
* Button to trigger the generation of the automation script.
* Display area to show the generated script to the user.

<a name = "error"></a>

# Common Error #
* "ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with LibreSSL 2.8.3"
  * Reference: https://stackoverflow.com/questions/76187256/importerror-urllib3-v2-0-only-supports-openssl-1-1-1-currently-the-ssl-modu


<a name = "reference"></a>

# Reference #
* Security token: https://akeyless.gw.prod.glb.us.walmart.net:18888/items
* Walmart LLM Gateway: https://gecgithub01.walmart.com/MLPlatforms/elementGenAI/wiki/Walmart-LLM-Gateway
* Steps to develop an agent: https://dx.walmart.com/dxaibuilder/documentation/dx/Steps-to-Add-a-New-Data-Source-D0000000210?sso_redirect_ts=1711389790
* **E2E GenAI Architecture: https://confluence.walmart.com/display/CEGECEEA/E2E+GenAI+Architecture (In draft)**
* Sample code: https://gecgithub01.walmart.com/gist/s0m01up/9e63cd3a1b4445224c9519396c03f90e#L46
* Getting Walmart CA Certificates: https://gecgithub01.walmart.com/MLPlatforms/elementGenAI/tree/main/examples/langchain#getting-the-walmart-ca-certificates

