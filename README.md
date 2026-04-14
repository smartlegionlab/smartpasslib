# smartpasslib (Smart Passwords Library) <sup>v3.0.0</sup>

---

**Smart Passwords Library**: Cryptographic password generation and management without storage. Generate passwords from secrets, verify knowledge without exposure, manage metadata securely.

**Now with Cross-Platform Determinism**: Same secret + same parameters = identical password on **Python, Go, Kotlin, JavaScript, C#** and any language with SHA-256.

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

## ⚠️ Breaking Changes (v3.0.0)

**This version is NOT backward compatible with v1.x.x and v2.x.x**

| Version | Status | Why                                              |
|---------|--------|--------------------------------------------------|
| v1.x.x | Deprecated | Used `random.choice()`, `login` - insecure, excessively     |
| v2.x.x | Deprecated | Used `random.seed()` - Python-only deterministic |
| **v3.x.x** | **Current** | Uses **SHA-256** - cross-platform deterministic  |

**What changed:**
- `SmartPasswordGenerator` now uses **SHA-256** instead of `random.seed()` and SHA3-512
- `BasePasswordGenerator` now uses **`secrets.choice()`** instead of `random.choice()`
- Character set changed: `!@#$%&^_` → `!@#$&*-_` (removed `^` and `%`, added `*` and `-`)
- Deterministic passwords now work identically across **all programming languages**

**Migration impact:**
- Old deterministic passwords will **NOT match** new ones
- Update any tests expecting specific password outputs
- Re-generate passwords for all services using old versions

**Why this is better:**
- Same secret + same length = **identical password** on Python, Go, Kotlin, JS, C#
- Based on **SHA-256** (NIST standard) — not Python-specific
- Cryptographically secure by default

---

## Core Principles:

- **Zero-Storage Security**: No passwords or secret phrases are ever stored or transmitted
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

**Key Features:**
- **No Password Database**: Eliminates the need for password storage
- **No Secret Storage**: Secret phrases never leave your control
- **Cross-Platform Determinism**: Same results on Python, Go, Kotlin, JavaScript, C#
- **Public Key Verification**: Verify secrets without exposing them
- **Multiple Generator Types**: Smart, strong, base, and code generators
- **Store Only Public Metadata**: Descriptions and public keys can be stored; private keys and secrets are NEVER persisted
- **Full Test Coverage**: 100% tested for reliability and security

---

## Security Model:

- **Proof of Knowledge**: Verify you know a secret without storing or transmitting it
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

The library implements **cross-platform deterministic password generation** - passwords are generated reproducibly from secret phrases using **SHA-256** cryptographic hash function.

