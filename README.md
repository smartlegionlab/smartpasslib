# Smart Passwords Library (smartpasslib) <sup>v1.0.3</sup>

[![PyPI - Downloads](https://img.shields.io/pypi/dm/smartpasslib?label=pypi%20downloads)](https://pypi.org/project/smartpasslib/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smartpasslib)](https://github.com/smartlegionlab/smartpasslib/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smartpasslib)
[![PyPI](https://img.shields.io/pypi/v/smartpasslib)](https://pypi.org/project/smartpasslib)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smartpasslib)](https://github.com/smartlegionlab/smartpasslib/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/smartpasslib)](https://pypi.org/project/smartpasslib)

[![PyPI Downloads](https://static.pepy.tech/badge/smartpasslib)](https://pepy.tech/projects/smartpasslib)
[![PyPI Downloads](https://static.pepy.tech/badge/smartpasslib/month)](https://pepy.tech/projects/smartpasslib)
[![PyPI Downloads](https://static.pepy.tech/badge/smartpasslib/week)](https://pepy.tech/projects/smartpasslib)

A cross-platform Python library for generating deterministic, secure passwords that never need to be stored.

## 🔥 Key Features

- 🚀 **On-the-fly generation** - Passwords are generated when needed, not stored
- 🔒 **Cryptographically secure** - Uses SHA3-512 and system entropy
- 🔄 **Deterministic output** - Same input always produces same password
- 📱 **Cross-platform** - Works on Linux, Windows, macOS, and Android (Termux)
- 🛠️ **Developer-friendly** - Clean API with full type hints

## 🤝 Supported:

- Linux: All.
- Windows: 7/8/10/11?.
- Termux (Android).

## 📦 Installation

```bash
pip install smartpasslib
```

## 🚀 Quick Start

```python
from smartpasslib import SmartPasswordMaster

# Initialize generator
spm = SmartPasswordMaster()

# Generate a smart password
login = "user@example.com"
secret = "mySecretPhrase"
password = spm.generate_smart_password(login=login, secret=secret, length=16)

# Verify later (without storing the password)
key = spm.generate_public_key(login, secret)
is_valid = spm.check_public_key(login, secret, key)  # Returns True
```

## ⚙️ Core Components

### 1. SmartPasswordMaster
The main class for password generation and verification:

```python
from smartpasslib import SmartPasswordMaster
# Generate different types of passwords
basic_pass = SmartPasswordMaster.generate_base_password(length=12)
strong_pass = SmartPasswordMaster.generate_strong_password(length=14)
login = "user@example.com"
secret = "mySecretPhrase"
smart_pass = SmartPasswordMaster.generate_smart_password(login, secret, 16)

# Key management
public_key = SmartPasswordMaster.generate_public_key(login, secret)
is_valid = SmartPasswordMaster.check_public_key(login, secret, public_key)
```

### 2. SmartPasswordManager
For managing password metadata:

```python
from smartpasslib import SmartPasswordManager, SmartPassword, SmartPasswordMaster

manager = SmartPasswordManager()
login = "user@example.com"
secret = "mySecretPhrase"
public_key = SmartPasswordMaster.generate_public_key(login, secret)

# Create and store password metadata
password = SmartPassword(login="user@example.com", 
                        key=public_key, 
                        length=16)
manager.add_smart_password(password)

# Retrieve later
stored_pass = manager.get_smart_password("user@example.com")
```

## 🔧 Advanced Usage

### Password Generation Options
| Method                       | Description                             | Recommended Use     |
|------------------------------|-----------------------------------------|---------------------|
| `generate_base_password()`   | Simple random password                  | Temporary passwords |
| `generate_strong_password()` | Password with character requirements    | User accounts       |
| `generate_smart_password()`  | Deterministic password from credentials | Main use case       |

### Security Notes
- Always keep your `secret` secure - it's required to regenerate passwords
- The `public_key` can be safely stored for verification
- Minimum recommended password length is 12 characters

## 📚 Examples

### CLI Password Generator
```python
from smartpasslib import SmartPasswordMaster

login = input("Enter your login: ")
secret = input("Enter your secret: ")
password = SmartPasswordMaster.generate_smart_password(login, secret, 14)
print(f"Your password: {password}")
```

### Password Manager Integration
```python
from smartpasslib import SmartPasswordManager, SmartPassword, SmartPasswordMaster
manager = SmartPasswordManager()

# Add new account
new_account = SmartPassword(
    login="work_email@company.com",
    key=SmartPasswordMaster.generate_public_key("work_email@company.com", "workSecret123"),
    length=18
)
manager.add_smart_password(new_account)

# Retrieve password later
account = manager.get_smart_password("work_email@company.com")
password = SmartPasswordMaster.generate_smart_password(
    account.login,
    "workSecret123",
    account.length
)
```

### Generate codes for two-factor authentication
```python
from smartpasslib.generators.code import CodeGenerator

code = CodeGenerator.generate(6) # '4&TkIP'
```

## 📝 Changelog

### v1.0.3
- Added tools for generating codes for two-factor authentication
- Added tests

> ⚠️ Note: Some deprecated methods will be removed in future versions

## 📜 Licensing

This project uses a dual licensing system:

### 🆓 BSD 3-Clause License
- For non-commercial use
- For academic and research purposes
- For open-source projects

### 💼 Commercial License
- For commercial products and services
- For enterprises using the code in proprietary solutions
- For additional features and support

**To obtain a commercial license:** [smartlegiondev@gmail.com](mailto:smartlegiondev@gmail.com)

## Related Projects
- [Console Password Generator](https://github.com/smartlegionlab/clipassgen/)
- [Console Password Manager](https://github.com/smartlegionlab/clipassman/)
- [Telegram Bot Manager](https://t.me/smartpasswordmanagerbot)
- [Desktop Manager](https://github.com/smartlegionlab/smart_password_manager_desktop/)


## 💻 Information for developers:

- `pip install pytest`
- `pip install pytest-cov`
- `pip install setuptools`
- `pip install wheel`
- `pip install build`

- `pytest tests/ -v`
- `pytest tests/ -v --cov=smartpasslib --cov-report=html`
- `python -m build` or `python setup.py sdist bdist_wheel`
- `twine upload dist/*`

![LOGO](https://github.com/smartlegionlab/smartpasslib/raw/master/data/images/cov.png)

***

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
