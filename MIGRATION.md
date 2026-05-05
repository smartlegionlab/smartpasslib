# Migration Guide: v1.x.x / v2.x.x / v3.x.x to v4.0.0

## ⚠️ Breaking Change Notice

**smartpasslib v4.0.0 is NOT backward compatible with v1.x.x, v2.x.x, or v3.x.x**

| Version    | Status      | Why                                                         |
|------------|-------------|-------------------------------------------------------------|
| v1.x.x     | Deprecated  | Used `random.choice()`, - insecure; used `login`            |
| v2.x.x     | Deprecated  | Used `random.seed()` - Python-only deterministic            |
| v3.x.x     | Deprecated  | Fixed steps (30/60), limited character set                  |
| **v4.0.0** | **Current** | Dynamic steps (15-30/45-60), expanded charset, max security |

Passwords generated with older versions cannot be regenerated using v4.0.0 
due to fundamental changes in the deterministic generation algorithm.

---

## Why the change?

**smartpasslib v4.0.0 introduces fundamental improvements:**

- **Dynamic iteration counts** — deterministic steps vary per secret (15-30 for private, 45-60 for public)
- **Expanded character set** — Google-compatible symbols: `!@#$%^&*()_+-=[]{};:,.<>?/`
- **Enhanced key derivation** — salt separation for public/private keys
- **Unified length validation** — password length must be 12-100 characters
- **Input validation** — secret phrases must be at least 12 characters
- **Maximum security** — no secret exposure in logs or iterations

---

## What changed:

- Private key steps: dynamic (15-30 instead of fixed 30)
- Public key steps: dynamic (45-60 instead of fixed 60)
- Character set: expanded to Google-compatible symbols
- Password length: min 12, max 100 (was min 4)
- Secret validation: min 12 characters (enforced)
- `SmartPasswordFactory` removed (use `SmartPassword` directly)
- Old metadata (`passwords.json`) will produce **different passwords** if used with v4.0.0

---

## Migration Steps from v3.x.x to v4.0.0

### Step 1: Install old version (if on v3.x.x)

```bash
pip install smartpasslib==3.0.2
```

### Step 2: Retrieve existing passwords

For each service, generate the actual password using your secret phrase:

```python
from smartpasslib.generators.smart import SmartPasswordGenerator

old_password = SmartPasswordGenerator.generate("your_secret_phrase", length)
```

Keep these passwords accessible during migration.

### Step 3: Upgrade to v4.0.0

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
- **Secret phrases shorter than 12 characters will now raise ValueError**
- **Password lengths shorter than 12 or longer than 100 will now raise ValueError**
- Older versions still available: `pip install smartpasslib==3.1.0`
- Test with non-essential accounts first

---

## Migration from v1.x.x / v2.x.x

First migrate to v3.x.x following the v3 migration guide, then to v4.0.0.

---

## Need Help?

- **Issues**: [GitHub Issues](https://github.com/smartlegionlab/smartpasslib/issues)