**Why SHA-256 instead of SHA3-512:**
- **Cross-platform standard** - Available in every programming language by default
- **NIST certified** - FIPS 180-4 compliant, used in Bitcoin, TLS, JWT
- **256-bit security** - Quantum-resistant (128-bit effective with Grover's algorithm)
- **Performance** - Faster on 32-bit and 64-bit systems
- **Sufficient for passwords** - 256 bits of entropy is impossible to brute force

**Key principle**: Instead of storing passwords, you store verification metadata. The actual password is regenerated on-demand from your secret.

**Cross-Platform Guarantee**:
- Same secret phrase + same length = **identical password** on any platform
- Implemented in Python, Go, Kotlin, JavaScript, C#
- Based on SHA-256 (NIST standard) — not language-specific

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

## What's New in v3.0.0

### Breaking Changes (Migration Required):
- **SmartPasswordGenerator now uses SHA-256** — passwords differ from v1.x and v2.x
- **BasePasswordGenerator uses `secrets.choice()`** — cryptographically secure, different output
- **Character set changed**: `!@#$%&^_` → `!@#$&*-_` (removed `^` and `%`, added `*` and `-`)
- **No backward compatibility** with versions 1.x.x and 2.x.x

### Cross-Platform Determinism (NEW):
- **Same secret → same password** on Python, Go, Kotlin, JavaScript, C#
- **SHA-256 based** — NIST standard, not Python-specific
- **Test vectors** available for all languages

### Security Improvements:
- **No more `random` module** in any generator
- **`secrets.choice()`** for cryptographically secure random passwords
- **Problematic symbols removed**

### Code Quality:
- **Unified character sets** via `PasswordChars` mixin
- **No code duplication** across generators
- **100% test coverage** maintained

### Storage Improvements:
- **New config location**: `~/.config/smart_password_manager/passwords.json`
- **Automatic migration**: Legacy `~/.cases.json` files are auto-migrated on first use
- **Cross-platform paths**: Uses `Path.home()` for all OS support

### Migration Guide (v2.x → v3.x):

```python
# OLD (v2.x) - STILL WORKS, BUT GIVES DIFFERENT RESULTS
# from smartpasslib.generators.smart import SmartPasswordGenerator
# password = SmartPasswordGenerator.generate("my_secret", 16)
# Output: m2m#4kb#RO6vAu2e (for example)

# NEW (v3.x) - USE THIS FOR CROSS-PLATFORM DETERMINISM
from smartpasslib.generators.smart import SmartPasswordGenerator
password = SmartPasswordGenerator.generate("my_secret", 16)
# Output: 560wjO-w3Kcl&Tc0 (DIFFERENT from v2.x!)
# Same secret gives SAME password on Python, Go, Kotlin, JS, C#!
```

**Action required:**
1. Old code still works, but produces DIFFERENT passwords than before
2. If you need the OLD behavior → pin to `smartpasslib==2.2.2`
3. If you migrate to v3.x → re-generate all passwords for your services

**Why the change:**
- v2.x used `random.seed()` + SHA3-512 (Python-specific)
- v3.x uses SHA-256 (cross-platform standard)
- Same input → different output by design (different algorithm)

---

## Installation

```bash
pip install smartpasslib
```

---

## File Locations

Configuration files are stored in:

| Platform | Configuration Path |
|----------|-------------------|
| Linux | `~/.config/smart_password_manager/passwords.json` |
| macOS | `~/.config/smart_password_manager/passwords.json` |
| Windows | `C:\Users\Username\.config\smart_password_manager\passwords.json` |

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
# Output: i&h!lLy&ONxC
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

## Cross-Platform Example

**Same secret → same password on any language:**

### Python:

```python
from smartpasslib.masters.smart_password_master import SmartPasswordMaster

secrets = ["my_secret_key", "test123", "hello_world"]
for secret in secrets:
    password = SmartPasswordMaster.generate_smart_password(secret, 12)
    print(f"secret: {secret:<20} -> password: {password}")

print("\n--- Testing determinism ---")
p1 = SmartPasswordMaster.generate_smart_password("secret", 12)
p2 = SmartPasswordMaster.generate_smart_password("secret", 12)
print(f"First call:  {p1}")
print(f"Second call: {p2}")
print(f"Match: {p1 == p2}")
```

**Output:**
```text
secret: my_secret_key        -> password: i&h!lLy&ONxC
secret: test123              -> password: 5AM*aF9MqEai
secret: hello_world          -> password: NQK8w$MdbFn8

--- Testing determinism ---
First call:  wQq-0&Qzl0GT
Second call: wQq-0&Qzl0GT
Match: True
```

### Go:

```go
package main

import (
    "crypto/sha256"
    "encoding/hex"
    "fmt"
)

var chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$&*-_"

func getHash(text string) string {
    hash := sha256.Sum256([]byte(text))
    return hex.EncodeToString(hash[:])
}

func generatePrivateKey(secret string) string {
    steps := 30
    allHash := getHash(secret)

    for i := 0; i < steps; i++ {
        tempString := fmt.Sprintf("%s:%s:%d", allHash, secret, i)
        allHash = getHash(tempString)
    }

    return allHash
}

func generateSmartPassword(secret string, length int) string {
    if length <= 0 {
        length = 12
    }

    seed := generatePrivateKey(secret)

    result := make([]byte, 0, length)
    counter := 0

    for len(result) < length {
        data := fmt.Sprintf("%s:%d", seed, counter)
        hash := sha256.Sum256([]byte(data))

        for _, b := range hash {
            if len(result) < length {
                result = append(result, chars[b%byte(len(chars))])
            }
        }
        counter++
    }

    return string(result)
}

func main() {
    secrets := []string{"my_secret_key", "test123", "hello_world"}

    for _, secret := range secrets {
        password := generateSmartPassword(secret, 12)
        fmt.Printf("secret: %-20s -> password: %s\n", secret, password)
    }

    fmt.Println("\n--- Testing determinism ---")
    p1 := generateSmartPassword("secret", 12)
    p2 := generateSmartPassword("secret", 12)
    fmt.Printf("First call:  %s\n", p1)
    fmt.Printf("Second call: %s\n", p2)
    fmt.Printf("Match: %v\n", p1 == p2)
}
```

**Output:**
```text
secret: my_secret_key        -> password: i&h!lLy&ONxC
secret: test123              -> password: 5AM*aF9MqEai
secret: hello_world          -> password: NQK8w$MdbFn8

--- Testing determinism ---
First call:  wQq-0&Qzl0GT
Second call: wQq-0&Qzl0GT
Match: true
```

### Kotlin:

```kotlin
#!/usr/bin/env kotlin

import java.security.MessageDigest
import java.math.BigInteger

val chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$&*-_"

fun getHash(text: String): String {
    val digest = MessageDigest.getInstance("SHA-256")
    val hash = digest.digest(text.toByteArray())
    return BigInteger(1, hash).toString(16).padStart(64, '0')
}

fun generatePrivateKey(secret: String): String {
    val steps = 30
    var allHash = getHash(secret)

    for (i in 0 until steps) {
        val tempString = "$allHash:$secret:$i"
        allHash = getHash(tempString)
    }

    return allHash
}

fun generateSmartPassword(secret: String, length: Int): String {
    var counter = 0
    val result = StringBuilder()

    val seed = generatePrivateKey(secret)

    while (result.length < length) {
        val data = "$seed:$counter"
        val hash = MessageDigest.getInstance("SHA-256").digest(data.toByteArray())

        for (byte in hash) {
            if (result.length < length) {
                val index = byte.toInt() and 0xFF
                result.append(chars[index % chars.length])
            }
        }
        counter++
    }

    return result.toString()
}

val secrets = listOf("my_secret_key", "test123", "hello_world")

for (secret in secrets) {
    val password = generateSmartPassword(secret, 12)
    println("secret: ${secret.padEnd(20)} -> password: $password")
}

println("\n--- Testing determinism ---")
val p1 = generateSmartPassword("secret", 12)
val p2 = generateSmartPassword("secret", 12)
println("First call:  $p1")
println("Second call: $p2")
println("Match: ${p1 == p2}")
```

**Output:**
```text
secret: my_secret_key        -> password: i&h!lLy&ONxC
secret: test123              -> password: 5AM*aF9MqEai
secret: hello_world          -> password: NQK8w$MdbFn8

--- Testing determinism ---
First call:  wQq-0&Qzl0GT
Second call: wQq-0&Qzl0GT
Match: true
```

### JavaScript (Browser):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Smart Password Generator - Cross-Platform Test</title>
</head>
<body>
    <h1>Smart Password Generator (SHA-256 + SmartKeyGenerator)</h1>
    <p>Same secret → same password as Python, Go, Kotlin</p>

    <label>Secret:</label>
    <input type="text" id="secret" value="my_secret_key" size="30">

    <label>Length:</label>
    <input type="number" id="length" value="12" min="1" max="64">

    <button onclick="generate()">Generate Password</button>

    <h2>Result:</h2>
    <input type="text" id="result" readonly size="40" style="font-family: monospace; font-size: 16px;">

    <hr>
    <h3>Test Vectors:</h3>
    <button onclick="testVectors()">Run Tests</button>
    <pre id="testOutput"></pre>

    <script>
        const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$&*-_";

        async function sha256(text) {
            const encoder = new TextEncoder();
            const hashBuffer = await crypto.subtle.digest('SHA-256', encoder.encode(text));
            const hashArray = Array.from(new Uint8Array(hashBuffer));
            return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
        }

        async function getHash(text) {
            return await sha256(text);
        }

        async function generatePrivateKey(secret) {
            const steps = 30;
            let allHash = await getHash(secret);

            for (let i = 0; i < steps; i++) {
                const tempString = `${allHash}:${secret}:${i}`;
                allHash = await getHash(tempString);
            }

            return allHash;
        }

        async function generateSmartPassword(secret, length) {
            const seed = await generatePrivateKey(secret);

            let result = [];
            let counter = 0;

            while (result.length < length) {
                const data = `${seed}:${counter}`;
                const hashHex = await sha256(data);
                const hashBytes = hexToBytes(hashHex);

                for (let i = 0; i < hashBytes.length; i++) {
                    if (result.length < length) {
                        result.push(chars[hashBytes[i] % chars.length]);
                    }
                }
                counter++;
            }

            return result.join('');
        }

        function hexToBytes(hex) {
            const bytes = [];
            for (let i = 0; i < hex.length; i += 2) {
                bytes.push(parseInt(hex.substr(i, 2), 16));
            }
            return bytes;
        }

        async function generate() {
            const secret = document.getElementById('secret').value;
            const length = parseInt(document.getElementById('length').value);
            const password = await generateSmartPassword(secret, length);
            document.getElementById('result').value = password;
        }

        async function testVectors() {
            const tests = [
                { secret: "my_secret_key", length: 12 },
                { secret: "test123", length: 12 },
                { secret: "hello_world", length: 12 },
                { secret: "secret", length: 12 }
            ];

            let output = "";

            for (const test of tests) {
                const result = await generateSmartPassword(test.secret, test.length);
                output += `secret: "${test.secret}" (len=${test.length})\n`;
                output += `   Got: ${result}\n\n`;
            }

            output += "Compare with Python output manually";
            document.getElementById('testOutput').textContent = output;
        }

        window.onload = () => generate();
    </script>
</body>
</html>
```

**Output:**
```text
secret: "my_secret_key" (len=12)
   Got: i&h!lLy&ONxC

secret: "test123" (len=12)
   Got: 5AM*aF9MqEai

secret: "hello_world" (len=12)
   Got: NQK8w$MdbFn8

secret: "secret" (len=12)
   Got: wQq-0&Qzl0GT

Compare with Python output manually
```

---

## Core Components

### SmartPasswordMaster - Main Interface

```python
from smartpasslib import SmartPasswordMaster

# Generate different types of passwords
base_password = SmartPasswordMaster.generate_base_password(length=12)
# Output example: JcAmAN-QIXHm

strong_password = SmartPasswordMaster.generate_strong_password(length=14)
# Output example: YFYCkqg#8W!_pH

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
public_key = SmartPasswordMaster.generate_public_key("github_secret")
smart_pass = SmartPassword(
    public_key=public_key,
    description="GitHub account",
    length=18
)
manager.add_smart_password(smart_pass)

# Retrieve and regenerate password when needed
stored_metadata = manager.get_smart_password(public_key)
regenerated_password = SmartPasswordMaster.generate_smart_password(
    "github_secret",
    stored_metadata.length
)
print(regenerated_password) # 3vQW6WHsbTo6YanMLJ
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
# Output: i&h!lLy&ONxC (SAME on Go, Kotlin, JS, C#!)
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

## Ecosystem

### Command Line Tools
- **[CLI Smart Password Generator](https://github.com/smartlegionlab/clipassgen/)** - Generate passwords from terminal
- **[CLI Smart Password Manager](https://github.com/smartlegionlab/clipassman/)** - Manage password metadata

### Graphical Applications
- **[Web Smart Password Manager](https://github.com/smartlegionlab/smart-password-manager-web)** - Browser-based interface
- **[Desktop Smart Password Manager](https://github.com/smartlegionlab/smart-password-manager-desktop)** - Cross-platform desktop app

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

## License

**[BSD 3-Clause License](LICENSE)**

Copyright (©) 2026, [Alexander Suvorov](https://github.com/smartlegionlab)

---

## Support

- **Issues**: [GitHub Issues](https://github.com/smartlegionlab/smartpasslib/issues)
- **Documentation**: Inline code documentation
- **Tests**: 100% coverage ensures reliability

---

## Security Warnings

### Secret Phrase Security

**Your secret phrase is the cryptographic master key**

1. **Permanent data loss**: Lost secret phrase = irreversible loss of all derived passwords
2. **No recovery mechanisms**: No password recovery, no secret reset, no administrative override
3. **Deterministic generation**: Identical input = identical output **on any platform**
4. **Single point of failure**: Secret phrase is the sole authentication factor
5. **Secure storage required**: Digital storage of secret phrases is prohibited

**Critical**: Test password regeneration with non-essential accounts before production use
**Note**: Always test password generation in your specific environment. Implementation security depends on proper usage.

---

