# smartpasslib (Smart Passwords Library) <sup>v2.0.0</sup>

---

Cross-platform library for generating deterministic smart passwords.

> Your passwords don't need to be stored because they were never created—they already exist as mathematically defined values, waiting to be discovered using your secret phrase.

## 📚 Research Paradigms & Publications

- **[Pointer-Based Security Paradigm](https://doi.org/10.5281/zenodo.17204738)** - Architectural Transition from Data Protection to No Vulnerable Data
- **[Local Data Regeneration Paradigm](https://doi.org/10.5281/zenodo.17264327)** - Ontological Shift from Data Transmission to Synchronous State Discovery

---

[![PyPI - Downloads](https://img.shields.io/pypi/dm/smartpasslib?label=pypi%20downloads)](https://pypi.org/project/smartpasslib/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smartpasslib)](https://github.com/smartlegionlab/smartpasslib/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smartpasslib)
[![PyPI](https://img.shields.io/pypi/v/smartpasslib)](https://pypi.org/project/smartpasslib)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smartpasslib)](https://github.com/smartlegionlab/smartpasslib/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/smartpasslib)](https://pypi.org/project/smartpasslib)

[![PyPI Downloads](https://static.pepy.tech/badge/smartpasslib)](https://pepy.tech/projects/smartpasslib)
[![PyPI Downloads](https://static.pepy.tech/badge/smartpasslib/month)](https://pepy.tech/projects/smartpasslib)
[![PyPI Downloads](https://static.pepy.tech/badge/smartpasslib/week)](https://pepy.tech/projects/smartpasslib)

---

## 📚 Technical Foundation

The library implements **deterministic password generation** - passwords are generated reproducibly from secret phrases using cryptographic functions. 

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

## 🔄 What's New in v2.0.0

⚠️ CRITICAL WARNING!: Upgrading to v2.0.0 will break all existing password generation. All passwords generated with v1.x will become invalid, and public keys will no longer verify. This is not a compatible upgrade - it completely changes the cryptographic foundation.

### Major Changes:

**API Simplification:**
- Removed `login` parameter from all methods - now uses only `secret` phrase
- Simplified `SmartKeyGenerator` to work with single `secret` parameter
- Removed `SmartPasswordMaster.generate_default_smart_password()` method

**Data Model Updates:**
- `SmartPassword` class updated: `login` → `description`, `key` → `public_key`
- All deprecated methods removed (not just marked as deprecated)
- Removed deprecated `file_path` property from `SmartPasswordManager`

**Security Improvements:**
- Simplified key derivation algorithm in `SmartKeyGenerator`
- Cleaner seed management in `SmartPasswordGenerator`
- Removed complex hash mixing from v1.x

**Testing & Quality:**
- 100% test coverage achieved
- Comprehensive exception testing added
- Improved test fixtures and data management

### Breaking Changes:

**Method Signature Changes:**
```python
# v1.x → v2.0
SmartPasswordMaster.generate_smart_password(login, secret, length)
SmartPasswordMaster.generate_smart_password(secret, length)

SmartPasswordMaster.generate_public_key(login, secret)
SmartPasswordMaster.generate_public_key(secret)

SmartPasswordMaster.check_public_key(login, secret, public_key)
SmartPasswordMaster.check_public_key(secret, public_key)
```

**Class Structure Changes:**
```python
# v1.x → v2.0
SmartPassword(login, key, length)
SmartPassword(public_key, description, length)

SmartKeyGenerator._create_key(login, secret, steps)
SmartKeyGenerator._create_key(secret, steps)
```

**Removed Methods:**
- `SmartPasswordManager.add()` → use `add_smart_password()`
- `SmartPasswordManager.get_password()` → use `get_smart_password()`
- `SmartPasswordManager.remove()` → use `delete_smart_password()`
- `SmartPasswordManager.load_file()` → internal `_load_data()`
- `SmartPasswordManager.save_file()` → internal `_write_data()`
- `SmartPasswordManager.file_path` → use `filename`
- `SmartPasswordMaster.generate_default_smart_password()`

### Migration Guide:

**Password Generation:**
```python
# v1.x
password = SmartPasswordMaster.generate_smart_password(
    login="service", 
    secret="mysecret", 
    length=12
)

# v2.0
password = SmartPasswordMaster.generate_smart_password(
    secret="mysecret", 
    length=12
)
```

**SmartPassword Creation:**
```python
# v1.x
sp = SmartPassword(
    login="GitHub", 
    key=public_key, 
    length=16
)

# v2.0
sp = SmartPassword(
    public_key=public_key,
    description="GitHub", 
    length=16
)
```

**Manager Operations:**
```python
# v1.x (deprecated methods)
manager.add(password)
manager.get_password("login")

# v2.0
manager.add_smart_password(sp)
manager.get_smart_password(public_key)
```

### Key Improvements:

1. **Simplified API** - Single `secret` parameter instead of `login` + `secret`
2. **Cleaner Code** - Removed all deprecated methods and legacy code
3. **Better Security** - Streamlined cryptographic operations
4. **Full Test Coverage** - 100% test coverage ensures reliability
5. **Clearer Naming** - `public_key` accurately represents verification key

**Note:** v2.0.0 is not backward compatible with v1.x. Update your code according to the migration guide.

---

## 📦 Installation

```bash
pip install smartpasslib
```

## 🧙‍♂️ Quick Start: Discover Your First Password

```python
from smartpasslib import SmartPasswordMaster

# Your secret phrase is the only key needed
secret = "my secret phrase"

# Discover the password that was always there
password = SmartPasswordMaster.generate_smart_password(
    secret=secret, 
    length=16
)
print(f"Your discovered password: {password}")
# Your discovered password: _4qkVFcC3#pGFvhH
```

## 🔑 The Magic: Verification Without Storage

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

manager = SmartPasswordManager()

# Store verification metadata (not the password and not secret phrase!)
public_key = SmartPasswordMaster.generate_public_key("github secret")
smart_pass = SmartPassword(
    public_key=public_key,
    description="GitHub account",
    length=18
)
manager.add_smart_password(smart_pass)

# Retrieve and regenerate password when needed
stored_metadata = manager.get_smart_password(public_key)
regenerated_password = SmartPasswordMaster.generate_smart_password(
    "github secret",
    stored_metadata.length
)
# Output: ntm#uhqVDx3GqqQzEL'
```

### Password Generators

**Base Generator** - Simple random passwords:
```python
from smartpasslib.generators.base import BasePasswordGenerator
password = BasePasswordGenerator.generate(12) # oGHZRCv6zaZF
```

**Strong Generator** - Cryptographically secure with character diversity:
```python
from smartpasslib.generators.strong import StrongPasswordGenerator
password = StrongPasswordGenerator.generate(14)  # Guarantees one of each character type 3g4nU_4k6!c%rs
```

**Code Generator** - Secure codes for authentication:
```python
from smartpasslib.generators.code import CodeGenerator
code = CodeGenerator.generate(6)  # Minimum 4 characters Q%5ff*
```

**Smart Generator** - Deterministic passwords from seeds:
```python
from smartpasslib.generators.smart import SmartPasswordGenerator
from smartpasslib.generators.key import SmartKeyGenerator

seed = SmartKeyGenerator.generate_private_key("secret")
password = SmartPasswordGenerator.generate(seed, 15) # wcJjBKIhsgV%!6I
```

## 🚀 Advanced Usage

### Complete Example: Password Management System

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
password = vault.get_password(key, "my account secret") # _!DGHSTiE!DQxLojjlT%'
```

### Two-Factor Authentication Codes

```python
from smartpasslib.generators.code import CodeGenerator

def generate_2fa_code():
    """Generate a secure 2FA code"""
    return CodeGenerator.generate(8)

auth_code = generate_2fa_code()  # Example: "lA4P&P!k"
```

## 🔧 Ecosystem

Built on smartpasslib applications:

### Command Line Tools
- **[CLI Smart Password Generator](https://github.com/smartlegionlab/clipassgen/)** - Generate passwords from terminal
- **[CLI Smart Password Manager](https://github.com/smartlegionlab/clipassman/)** - Manage password metadata

### Graphical Applications
- **[Web Smart Password Manager](https://github.com/smartlegionlab/smart-password-manager)** - Browser-based interface
- **[Desktop Smart Password Manager](https://github.com/smartlegionlab/smart-password-manager-desktop)** - Cross-platform desktop app

## 💻 For Developers

### Development Setup

```bash
# Install development dependencies
pip install pytest pytest-cov

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

```
Coverage report: 100%
coverage.py v7.12.0
```

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

## 📜 License & Disclaimer

**BSD 3-Clause License**

Copyright (c) 2025, Alexander Suvorov

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

## 🆘 Support & Contribution

- **Issues**: [GitHub Issues](https://github.com/smartlegionlab/smartpasslib/issues)
- **Documentation**: Inline code documentation
- **Tests**: 100% coverage ensures reliability

**Note**: Always test password generation in your specific environment. Implementation security depends on proper usage.
