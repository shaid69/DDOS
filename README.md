
# DDoS

**DDoS** is a Python-based Distributed Denial of Service (DDoS) attack simulator. This tool is created for **educational purposes only** to demonstrate how DDoS attacks work in a controlled and ethical environment.

> **Important**: This tool is not intended for malicious use. Unauthorized use of this tool is illegal. You are solely responsible for how you use this tool. Use it at your own risk.

## Features

- **Target IP Simulation**: Attack a specified IP address.
- **Randomized Ports**: The attack sends packets over random ports between `1-65535`.
- **Loading & Progress Bar**: Displays a professional loading animation before starting the attack and shows the progress bar while the attack is running.
- **User-Friendly**: Colorful and interactive console output using `colorama` for better visualization.
- **Graceful Shutdown**: Handle user interruption (Ctrl+C) and any exceptions.

## Installation

### Prerequisites

- Python 3.x
- `colorama` library

### Installation Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/shaid69/DDOS.git
    cd DDOS
    ```

2. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Install `figlet` (for banner generation):

    **Linux / macOS**:
    ```bash
    sudo apt install figlet
    ```

    **Windows**:
    - Download and install [Figlet for Windows](https://github.com/cmatsuoka/figlet).
    
4. Run the script:

    ```bash
    python ddos.py
    ```

## Usage

1. **Launch the tool**: 
    ```bash
    python ddos.py
    ```

2. **Input the target IP address** when prompted.

3. The tool will start simulating the DDoS attack with a randomized port selection.

4. **Press Ctrl+C** to stop the attack.

---

## Example Output

```bash
Created By : Shaid Mahamud
Author     : shaid69
GitHub     : github.com/shaid69
Note: This tool is for educational purposes only. Use at your own risk.

Enter Target IP Address: 192.168.1.1

Team : shaid69
____________________________________________________________
[*] Trying to reach the server...
[*] Establishing connection...
[*] Bypassing security layers...
[✓] Connection established. Preparing attack...

Starting DDoS Attack... (Educational Purposes Only)

[*] Attack started. Press Ctrl+C to stop the attack.

Sent 100 packets: [#########################                     ] 50%
Sent 200 packets: [###########################################         ] 70%
Sent 300 packets: [#############################################     ] 90%
...
```

## Disclaimer

- **DDoS** is designed solely for **educational purposes** to understand how DDoS attacks work. It should not be used for any illegal activities.
- **Usage of this tool for unauthorized attacks is illegal**. Please ensure that you have permission from the network owner before using this tool.
- **The developers are not responsible for any damages** caused by using this tool. Always use it responsibly.

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

