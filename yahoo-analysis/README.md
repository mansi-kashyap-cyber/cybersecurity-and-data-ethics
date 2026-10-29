# Technical Post-Mortem: Cryptographic Collapse at Yahoo

This case study analyzes the technical specifics behind the compromise of over 3 billion user accounts, focusing heavily on cryptographic debt and legacy system degradation.

## 🛠️ The Cryptographic Flaw: MD5 & The Absence of Salting

At the time of the breaches, Yahoo's user credential database utilized the **MD5 (Message-Digest Algorithm 5)** hashing function to protect user passwords. MD5 converts an arbitrary length string into a fixed 128-bit hash value. By the mid-2000s, MD5 was mathematically proven to be insecure against collision attacks, but Yahoo’s architectural failure was two-fold:

### 1. The Vulnerability to Pre-Computed Tables (Rainbow Tables)
Because MD5 is extremely fast to compute ($O(1)$ lookup complexity for an attacker once compiled), threat actors used **Rainbow Tables**—massive pre-computed databases of strings and their corresponding MD5 hashes. When hackers exfiltrated the database, they did not need to guess passwords; they simply mapped the stolen hashes against their tables to instantly reverse them into plain text.

### 2. The Absence of Cryptographic Salting
Yahoo failed to implement unique **salting**. A salt is a random string concatenated to a user's password *before* it is hashed (e.g., `Hash(Password + Salt)`). 
*   **Without Salts:** If User A and User B both used the password `password123`, their database records would display the exact same MD5 string: `482c811da5d5b4bc6d497ffa98491e38`.
*   **The Result:** Attackers could identify patterns across millions of users instantly. They could crack one hash and instantly compromise every single account utilizing that exact password string.

