# Migration Guide: v1.x.x / v2.x.x / v3.x.x to v4.0.0

> **📌 Version Note:** smartpasslib v4.0.0 introduces breaking changes from all previous versions (v1.x.x, v2.x.x, v3.x.x). All smartpasslib implementations (Python, C#, JS, Go, Kotlin) now share the same version number and algorithm.

## ⚠️ Breaking Change Notice

**smartpasslib v4.0.0 is NOT backward compatible with v1.x.x, v2.x.x, or v3.x.x**

| Version    | Status      | Why                                                         |
|------------|-------------|-------------------------------------------------------------|
| v1.x.x     | Deprecated  | Used `random.choice()`, insecure; used `login`              |
| v2.x.x     | Deprecated  | Used `random.seed()` - Python-only deterministic            |
| v3.x.x     | Deprecated  | Fixed steps (30/60), limited character set                  |
| **v4.0.0** | **Current** | Dynamic steps (15-30/45-60), expanded charset, max security |

Passwords generated with older versions cannot be regenerated using v4.0.0 
due to fundamental changes in the deterministic generation algorithm.

---

## Why the change?

**smartpasslib v4.0.0 introduces fundamental improvements:**

- **Dynamic iteration counts** — deterministic steps vary per secret (15-30 for private, 45-60 for public)
- **Expanded character set** — Google-compatible symbols
- **Enhanced key derivation** — salt separation for public/private keys ("private"/"public")
- **Unified length validation** — password length must be 12-100 characters
- **Input validation** — secret phrases must be at least 12 characters
- **Maximum security** — no secret exposure in logs or iterations

---

## What changed:

- Private key steps: dynamic (15-30 instead of fixed 30)
- Public key steps: dynamic (45-60 instead of fixed 60)
- **Salt separation**: "private" and "public" salts added for key isolation
- Character set: expanded to Google-compatible symbols
- Password length: min 12, max 100 (was min 4)
- Secret validation: min 12 characters (enforced)
- `SmartPasswordFactory` removed (use `SmartPassword` directly)

## ⚠️ Metadata and Backup Files Compatibility

**Old metadata files (`passwords.json`) are NOT compatible with v4.0.0**

- Public keys generated with v3.x.x will NOT work with v4.0.0
- Reason: Iteration counts changed (60 → 45-60 dynamic) + salt "public" added
- **Backup files from older versions cannot be restored directly**

### What to do with old metadata:

```python
# Old v3.x.x backup file contains public keys (no longer valid)
# You need to regenerate public keys:

from smartpasslib import SmartPasswordMaster

secret = "your_secret_phrase"
new_public_key = SmartPasswordMaster.generate_public_key(secret)

# Update your stored metadata with new public key
```

---

## Migration Steps

The migration process is the SAME for all previous versions (v1.x.x, v2.x.x, v3.x.x):

### Step 1: Keep your current old version installed

Continue using your current version to retrieve existing passwords.

### Step 2: Retrieve all existing passwords

For each service, generate the actual password using your secret phrase with your current old version:

```python
from smartpasslib.generators.smart import SmartPasswordGenerator

old_password = SmartPasswordGenerator.generate("your_secret_phrase", length)
```

**Save ALL retrieved passwords** in a safe place. You will need them to update your services after migration.

### Step 3: Backup your metadata file

Backup your existing `passwords.json` file (for reference only, it will NOT work with v4.0.0):

```bash
cp ~/.config/smart_password_manager/passwords.json ~/passwords.json.v3.backup
```

### Step 4: Upgrade to v4.0.0

```bash
pip install --upgrade smartpasslib
```

### Step 5: Generate new passwords

Using the **SAME secret phrases and lengths**, generate new passwords:

```python
from smartpasslib.generators.smart import SmartPasswordGenerator

new_password = SmartPasswordGenerator.generate("your_secret_phrase", length)
```

### Step 6: Generate new public keys

```python
from smartpasslib import SmartPasswordMaster

new_public_key = SmartPasswordMaster.generate_public_key("your_secret_phrase")
```

### Step 7: Recreate your metadata entries

Your old `passwords.json` is NOT compatible. You need to recreate entries:

```python
from smartpasslib import SmartPasswordManager, SmartPassword

manager = SmartPasswordManager()
smart_pass = SmartPassword(
    public_key=new_public_key,
    description="your_service_description",
    length=length
)
manager.add_smart_password(smart_pass)
```

### Step 8: Update your services

Replace old passwords (from Step 2) with newly generated ones (from Step 5) on each website/service.

### Step 9: Verify

- Log in using new passwords
- Confirm regeneration works (same secret → same password)
- Test with non-essential accounts first

---

## Important Notes

- **No automatic migration** — manual regeneration required for each password
- **Your secret phrases remain the same** — only generated passwords change
- **Secret phrases shorter than 12 characters will now raise ValueError**
- **Password lengths shorter than 12 or longer than 100 will now raise ValueError**
- **Old metadata files (`passwords.json`) are NOT compatible** — must be recreated
- **Backup files from older versions cannot be restored** — keys use different derivation
- Older versions still available for reference
- Test with non-essential accounts first

---

## Need Help?

- **Issues**: [GitHub Issues](https://github.com/smartlegionlab/smartpasslib/issues)

---

