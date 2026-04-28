# Migration Guide: v1.x.x / v2.x.x to v3.x.x

## ⚠️ Breaking Change Notice

**smartpasslib v3.x.x is NOT backward compatible with v1.x.x and v2.x.x**

| Version    | Status      | Why                                                     |
|------------|-------------|---------------------------------------------------------|
| v1.x.x     | Deprecated  | Used `random.choice()`, `login` - insecure              |
| v2.x.x     | Deprecated  | Used `random.seed()` - Python-only deterministic        |
| **v3.x.x** | **Current** | Uses **SHA-256** - cross-platform deterministic         |

Passwords generated with older versions cannot be regenerated using v3.x.x 
due to fundamental changes in the deterministic generation algorithm.

---

## Why the change?

**smartpasslib v3.x.x introduces fundamental improvements:**

- **Cross-platform determinism** — same secret → same password on Python, Go, Kotlin, JavaScript, C#
- **Decentralized by design** — no central servers, no cloud dependency, complete user sovereignty
- **Stronger cryptographic algorithm** — enhanced deterministic generation with better entropy distribution
- **Improved performance** — faster password generation, especially for longer passwords
- **Extended character set support** — wider range of special characters for stronger passwords
- **Future-ready architecture** — simplified updates and security patching

---

## What changed:

- `SmartPasswordGenerator` now uses **SHA-256** instead of `random.seed()` and SHA3-512
- `BasePasswordGenerator` now uses **`secrets.choice()`** instead of `random.choice()`
- Character set changed: `!@#$%&^_` → `!@#$&*-_` (removed `^` and `%`, added `*` and `-`)
- Deterministic passwords now work identically across **all programming languages**
- Old metadata (`passwords.json`) will produce **different passwords** if used with v3.x.x

---

## Migration Steps

### Step 1: Install old version

```bash
pip install smartpasslib==2.2.2
```

### Step 2: Retrieve existing passwords

For each service, generate the actual password using your secret phrase and the old version:

```python
from smartpasslib.generators.smart import SmartPasswordGenerator

old_password = SmartPasswordGenerator.generate("your_secret_phrase", length)
```

Keep these passwords accessible during migration.

### Step 3: Upgrade to v3.x.x

```bash
pip install --upgrade smartpasslib
```

### Step 4: Generate new passwords

Using the **same secret phrases and lengths**, generate new passwords:

```python
from smartpasslib.generators.smart import SmartPasswordGenerator

new_password = SmartPasswordGenerator.generate("your_secret_phrase", length)
```

### Step 5: Update your services

Replace old passwords with newly generated ones on each website/service.

### Step 6: Verify

- Log in using new passwords
- Confirm regeneration works (same secret → same password)

---

## Important Notes

- **No automatic migration** — manual regeneration required for each password
- **Your secret phrases remain the same** — only generated passwords change
- Old version still available: `pip install smartpasslib==2.2.2`
- Test with non-essential accounts first

---

## Need Help?

- **Issues**: [GitHub Issues](https://github.com/smartlegionlab/smartpasslib/issues)
- **Core Library Issues**: [smartpasslib Issues](https://github.com/smartlegionlab/smartpasslib/issues)

