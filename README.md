

# 🦘 KANGAROO ATTACK 🧠🔨  
> **Elliptic Curve Discrete Logarithm Problem (ECDLP) Solver**  
> Like a kangaroo, but with math, speed, and *emotional damage*.

---

## 💡 What is this?

Welcome to **KANGAROO**, the only crypto-animal you’ll ever need. This isn’t just a Python script—it’s a full-on *mathematical kangaroo simulator* for solving the ECDLP. Why is it a kangaroo? Because kangaroos **hop**. This one hops through elliptic curve land trying to guess your secrets.

You give it a compressed SECP256k1 public key, and it returns your private key.  
Simple. Dangerous. Ridiculous.

---

## ⚠️ WARNING

> 💣 **This code is strictly for educational and research purposes only.**  
> Do not use it on anything you do not own.  
> If you try it on the wrong thing, the crypto gods will find you and SHA256 your soul.

---

## 🧪 Features

- 🚀 **Parallel brute force with multiprocessing**  
- 🔥 **Random seed generation** for kangaroo variety  
- 🐑 **Tame and wild herds** of hopping point trackers  
- 🧮 Full-blown ECC arithmetic with `gmpy2` (because math is hard)  
- 📝 Automatically logs keys like it’s 1999  
- 🕵️ Finds private keys (sometimes) with more drama than a Netflix docuseries  

---

## 📦 Requirements

- 🐍 Python 3.8+
- 🧮 `gmpy2`
- 🧠 Brain cells (optional, but helpful)

```bash
pip install gmpy2
```

---

## ⚙️ Usage

```bash
python kangaroo.py
```

Then sit back and watch it bounce like an over-caffeinated marsupial.

---

## 🧠 How it Works (sort of)

- Generates **herds** of elliptic curve points.
- Makes them **hop** around like lost tourists.
- Waits for two of them to crash into each other.
- Derives a private key from the wreckage.
- Profit??? No.

---

## 🎯 Target

Cracking private keys of SECP256k1 compressed public keys in up to 40-bit space.  
More than that? Bring snacks. And a few millennia.

---

## 📸 Sample Output

```
[+] KANGAROO: Wed May  6 23:38:45 2025
[+] [Tame and Wild herds are prepared]
[+] [P-table prepared]
[+] [Puzzle: 40]
[+] [Lower range limit: 549755813888]
[+] [Upper range limit: 1099511627775]
[+] [Expected Hops: 2^20.64 (1631201)]
[+] [Using 12 CPU cores for parallel search]
[+] [Core]: 05, [Random seed]: b'\xcd\xdf\xa5\x82q\x93\xbb\xce'
[+] [Core]: 04, [Random seed]: b'\xba\x98FCH\xd4\xee\x00'
[+] [Core]: 06, [Random seed]: b"\x11\x11\x8e\xf1'\x8c*\xa4"
[+] [Core]: 07, [Random seed]: b'\xde\x9bo\xad\xd0%\xbc\x9b'
[+] [Core]: 08, [Random seed]: b'\x8c\xa1\xdekq>Y\xfa'
[+] [Core]: 09, [Random seed]: b'\x8a\x00@\xc7\xb3\xa2\x00\x82'
[+] [Core]: 10, [Random seed]: b'J\x87.S\x8c\xc1]\xfa'
[+] [Core]: 11, [Random seed]: b'\xdf\xe7\xe6\xe6@\x11\x0e\n'
[+] [Core]: 12, [Random seed]: b'\xf1\x88\xf2\xe2\x86n\xf6\xbd'
[+] [Core]: 01, [Random seed]: b'\x13O3\x8a\xa1m\x04r'
[+] [Core]: 03, [Random seed]: b'\xe6\xd8?\x06\xa73Y\x82'
[+] [Core]: 02, [Random seed]: b'\x90IT\xf9\xe9\xb1\xa3\xeb'
[+] [Hops: 2^22.75 <-> 2408083 h/s] [00:00:03]
[+] total time: 3.97 sec
[+] PUZZLE SOLVED: Wed May  6 23:38:49 2025, Core: 01 
[+] Random seed used: b'\x13O3\x8a\xa1m\x04r' 
[+] Private key (dec) : 1003651412950 
[+] Hops: 9363708
[+] Average time to solve: 3.98 sec

[+] Solution found by Core: 01
[+] Random seed used: b'\x13O3\x8a\xa1m\x04r'

```

---

## 🧛‍♂️ Why the name?

Because **Pollard's Kangaroo algorithm** is real, and because who doesn’t love a script where kangaroos break crypto?

---

## 🤖 Contributing

Pull requests are welcome, especially if they add more marsupials.

---

## 🪦 Disclaimer

We are not responsible for any:

- Burned CPUs
- Existential dread
- Calls from three-letter agencies
- Math-induced rage

Use at your own risk. Or don’t. We’re not your parents.

---

## 🐸 Bonus Meme

> “I fear no man. But that thing…  
> That thing that hops elliptic curves...  
> It scares me.”

---

## ⭐ Star this repo

If this project made you chuckle, cry, or question your career path—give it a ⭐.  
Kangaroos love attention.

---

## 📬 Contact

Want to collaborate or challenge the kangaroo? 
Or throw a Vegemite sandwich.
BTC: bc1qdwnxr7s08xwelpjy3cc52rrxg63xsmagv50fa8
