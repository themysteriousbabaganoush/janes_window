# Jane's Window

sha256 sum's

e62f9beb76f24bc76c4a4eb8ee42c0065c9ef7a52465a2fc34d68915b7363250  janes_window
d08126a4805368b8acd41c8e72ec9055f6c6aed4fdda6cac29a24734a3049b81  janes_window.py

**A Friendly Wrapper for John the Ripper**  
_By Chairman Hellsing & Mun_  

---

### 💡 Concept & Origin

**Jane's Window** is a clever play on the legendary password cracker **John the Ripper**. Where *John* is the engine, *Jane* is the interface—the window through which you control the cracking.

Designed for clarity and speed, Jane’s Window wraps `john` in an intuitive, guided shell that simplifies hash input, wordlist selection, and result handling—without sacrificing power.

---

### ⚙️ Features

- 🧠 **NTLM hash cracking** (Windows hashes)
- 📎 Accepts hashes via **direct input** or **file upload**
- 📚 Interactive **wordlist selector** (with Linux default detection)
- 📂 Automatic log folder and log naming using timestamps
- 📄 Saves cracked credentials into a readable `.log` file
- 🎭 ASCII startup art for flavor

---

### 🚀 How to Use

#### 1. **Run the Program**
```bash
python janes_window.py
```

#### 2. **Choose Input Mode**
You’ll be prompted to:
- Paste comma-separated NT hashes  
- OR load them from a file  

#### 3. **Pick a Wordlist**
- Jane will auto-detect `/usr/share/wordlists` on Linux
- Or you can provide a custom wordlist path

#### 4. **Cracking Begins**
John the Ripper will launch behind the scenes:
- Format is hardcoded to `NT`
- Status updates every 10 seconds
- Cracked credentials shown at the end

#### 5. **Review Your Results**
- Cracked hashes are saved in the `logs/` folder
- Filenames follow this pattern:
  ```
  logs/janes_2cents_<timestamp>.log
  ```

---

### 🧪 Sample Run

```text
=== Janes Window — NT Hash Decipher Engine ===

[1] Paste comma-separated NT hashes
[2] Load NT hashes from file
Select input mode [1/2]: 1

Paste NT hashes (comma-separated): 31d6cfe0d16ae931b73c59d7e0c089c0
Available wordlists:
[1] /usr/share/wordlists/rockyou.txt
[2] Enter custom path
Select wordlist: 1

[+] Launching John the Ripper...
[*] Cracking in progress... waiting 10 seconds
[+] John has finished cracking.

[✓] Cracked hashes saved to: logs/janes_2cents_0706253005.log
```

---

### 🏗 Building as Executable

To turn Jane’s Window into a standalone `.exe`:

```bash
pip install pyinstaller
pyinstaller --onefile janes_window.py
```

This will generate `janes_window.exe` in the `dist/` folder.

---

### 🔐 Requirements

- Python 3.6+
- John the Ripper (`john`) installed and in PATH
- Wordlist(s) available on disk
- NT hashes to crack

---

### 📜 License & Credits

Created by **Chairman Hellsing & Mun** as part of the cyber toolkit for pentesters, hobbyists, and defenders alike.

> "Behind every strong John is a stronger Jane opening his window."

---
