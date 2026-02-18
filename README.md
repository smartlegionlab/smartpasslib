# smartpasslib (Smart Passwords Library) <sup>v2.2.0</sup>

---

**Smart Passwords Library**: Cryptographic password generation and management without storage. Generate passwords from secrets, verify knowledge without exposure, manage metadata securely.

---

[![PyPI - Downloads](https://img.shields.io/pypi/dm/smartpasslib?label=pypi%20downloads)](https://pypi.org/project/smartpasslib/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smartpasslib)](https://github.com/smartlegionlab/smartpasslib/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smartpasslib)
[![PyPI](https://img.shields.io/pypi/v/smartpasslib)](https://pypi.org/project/smartpasslib)
![Platform](https://img.shields.io/badge/🪟%20Windows%20%7C%20🐧%20Linux%20%7C%20🍎%20macOS-666?style=flat-square)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smartpasslib)](https://github.com/smartlegionlab/smartpasslib/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/smartpasslib)](https://pypi.org/project/smartpasslib)
[![GitHub stars](https://img.shields.io/github/stars/smartlegionlab/smartpasslib?style=social)](https://github.com/smartlegionlab/smartpasslib/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smartpasslib?style=social)](https://github.com/smartlegionlab/smartpasslib/network/members)

[![PyPI Downloads](https://static.pepy.tech/badge/smartpasslib)](https://pepy.tech/projects/smartpasslib)
[![PyPI Downloads](https://static.pepy.tech/badge/smartpasslib/month)](https://pepy.tech/projects/smartpasslib)
[![PyPI Downloads](https://static.pepy.tech/badge/smartpasslib/week)](https://pepy.tech/projects/smartpasslib)

---

## **🔐 Core Principles:**

- 🔐 **Zero-Storage Security**: No passwords or secret phrases are ever stored or transmitted
- 🔑 **Deterministic Generation**: Identical secret + parameters = identical password (SHA3-512 based)
- 📝 **Metadata Only**: Store only verification metadata (public keys, descriptions, lengths)
- 🔄 **On-Demand Regeneration**: Passwords are recalculated when needed, never retrieved from storage

**What You Can Do:**
1. **Smart Passwords**: Generate deterministic passwords from secret phrases
2. **Strong Random Passwords**: Cryptographically secure passwords with character diversity
3. **Authentication Codes**: Generate secure 2FA/MFA codes with guaranteed character sets
4. **Base Passwords**: Simple random passwords for general use
5. **Key Generation**: Create public/private verification keys from secrets
6. **Secret Verification**: Prove knowledge of secrets without revealing them (public key verification)
7. **Metadata Management**: Store and update password metadata (descriptions, lengths) without storing passwords
8. **Deterministic & Non-Deterministic**: Both reproducible and random password generation options

**Key Features:**
- ✅ **No Password Database**: Eliminates the need for password storage
- ✅ **No Secret Storage**: Secret phrases never leave your control
- ✅ **Public Key Verification**: Verify secrets without exposing them
- ✅ **Multiple Generator Types**: Smart, strong, base, and code generators
- ✅ **Metadata Updates**: Modify descriptions and lengths without affecting cryptographic integrity
- ✅ **Full Test Coverage**: 100% tested for reliability and security
- ✅ **Cross-Platform**: Works anywhere Python runs

**Security Model:**
- **Proof of Knowledge**: Verify you know a secret without storing or transmitting it
- **Deterministic Security**: Same input = same output, always reproducible
- **Metadata Separation**: Non-sensitive data (descriptions) stored separately from verification data (public keys)
- **No Recovery Backdoors**: Lost secret = permanently lost passwords (by design)

---

## ⚠️ Critical Notice

**BEFORE USING THIS SOFTWARE, READ THE COMPLETE LEGAL DISCLAIMER BELOW**

[View Legal Disclaimer & Liability Waiver](#-legal-disclaimer)

*Usage of this software constitutes acceptance of all terms and conditions.*

---

## 📚 Research Paradigms & Publications

- **[Pointer-Based Security Paradigm](https://doi.org/10.5281/zenodo.17204738)** - Architectural Shift from Data Protection to Data Non-Existence
- **[Local Data Regeneration Paradigm](https://doi.org/10.5281/zenodo.17264327)** - Ontological Shift from Data Transmission to Synchronous State Discovery

---

## 🔬 Technical Foundation

The library implements **deterministic password generation** - passwords are generated reproducibly from secret phrases using cryptographic hash functions.

**Key principle**: Instead of storing passwords, you store verification metadata. The actual password is regenerated on-demand from your secret.

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

## 🆕 What's New in v2.2.0

### Storage Improvements:
- **New config location**: `~/.config/smart_password_manager/passwords.json`
- **Automatic migration**: Legacy `~/.cases.json` files are auto-migrated on first use
- **Cross-platform paths**: Uses `Path.home()` for all OS support
- **Safe backup**: Original file preserved as `.cases.json.bak`
- **Backward compatibility**: Old files are automatically migrated, not deleted

### Breaking Changes:
- None! Full backward compatibility maintained

---

## 📦 Installation

```bash
pip install smartpasslib
```

---

## 📁 File Locations

Starting from v2.2.0, configuration files are stored in:

| Platform | Configuration Path |
|----------|-------------------|
| Linux | `~/.config/smart_password_manager/passwords.json` |
| macOS | `~/.config/smart_password_manager/passwords.json` |
| Windows | `C:\Users\Username\.config\smart_password_manager\passwords.json` |

**Legacy Migration**: 
- Old `~/.cases.json` files are automatically migrated on first use
- Original file is backed up as `~/.cases.json.bak`
- Migration is one-time and non-destructive

**Custom Path**:
```python
# Use default platform-specific path
manager = SmartPasswordManager()

# Or specify custom path
manager = SmartPasswordManager('/path/to/my/config.json')
```

---

## 🚀 Quick Start

```python
from smartpasslib import SmartPasswordMaster

# Your secret phrase is the only key needed
secret = "my secret phrase"

# Discover the password
password = SmartPasswordMaster.generate_smart_password(
    secret=secret, 
    length=16
)
print(f"Your discovered password: {password}")
# Example output: _4qkVFcC3#pGFvhH
```

## 🔑 Verification Without Storage

```python
from smartpasslib import SmartPasswordMaster

# Generate a public verification key (store this, not the password)
public_key = SmartPasswordMaster.generate_public_key(
    secret="my secret"
)

# Later, verify you know the secret without revealing it
is_valid = SmartPasswordMaster.check_public_key(
    secret="my secret",
    public_key=public_key
)  # Returns True - proof of secret knowledge
print(is_valid)  # True
```

---

## 🏗️ Core Components

### SmartPasswordMaster - Main Interface

```python
from smartpasslib import SmartPasswordMaster

# Generate different types of passwords
base_password = SmartPasswordMaster.generate_base_password(length=12)
# Output: wd@qt99QH84P

strong_password = SmartPasswordMaster.generate_strong_password(length=14)
# Output: _OYZ7h7wBLcg1Y

smart_password = SmartPasswordMaster.generate_smart_password("secret", 16)
# Output: wcJjBKIhsgV%!6Iq

# Generate and verify keys
public_key = SmartPasswordMaster.generate_public_key("secret")
is_valid = SmartPasswordMaster.check_public_key("secret", public_key)
print(f"Verification: {is_valid}")  # Verification: True

# Generate secure codes
auth_code = SmartPasswordMaster.generate_code(8)
# Output: r6*DFyM4
```

### SmartPasswordManager - Metadata Storage

```python
from smartpasslib import SmartPasswordManager, SmartPassword, SmartPasswordMaster

manager = SmartPasswordManager()  # Automatically uses ~/.config/smart_password_manager/passwords.json

# Store verification metadata (not the password and not secret phrase!)
public_key = SmartPasswordMaster.generate_public_key("github secret")
smart_pass = SmartPassword(
    public_key=public_key,
    description="GitHub account",
    length=18
)
manager.add_smart_password(smart_pass)

# Update metadata
manager.update_smart_password(
    public_key=public_key,
    description="GitHub Professional",
    length=20
)

# Retrieve and regenerate password when needed
stored_metadata = manager.get_smart_password(public_key)
regenerated_password = SmartPasswordMaster.generate_smart_password(
    "github secret",
    stored_metadata.length
)
# Output: ntm#uhqVDx3GqqQzELOH
```

### Generators

**Base Generator** - Simple random passwords:
```python
from smartpasslib.generators.base import BasePasswordGenerator
password = BasePasswordGenerator.generate(12)
# Output: oGHZRCv6zaZF
```

**Strong Generator** - Cryptographically secure with character diversity:
```python
from smartpasslib.generators.strong import StrongPasswordGenerator
password = StrongPasswordGenerator.generate(14)  # Guarantees one of each character type
# Output: 3g4nU_4k6!c%rs
```

**Code Generator** - Secure codes for authentication:
```python
from smartpasslib.generators.code import CodeGenerator
code = CodeGenerator.generate(6)  # Minimum 4 characters
# Output: Q%5ff*
```

**Smart Generator** - Deterministic passwords from seeds:
```python
from smartpasslib.generators.smart import SmartPasswordGenerator
from smartpasslib.generators.key import SmartKeyGenerator

seed = SmartKeyGenerator.generate_private_key("secret")
password = SmartPasswordGenerator.generate(seed, 15)
# Output: wcJjBKIhsgV%!6I
```

---

## 💡 Advanced Usage

### Password Management System

```python
from smartpasslib import SmartPasswordManager, SmartPassword, SmartPasswordMaster

class PasswordVault:
    def __init__(self):
        self.manager = SmartPasswordManager()
    
    def add_service(self, service_name: str, secret: str, length: int = 16):
        """Register a new service with its secret"""
        public_key = SmartPasswordMaster.generate_public_key(secret)
        metadata = SmartPassword(
            public_key=public_key,
            description=service_name,
            length=length
        )
        self.manager.add_smart_password(metadata)
        return public_key
    
    def get_password(self, public_key: str, secret: str) -> str:
        """Regenerate password when needed"""
        metadata = self.manager.get_smart_password(public_key)
        if metadata:
            return SmartPasswordMaster.generate_smart_password(
                secret, 
                metadata.length
            )
        return None

# Usage
vault = PasswordVault()
key = vault.add_service("My Account", "my account secret", 20)
password = vault.get_password(key, "my account secret")
# Output: _!DGHSTiE!DQxLojjlT%'
```

### Two-Factor Authentication Codes

```python
from smartpasslib.generators.code import CodeGenerator

def generate_2fa_code():
    """Generate a secure 2FA code"""
    return CodeGenerator.generate(8)

auth_code = generate_2fa_code()  # Example: "lA4P&P!k"
```

---

## 🔧 Ecosystem

### Command Line Tools
- **[CLI Smart Password Generator](https://github.com/smartlegionlab/clipassgen/)** - Generate passwords from terminal
- **[CLI Smart Password Manager](https://github.com/smartlegionlab/clipassman/)** - Manage password metadata

### Graphical Applications
- **[Web Smart Password Manager](https://github.com/smartlegionlab/smart-password-manager)** - Browser-based interface
- **[Desktop Smart Password Manager](https://github.com/smartlegionlab/smart-password-manager-desktop)** - Cross-platform desktop app

---

## 👨‍💻 For Developers

### Development Setup

```bash
# Install development dependencies
pip install -r data/requirements-dev.txt

# Run tests
pytest -v

# Run tests with coverage
pytest -v --cov=smartpasslib --cov-report=html

# Build package
python -m build
```

### Testing Coverage

**100% test coverage** - All components thoroughly tested:
- Password generators with edge cases
- Cryptographic key operations
- Metadata serialization/deserialization
- Error handling and validation
- File persistence operations

![Test Coverage](https://github.com/smartlegionlab/smartpasslib/raw/master/data/images/cov.png)

### API Stability

**Public API** (stable):
- `SmartPasswordMaster` - Main interface class
- `SmartPasswordManager` - Metadata management
- `SmartPassword` - Password metadata container
- `SmartPasswordFactory` - Factory for creating metadata

**Internal API** (subject to change):
- All modules in `smartpasslib.generators.*`
- `smartpasslib.factories.*`
- `smartpasslib.utils.*`

---

## 📜 License

**[BSD 3-Clause License](LICENSE)**

Copyright (©) 2026, Alexander Suvorov

```
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

---

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/smartlegionlab/smartpasslib/issues)
- **Documentation**: Inline code documentation
- **Tests**: 100% coverage ensures reliability

**Note**: Always test password generation in your specific environment. Implementation security depends on proper usage.

---

## ⚠️ Security Warnings

### Secret Phrase Security

**Your secret phrase is the cryptographic master key**

1. **Permanent data loss**: Lost secret phrase = irreversible loss of all derived passwords
2. **No recovery mechanisms**: No password recovery, no secret reset, no administrative override
3. **Deterministic generation**: Identical input (secret + parameters) = identical output (password)
4. **Single point of failure**: Secret phrase is the sole authentication factor for all passwords
5. **Secure storage required**: Digital storage of secret phrases is prohibited

**Critical**: Test password regeneration with non-essential accounts before production use

---

## 📄 Legal Disclaimer

**COMPLETE AND ABSOLUTE RELEASE FROM ALL LIABILITY**

**SOFTWARE PROVIDED "AS IS" WITHOUT ANY WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT.**

The copyright holder, contributors, and any associated parties **EXPLICITLY DISCLAIM AND DENY ALL RESPONSIBILITY AND LIABILITY** for:

1. **ANY AND ALL DATA LOSS**: Complete or partial loss of passwords, accounts, credentials, cryptographic keys, or any data whatsoever
2. **ANY AND ALL SECURITY INCIDENTS**: Unauthorized access, data breaches, account compromises, theft, or exposure of sensitive information
3. **ANY AND ALL FINANCIAL LOSSES**: Direct, indirect, incidental, special, consequential, or punitive damages of any kind
4. **ANY AND ALL OPERATIONAL DISRUPTIONS**: Service interruptions, account lockouts, authentication failures, or denial of service
5. **ANY AND ALL IMPLEMENTATION ISSUES**: Bugs, errors, vulnerabilities, misconfigurations, or incorrect usage
6. **ANY AND ALL LEGAL OR REGULATORY CONSEQUENCES**: Violations of laws, regulations, compliance requirements, or terms of service
7. **ANY AND ALL PERSONAL OR BUSINESS DAMAGES**: Reputational harm, business interruption, loss of revenue, or any other damages
8. **ANY AND ALL THIRD-PARTY CLAIMS**: Claims made by any other parties affected by software usage

**USER ACCEPTS FULL AND UNCONDITIONAL RESPONSIBILITY**

By installing, accessing, or using this software in any manner, you irrevocably agree that:

- You assume **ALL** risks associated with software usage
- You bear **SOLE** responsibility for secret phrase management and security
- You accept **COMPLETE** responsibility for all testing and validation
- You are **EXCLUSIVELY** liable for compliance with all applicable laws
- You accept **TOTAL** responsibility for any and all consequences
- You **PERMANENTLY AND IRREVOCABLY** waive, release, and discharge all claims against the copyright holder, contributors, distributors, and any associated entities

**NO WARRANTY OF ANY KIND**

This software comes with **ABSOLUTELY NO GUARANTEES** regarding:
- Security effectiveness or cryptographic strength
- Reliability or availability
- Fitness for any particular purpose
- Accuracy or correctness
- Freedom from defects or vulnerabilities

**NOT A SECURITY PRODUCT OR SERVICE**

This is experimental software. It is not:
- Security consultation or advice
- A certified cryptographic product
- A guaranteed security solution
- Professional security software
- Endorsed by any security authority

**FINAL AND BINDING AGREEMENT**

Usage of this software constitutes your **FULL AND UNCONDITIONAL ACCEPTANCE** of this disclaimer. If you do not accept **ALL** terms and conditions, **DO NOT USE THE SOFTWARE.**

**BY PROCEEDING, YOU ACKNOWLEDGE THAT YOU HAVE READ THIS DISCLAIMER IN ITS ENTIRETY, UNDERSTAND ITS TERMS COMPLETELY, AND ACCEPT THEM WITHOUT RESERVATION OR EXCEPTION.**

---

**Version**: 2.2.0 | [**Author**](https://smartlegionlab.ru): [Alexander Suvorov](https://alexander-suvorov.ru)