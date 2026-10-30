# cybersecurity-and-data-ethics
Technical analysis and open-source tools exploring structural data breaches and algorithmic privacy flaws.
# Cybersecurity & Data Ethics Research Hub

Welcome to my research and development hub. As a student exploring the intersection of artificial intelligence, system architecture, and cybersecurity, I build tracking tools and analyze historic network failures to understand how technical designs impact human privacy.

Rather than treating data breaches as abstract mishaps, this repository breaks down the exact algorithmic and architectural vulnerabilities that enabled them.

##  Repository Structure

*   ` case-studies/yahoo-breach/`: A deep dive into the cryptographic failures and legacy system neglect behind the compromise of 3 billion accounts.
*   ` case-studies/cambridge-analytica/`: A data-flow analysis of Facebook's Graph API v1.0, paired with a simulation script demonstrating nested relational data leaks.
*   Active Technical Projects-
*   **[The Ethical Data Sentinel](./ethical-data-sentinel/)**: A secure, command-line interface (CLI) application built in Python. It implements a secure **k-Anonymity** model to audit real-world password exposures via the Have I Been Pwned API and calculates an interactive Human Vulnerability Score.
---

## 🔍 Hub Overview

### 1. The Yahoo Data Breaches (Cryptographic & Infrastructure Failure)
*   **The Flaw:** Prolonged reliance on the structurally broken **MD5 hashing algorithm** without modern salting protocols, exposing user credentials to lightning-fast dictionary and rainbow table lookups.
*   **The Paradigm Shift:** Security is a continuous deployment lifecycle, not a static implementation. Leaving legacy architecture unpatched is functionally identical to leaving it unsecured.
*   **Detailed Post-Mortem:** Read the full analysis in the [Yahoo Data Breach Case Study](./yahoo-analysis/)
 directory.

### 2. The Cambridge Analytica Scandal (API Design & Nested Relational Vulnerabilities)
*   **The Flaw:** Facebook's **Graph API v1.0** data models treated authorization tokens as blanket passes to pull object graphs of un-consenting, secondary nodes (friends), turning user connections into data exploits.
*   **The Paradigm Shift:** System architectures must assume human data is intrinsically interconnected. Data governance models must enforce zero-trust boundary isolation at the node level, rather than relying on single-user consent.
*   **Detailed Breakdown & Script:** Explore the data-flow diagrams and code in the [Cambridge Analytica Case Study](./yahoo-analysis/cambridge-analytica/)

---
## ⚙️ Technical Skills Demonstrated Here
*   **Languages & Frameworks:** Python, Markdown
*   **Security Concepts:** Cryptographic Hashing (MD5 vs. bcrypt/SHA-1), Salt implementation, Rainbow Table mitigation, API Access Tokens, Node-level Authorization.
*   **Methodologies:** Threat Modeling, Behavioral Privacy Auditing, k-Anonymity API Querying.
## 🚀 Research Objectives
*   **Deconstruct** systemic security vulnerabilities down to the source code and network architectural levels.
*   **Bridge the gap** between strict software engineering choices and their downstream societal, political, and ethical consequences.
*   **Advocate for Privacy-by-Design (PbD)** principles in modern full-stack development.
