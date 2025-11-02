# NumberLookup

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Issues](https://img.shields.io/github/issues/Abhinavsahu1/NumberLookup)](https://github.com/Abhinavsahu1/NumberLookup/issues)
[![Forks](https://img.shields.io/github/forks/Abhinavsahu1/NumberLookup)](https://github.com/Abhinavsahu1/NumberLookup/network)
[![Stars](https://img.shields.io/github/stars/Abhinavsahu1/NumberLookup)](https://github.com/Abhinavsahu1/NumberLookup/stargazers)

> A simple, powerful OSINT tool to gather publicly available information from any phone number.

**<img width="1039" height="326" alt="Screenshot 2025-11-02 113605" src="https://github.com/user-attachments/assets/e1f7140b-5e63-4dc5-9a91-d9451a24fdfb" />
**

---

> [!WARNING]
> **Ethical Use Disclaimer**
>
> This tool is intended for **educational purposes and ethical use only**. It is designed to help security professionals understand what public information is associated with a phone number.
>
> **DO NOT** use this tool for stalking, harassment, or any illegal or malicious activities. The developers are not responsible for any misuse.

---

## ✨ Features

* **🌍 Country & Location:** Identifies the country and region.
* **📡 Carrier Information:** Detects the mobile carrier (e.g., Jio, Airtel).
* **📞 Line Type:** Determines if it's a `mobile`, `landline`, or `VoIP` number.
* **🕒 Timezone:** Finds the timezone associated with the number.

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* pip

### Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/Abhinavsahu1/NumberLookup.git](https://github.com/Abhinavsahu1/NumberLookup.git)
    ```
2.  Navigate to the directory:
    ```bash
    cd NumberLookup
    ```
3.  Install the required packages:
    ```bash
    pip install -r requirements.txt 
    ```
    *(**Note:** Iske liye aapko `requirements.txt` file upload karni hogi!)*

## 💻 How to Use

Run the tool from your terminal. Remember to include the country code.

```bash
python main.py -n "enter your no."
