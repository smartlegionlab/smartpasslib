# Smart Passwords Library (smartpasslib) <sup>v1.1.2</sup>

[![PyPI - Downloads](https://img.shields.io/pypi/dm/smartpasslib?label=pypi%20downloads)](https://pypi.org/project/smartpasslib/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smartpasslib)](https://github.com/smartlegionlab/smartpasslib/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smartpasslib)
[![PyPI](https://img.shields.io/pypi/v/smartpasslib)](https://pypi.org/project/smartpasslib)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smartpasslib)](https://github.com/smartlegionlab/smartpasslib/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/smartpasslib)](https://pypi.org/project/smartpasslib)

[![PyPI Downloads](https://static.pepy.tech/badge/smartpasslib)](https://pepy.tech/projects/smartpasslib)
[![PyPI Downloads](https://static.pepy.tech/badge/smartpasslib/month)](https://pepy.tech/projects/smartpasslib)
[![PyPI Downloads](https://static.pepy.tech/badge/smartpasslib/week)](https://pepy.tech/projects/smartpasslib)

Your passwords don't need to be stored because they were never created - they already exist as mathematical certainties, waiting to be discovered through the correct combination of login and secret phrase.

---

## 📦 Installation

```bash
pip install smartpasslib
```

## 🧙‍♂️ Quick Start: Discover Your First Password

```python
from smartpasslib import SmartPasswordMaster

# Your secret phrase is the key to the infinite password library
secret = "myQuantumUniverse42$"

# Discover the password that was always yours
password = SmartPasswordMaster.generate_smart_password(
    login="alice@quantum.org", 
    secret=secret, 
    length=16
)
print(f"Your discovered password: {password}")
# '4_u4k!j^6SdDW$I7' - This was always your password!
```

## 🔑 The Magic of Verification Without Storage

```python
# Generate a public verification key (safe to store anywhere)
public_key = SmartPasswordMaster.generate_public_key(
    login="alice@quantum.org", 
    secret="myQuantumUniverse42$"
)

# Later, verify you can rediscover the same password
is_valid = SmartPasswordMaster.check_public_key(
    login="alice@quantum.org",
    secret="myQuantumUniverse42$",
    public_key=public_key
)  # Returns True - The password is still there!
```

## 🏗️ Core Components

### 1. SmartPasswordMaster - Your Guide to the Password Library

```python
from smartpasslib import SmartPasswordMaster

# Discover different types of passwords
basic_pass = SmartPasswordMaster.generate_base_password(length=12)
strong_pass = SmartPasswordMaster.generate_strong_password(length=14)
smart_pass = SmartPasswordMaster.generate_smart_password("user", "secret", 16)

# Key management for verification
public_key = SmartPasswordMaster.generate_public_key("user", "secret")
is_valid = SmartPasswordMaster.check_public_key("user", "secret", public_key)
```

### 2. SmartPasswordManager - Organize Your Discoveries

```python
from smartpasslib import SmartPasswordManager, SmartPassword, SmartPasswordMaster

manager = SmartPasswordManager()

# "Store" password coordinates (not the password itself!)
public_key = SmartPasswordMaster.generate_public_key(
    "bank@account.com", 
    "financialSecret123"
)
password_data = SmartPassword(
    login="bank@account.com", 
    key=public_key, 
    length=18
)
manager.add_smart_password(password_data)

# "Retrieve" by rediscovering from the secret
account = manager.get_smart_password("bank@account.com")
password = SmartPasswordMaster.generate_smart_password(
    account.login,
    "financialSecret123",
    account.length
)
```

## 🚀 Advanced Usage

### Password Generation Options

| Method                       | Description                             | Perfect For          |
|------------------------------|-----------------------------------------|----------------------|
| `generate_base_password()`   | Simple random discovery                 | Temporary access     |
| `generate_strong_password()` | Discovery with character requirements   | User accounts        |
| `generate_smart_password()`  | Deterministic discovery from credentials | Main use case        |
| `generate_code()`            | Discover 2FA codes                      | Authentication       |

### Complete Usage Examples

**CLI Password Discovery Tool:**
```python
from smartpasslib import SmartPasswordMaster

login = input("Enter your login: ")
secret = input("Enter your secret phrase: ")
password = SmartPasswordMaster.generate_smart_password(login, secret, 14)
print(f"Discovered password: {password}")
```

**Two-Factor Code Discovery:**
```python
from smartpasslib.generators.code import CodeGenerator

# Discover authentication codes that were always waiting
auth_code = CodeGenerator.generate(6)  # '4&TkIP'
print(f"Your auth code: {auth_code}")
```

## 🌐 Ecosystem Applications Built on SmartPassLib

Explore my suite of applications that implement the "discovery over storage" paradigm:

### 🔧 Console Tools
- [**CLI PassGen**](https://github.com/smartlegionlab/clipassgen/) - Console password discovery tool

- [**CLI PassMan**](https://github.com/smartlegionlab/clipassman/) - Console password manager

### 🖥️ Desktop & Web Applications
- [**Web Password Manager**](https://github.com/smartlegionlab/smart-password-manager) - Web-based discovery interface

- [**Desktop Manager**](https://github.com/smartlegionlab/smart-password-manager-desktop) - Cross-platform desktop application

## 💻 For Developers

### Development Setup
```bash
pip install pytest pytest-cov setuptools wheel build
pytest tests/ -v
pytest tests/ -v --cov=smartpasslib --cov-report=html
python -m build
twine upload dist/*
```

### Testing Coverage
![Test Coverage](https://github.com/smartlegionlab/smartpasslib/raw/master/data/images/cov.png)

## 📜 License & Disclaimer

BSD 3-Clause License

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

*Discover more revolutionary projects at [Smart Legion Lab](https://github.com/smartlegionlab)*
