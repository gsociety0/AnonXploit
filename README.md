<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="author" content="gsociety">
    </head>
    <body>
        <h1>AnonXploit</h1>
        <p>
            <img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Awesome">
            <img src="https://badges.frapsoft.com/os/v1/open-source.svg" alt="Open Source Love">
            <a href="https://www.gnu.org/licenses/gpl-3.0"><img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="License: GPL v3"></a>
            <img src="https://coveralls.io/repos/boennemann/badges/badge.svg" alt="Encryption Status">
        </p>
        <h4>AnonXploit is a tool for pentesters, it can be used by organizations of all sizes, including individuals.</h4>
        <h4>It was developed with the purpose of exploiting the vulnerability of creating a reverse shell between the pentester and the injected computer. This tool can work without warnings about viruses and suspicious connections.</h4>
        <br>
        <div class="table_of_contents">
            <h2>📋 Table of Contents</h2>
            <p><a href="#supported_os">1. 💻 Compatible Operating Systems</a></p>
            <p><a href="#installation">2. 🔨 Installation</a></p>
            <p><a href="#how_to_use">3. 📡 How to Use</a></p>
            <p><a href="#code_analysis">4. ☑️ Code Analysis</a></p>
            <p><a href="#license">4. ©️ License</a></p>
        </div>
        <br>
        <div id="supported_os">
            <h2>💻 Supported Operating Systems</h2>
            <td><img src="https://img.shields.io/badge/OS-Linux%20%7C%20WSL%20%7C%20Termux-blue??style=flat&logo=Linux&logoColor=b0c0c0&labelColor=363D44" alt="Operating systems"/></td>
            <td colspan="2"><img src="https://img.shields.io/badge/CPU-x86__64%20%7C%20Arm%20-blue?style=flat&logoColor=b0c0c0&labelColor=363D44" alt="CPU Architect"/></td>
            <h4>We carried out the tests on systems based on Ubuntu, Debian and Termux. We believe it will also work on other systems, such as Fedora and Arch. The installation instructions are for Ubuntu/Debian and Termux only. If you don't know how to install on other operation system, google it.</h4>
        </div>
        <br>
        <div id="installation">
            <h2>🔨 Installation</h2>
            <h3>Installation for Debian/Ubuntu</h3>
            <h5>System Update</h5>
            <code>sudo apt update</code>
            <h5>Install Git</h5>
            <code>sudo apt install -y git</code>
            <h5>Download the Repository</h5>
            <code>git clone https://github.com/gsociety0/AnonXploit.git</code>
            <h5>Install AnonXploit</h5>
            <code>./install</code> or <code>bash ./install</code>
            <h3>Installation for Termux</h3>
            <h5>System Update</h5>
            <code>pkg update</code>
            <br>
            <code>pkg full-upgrade -y</code>
            <h5>Install Git</h5>
            <code>pkg install -y git</code>
            <h5>Install Python3</h5>
            <code>pkg install -y python python-pip</code>
            <h5>Download the Repository</h5>
            <code>git clone https://github.com/gsociety0/AnonXploit.git</code>
            <h5>Install AnonXploit</h5>
            <code>./install</code> or <code>bash ./install</code>
        </div>
        <br>
        <div id="how_to_use">
            <h2>📡 How to Use</h2>
            <h4>To create the RAT you need to run two programs, client.py and server.py. Where the client will automatically create the RAT, and the server will wait for the connection.</h4>
            <h5>client.py</h5>
            <code>python3 client.py</code>
            <h5>server.py</h5>
            <code>python3 server.py</code>
        </div>
        <br>
        <div id="code_analysis">
            <h2>☑️ Code Analysis</h2>
            <h4>If you check the source code of each AnonXploit file, you will notice that the code is obfuscated. This is done for security reasons and compatibility with WSL (Windows Subsystem for Linux), where the antivirus detected the files as viruses and deleted them.</h4>
            <h3>🔬 Virus Total</h3>
            <h4>install file:</h4>
            <img src="./src/img/install.png">
            <br>
            <h4>client.py file (91% undetectable):</h4>
            <img src="./src/img/client.png">
            <br>
            <h4>server.py file:</h4>
            <img src="./src/img/server.png">
            <br>
            <br>
            <p><b>DON'T UPLOAD THE RAT FILE TO VIRUS TOTAL!</b></p>
            <h4>The RAT bypasses Windows Defender antivirus. <b>(Information verified until 1/28/2024)</b></h4>
            <h4>"Files and URLs sent to VirusTotal will be shared with antivirus vendors and security companies..."</h4>
            <h6>Source: <a href="https://en.wikipedia.org/wiki/VirusTotal">Wikipedia</a></h6>
        </div>
            <br>
            <div id="license">
            <h2>©️ License</h2>
            <h4>This project is licensed under the <a href="https://choosealicense.com/licenses/agpl-3.0/">GNU Affero General Public License v3.0</a></h4>
            <h4>✅ Permission:</h4>
            <li>Patent use;</li>
            <li>Commercial use;</li>
            <li>Private use;</li>
            <li>Distribution;</li>
            <li>Modification.</li>
            <h4>✒️ Conditions:</h4>
            <li>Same license;</li>
            <li>Disclose source;</li>
            <li>License and copyright notice;</li>
            <li>Network use is distribution;</li>
            <li>State changes.</li>
            <h4>⚠️ Limitations:</h4>
            <li>Liability;</li>
            <li>Warranty.</li>
        </div>
    </body>
</html>
