# SmartPassLib <sup>v3.0.2</sup>

---

**Smart Passwords Library**: Cryptographic password generation and management without storage. 
Generate passwords from secrets, verify knowledge without exposure, manage metadata securely.

**Now with Cross-Platform Determinism**: Same secret + same parameters = identical password on 
**C#, Python, Go, Kotlin, JavaScript** and any language with SHA-256.

**Decentralized by Design**: Unlike traditional password managers that store encrypted vaults on central servers, 
smartpasslib stores nothing. Your secrets never leave your device. Passwords are regenerated on-demand — 
**no cloud, no database, no trust required**.

---

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smartpasslib)](https://github.com/smartlegionlab/smartpasslib/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smartpasslib)
![Platform](https://img.shields.io/badge/🪟%20Windows%20%7C%20🐧%20Linux%20%7C%20🍎%20macOS-666?style=flat-square)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smartpasslib)](https://github.com/smartlegionlab/smartpasslib/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/smartlegionlab/smartpasslib?style=social)](https://github.com/smartlegionlab/smartpasslib/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smartpasslib?style=social)](https://github.com/smartlegionlab/smartpasslib/network/members)

[![PyPI - Downloads](https://img.shields.io/pypi/dm/smartpasslib?label=pypi%20downloads)](https://pypi.org/project/smartpasslib/)
[![PyPI](https://img.shields.io/pypi/v/smartpasslib)](https://pypi.org/project/smartpasslib)
[![PyPI - Format](https://img.shields.io/pypi/format/smartpasslib)](https://pypi.org/project/smartpasslib)
[![PyPI Downloads](https://static.pepy.tech/badge/smartpasslib)](https://pepy.tech/projects/smartpasslib)
[![PyPI Downloads](https://static.pepy.tech/badge/smartpasslib/month)](https://pepy.tech/projects/smartpasslib)
[![PyPI Downloads](https://static.pepy.tech/badge/smartpasslib/week)](https://pepy.tech/projects/smartpasslib)

---

## ⚠️ Disclaimer

**By using this software, you agree to the full disclaimer terms.**

**Summary:** Software provided "AS IS" without warranty. You assume all risks.

**Full legal disclaimer:** See [DISCLAIMER.md](https://github.com/smartlegionlab/smartpasslib/blob/master/DISCLAIMER.md)

---

## 🔄 Breaking Change (v3.0.2)

> **⚠️ This version is NOT backward compatible with v1.x.x and v2.x.x**

Passwords generated with older versions **cannot be regenerated** with v3.x.x.

📖 **Full migration instructions** → see [MIGRATION.md](https://github.com/smartlegionlab/smartpasslib/blob/master/MIGRATION.md)

---

## Core Principles:

- **Zero-Storage Security**: No passwords or secret phrases are ever stored or transmitted
- **Decentralized Architecture**: No central servers, no cloud dependency, no third-party trust required
- **Cross-Platform Deterministic Generation**: Identical secret + parameters = identical password **on any language** (SHA-256 based)
- **Metadata Only**: Store only verification metadata (public keys, descriptions, lengths)
- **On-Demand Regeneration**: Passwords are recalculated when needed, never retrieved from storage
- **Cryptographically Secure**: Uses `secrets` module and SHA-256

**What You Can Do:**
1. **Smart Passwords**: Generate deterministic passwords from secret phrases (cross-platform!)
2. **Strong Random Passwords**: Cryptographically secure passwords with character diversity
3. **Authentication Codes**: Generate secure 2FA/MFA codes with guaranteed character sets
4. **Base Passwords**: Simple cryptographically secure random passwords for general use
5. **Key Generation**: Create public/private verification keys from secrets
6. **Secret Verification**: Prove knowledge of secrets without revealing them (public key verification)
7. **Metadata Management**: Store and update password metadata (descriptions, lengths) without storing passwords
8. **Deterministic & Non-Deterministic**: Both reproducible and random password generation options

---

## Decentralized Password Management

Unlike traditional password managers that store your encrypted vault on central servers, smartpasslib is **decentralized by design**:

- **No central storage** — passwords are never stored anywhere
- **No server dependency** — generation happens on your device
- **No third-party trust** — your secret is yours alone
- **No cloud lock-in** — metadata can be synced via any channel (USB, Nextcloud, Signal, paper)

Your passwords exist only when you generate them. Your secrets never leave your device.

---

**Key Features:**
- **Decentralized & Serverless**: No central database, no cloud lock-in, complete user sovereignty
- **No Password Database**: Eliminates the need for password storage
- **No Secret Storage**: Secret phrases never leave your control
- **Cross-Platform Determinism**: Same results on C#, Python, Go, Kotlin, JavaScript
- **Public Key Verification**: Verify secrets without exposing them
- **Multiple Generator Types**: Smart, strong, base, and code generators
- **Store Only Public Metadata**: Descriptions and public keys can be stored; private keys and secrets are NEVER persisted
- **Full Test Coverage**: 100% tested for reliability and security

---

## Security Model:

- **Proof of Knowledge**: Verify you know a secret without storing or transmitting it
- **Decentralized Trust**: No third party needed — you control your secrets completely
- **Deterministic Security**: Same input = same output, always reproducible across platforms
- **No Vulnerable Metadata Storage**: Only public keys and descriptions can be stored (optional). Private keys and secret phrases are NEVER stored anywhere
- **Zero Storage of Secrets**: Secret phrases exist only in your memory, private keys are derived on-demand and never persisted
- **No Recovery Backdoors**: Lost secret = permanently lost passwords (by design)

---

## Research Paradigms & Publications

- **[Pointer-Based Security Paradigm](https://doi.org/10.5281/zenodo.17204738)** - Architectural Shift from Data Protection to Data Non-Existence
- **[Local Data Regeneration Paradigm](https://doi.org/10.5281/zenodo.17264327)** - Ontological Shift from Data Transmission to Synchronous State Discovery

---

## Technical Foundation

The library implements **cross-platform deterministic password generation** - passwords are generated reproducibly 
from secret phrases using **SHA-256** cryptographic hash function.

**Why SHA-256 instead of SHA3-512:**
- **Cross-platform standard** - Available in every programming language by default
- **NIST certified** - FIPS 180-4 compliant, used in Bitcoin, TLS, JWT
- **256-bit security** - Quantum-resistant (128-bit effective with Grover's algorithm)
- **Performance** - Faster on 32-bit and 64-bit systems
- **Sufficient for passwords** - 256 bits of entropy is impossible to brute force

**Key principle**: Instead of storing passwords, you store verification metadata. The actual password is regenerated on-demand from your secret.

**Cross-Platform Guarantee**:
- Same secret phrase + same length = **identical password** on any platform
- Implemented in C#, Python, Go, Kotlin, JavaScript
- Based on SHA-256 (NIST standard) — not language-specific

**Decentralized Architecture**:
- No central authority required
- Metadata can be synced via any channel (USB, cloud, even paper)
- Your security depends only on your secret phrase, not on any service provider
- Works offline — no internet connection required

**What's NOT stored**:
- Your secret phrase
- The actual password
- Any reversible password data

**What IS stored** (optional):
- Public verification key (hash of secret)
- Service description
- Password length parameter

**Security model**: Proof of secret knowledge without secret storage.

---

## Installation

```bash
pip install smartpasslib
```

---

## File Locations

Configuration files are stored in:

| Platform | Configuration Path                                                |
|----------|-------------------------------------------------------------------|
| Linux    | `~/.config/smart_password_manager/passwords.json`                 |
| macOS    | `~/.config/smart_password_manager/passwords.json`                 |
| Windows  | `C:\Users\Username\.config\smart_password_manager\passwords.json` |

**Legacy Migration**: 
- Old `~/.cases.json` files are automatically migrated on first use
- Original file is backed up as `~/.cases.json.bak`
- Migration is one-time and non-destructive

---

## Quick Start

```python
from smartpasslib import SmartPasswordMaster

# Your secret phrase is the only key needed
secret = "my_secret_key"

# Discover the password (CROSS-PLATFORM!)
password = SmartPasswordMaster.generate_smart_password(
    secret=secret, 
    length=12
)
print(f"Your discovered password: {password}")
# Your discovered password: i&h!lLy&ONxC
```

## Verification Without Storage

```python
from smartpasslib import SmartPasswordMaster

# Generate a public verification key (store this, not the password)
public_key = SmartPasswordMaster.generate_public_key(
    secret="my_secret_key"
)

# Later, verify you know the secret without revealing it
is_valid = SmartPasswordMaster.check_public_key(
    secret="my_secret_key",
    public_key=public_key
)
print(is_valid)  # True
```

---

## Core Components

### SmartPasswordMaster - Main Interface

```python
from smartpasslib import SmartPasswordMaster

# Generate different types of passwords
base_password = SmartPasswordMaster.generate_base_password(length=12)
# Output example: MG-QwPHu6a*y

strong_password = SmartPasswordMaster.generate_strong_password(length=14)
# Output example: 7u-IOW7$#K*FHd

smart_password = SmartPasswordMaster.generate_smart_password("my_secret_key", 12)
# Output: i&h!lLy&ONxC

# Generate and verify keys
public_key = SmartPasswordMaster.generate_public_key("my_secret_key")
is_valid = SmartPasswordMaster.check_public_key("my_secret_key", public_key)
print(f"Verification: {is_valid}")  # Verification: True

# Generate secure codes
auth_code = SmartPasswordMaster.generate_code(8)
# Output example: oLi&D@3s
```

### SmartPasswordManager - Metadata Storage

```python
from smartpasslib import SmartPasswordManager, SmartPassword, SmartPasswordMaster

manager = SmartPasswordManager()

# Store verification metadata (not the password and not secret phrase!)
public_key = SmartPasswordMaster.generate_public_key("MyStrongSecretPhrase2026!")
smart_pass = SmartPassword(
    public_key=public_key,
    description="GitHub account",
    length=18
)
manager.add_smart_password(smart_pass)

# Retrieve and regenerate password when needed
stored_metadata = manager.get_smart_password(public_key)
regenerated_password = SmartPasswordMaster.generate_smart_password(
    "MyStrongSecretPhrase2026!",
    stored_metadata.length
)
print(regenerated_password) # im5daDg77!drK7-lan
```

### Generators

**Base Generator** - Cryptographically secure random passwords:
```python
from smartpasslib.generators.base import BasePasswordGenerator
password = BasePasswordGenerator.generate(12)
# Output example: Q#1&tesRzeza
```

**Strong Generator** - Cryptographically secure with character diversity:
```python
from smartpasslib.generators.strong import StrongPasswordGenerator
password = StrongPasswordGenerator.generate(14)
# Output example: Ft7n!vJu6&9@V4
```

**Code Generator** - Secure codes for authentication:
```python
from smartpasslib.generators.code import CodeGenerator
code = CodeGenerator.generate(6)
# Output example: M$yVc9
```

**Smart Generator** - Deterministic passwords from seeds (CROSS-PLATFORM):
```python
from smartpasslib.generators.smart import SmartPasswordGenerator

password = SmartPasswordGenerator.generate("my_secret_key", 12)
# Output: i&h!lLy&ONxC (SAME on Go, Kotlin, JS!)
```

---

## Advanced Usage

### Password Management System

```python
from smartpasslib import SmartPasswordManager, SmartPassword, SmartPasswordMaster

class PasswordVault:
    def __init__(self):
        self.manager = SmartPasswordManager()
    
    def add_service(self, service_name: str, secret: str, length: int = 16):
        public_key = SmartPasswordMaster.generate_public_key(secret)
        metadata = SmartPassword(
            public_key=public_key,
            description=service_name,
            length=length
        )
        self.manager.add_smart_password(metadata)
        return public_key
    
    def get_password(self, public_key: str, secret: str) -> str:
        metadata = self.manager.get_smart_password(public_key)
        if metadata:
            return SmartPasswordMaster.generate_smart_password(secret, metadata.length)
        return None

# Usage
vault = PasswordVault()
key = vault.add_service("My Account", "my_account_secret", 20)
password = vault.get_password(key, "my_account_secret")
```

---

## Security Warnings

### Decentralized Nature

**There is no "forgot password" button.** This is by design:

- No central server can reset your passwords
- No support team can recover your access
- Your secret phrase is the ONLY key

**This is the price of true decentralization** — you are completely in control.

### Security Requirements

#### Secret Phrase
- **Minimum 12 characters** (enforced)
- Case-sensitive
- Use mix of: uppercase, lowercase, numbers, symbols, emoji, or Cyrillic
- Never store digitally
- **NEVER use your password description as secret phrase**

#### Strong Secret Examples
```
✅ "MyCatHippo2026"          — mixed case + numbers
✅ "P@ssw0rd!LongSecret"     — special chars + numbers + length
✅ "КотБегемот2026НаДиете"   — Cyrillic + numbers
✅ "GitHubPersonal2026!"     — description + extra chars (but not the description alone)
```

#### Weak Secret Examples (avoid)
```
❌ "GitHub Account"          — using description as secret (weak!)
❌ "password"                — dictionary word, too short
❌ "1234567890"              — only digits, too short
❌ "qwerty123"               — keyboard pattern
❌ Same as description       — never use the same value as password description
```

### Secret Phrase Security

**Your secret phrase is the cryptographic master key**

1. **Permanent data loss**: Lost secret phrase = irreversible loss of all derived passwords
2. **No recovery mechanisms**: No password recovery, no secret reset, no administrative override
3. **Deterministic generation**: Identical input = identical output **on any platform**
4. **Single point of failure**: Secret phrase is the sole authentication factor
5. **Secure storage required**: Digital storage of secret phrases is prohibited

**Critical**: Test password regeneration with non-essential accounts before production use
**Note**: Always test password generation in your specific environment. Implementation security depends on proper usage.
**NEVER use your password description as secret phrase**

---

## Cross-Platform Implementations

The same deterministic algorithm is available in multiple languages.
smartpasslib Python produces **identical passwords** to:

| Language   | Repository                                                                   |
|------------|:-----------------------------------------------------------------------------|
| JavaScript | [smartpasslib-js](https://github.com/smartlegionlab/smartpasslib-js)         |
| Kotlin     | [smartpasslib-kotlin](https://github.com/smartlegionlab/smartpasslib-kotlin) |
| Go         | [smartpasslib-go](https://github.com/smartlegionlab/smartpasslib-go)         |
| C#         | [smartpasslib-csharp](https://github.com/smartlegionlab/smartpasslib-csharp) |

---

## Ecosystem

**Core Libraries:**
- **[smartpasslib](https://github.com/smartlegionlab/smartpasslib)** - Python (this)
- **[smartpasslib-js](https://github.com/smartlegionlab/smartpasslib-js)** - JavaScript
- **[smartpasslib-kotlin](https://github.com/smartlegionlab/smartpasslib-kotlin)** - Kotlin
- **[smartpasslib-go](https://github.com/smartlegionlab/smartpasslib-go)** - Go
- **[smartpasslib-csharp](https://github.com/smartlegionlab/smartpasslib-csharp)** - C#

**CLI Applications:**
- **[CLI Smart Password Manager (Python)](https://github.com/smartlegionlab/clipassman)**
- **[CLI Smart Password Generator (Python)](https://github.com/smartlegionlab/clipassgen)**
- **[CLI Smart Password Manager (C#)](https://github.com/smartlegionlab/SmartPasswordManagerCsharpCli)**
- **[CLI Smart Password Generator (C#)](https://github.com/smartlegionlab/SmartPasswordGeneratorCsharpCli)** 

**Desktop Applications:**
- **[Desktop Smart Password Manager (Python)](https://github.com/smartlegionlab/smart-password-manager-desktop)**
- **[Desktop Smart Password Manager (C#)](https://github.com/smartlegionlab/SmartPasswordManagerCsharpDesktop)**

**Other:**
- **[Smart Password Web Manager](https://github.com/smartlegionlab/smart-password-manager-web)**
- **[Smart Password Android Manager](https://github.com/smartlegionlab/smart-password-manager-android)**

---

## License

**[BSD 3-Clause License](https://github.com/smartlegionlab/smartpasslib/blob/master/LICENSE)**

Copyright (©) 2026, [Alexander Suvorov](https://github.com/smartlegionlab)

---

## Support

- **Issues**: [GitHub Issues](https://github.com/smartlegionlab/smartpasslib/issues)
- **Documentation**: Inline code [documentation](https://github.com/smartlegionlab/smartpasslib/blob/master/README.md)
- **Tests**: 100% coverage ensures reliability

---

## For Developers

### Development Setup

```bash
pip install -r data/requirements-dev.txt
pytest -v --cov=smartpasslib --cov-report=html
python -m build
```

### Testing Coverage

**100% test coverage** - All components thoroughly tested

![Test Coverage](https://github.com/smartlegionlab/smartpasslib/raw/master/data/images/cov.png)

### API Stability

**Public API** (stable):
- `SmartPasswordMaster` - Main interface class
- `SmartPasswordManager` - Metadata management
- `SmartPassword` - Password metadata container
- `SmartPasswordFactory` - Factory for creating metadata

**Internal API** (subject to change):
- `smartpasslib.generators.*`
- `smartpasslib.factories.*`
- `smartpasslib.utils.*`

---


