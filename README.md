# smartpasslib

***

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smartpasslib)](https://github.com/smartlegionlab/smartpasslib/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smartpasslib?label=pypi%20downloads)](https://pypi.org/project/smartpasslib/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smartpasslib)
[![PyPI](https://img.shields.io/pypi/v/smartpasslib)](https://pypi.org/project/smartpasslib)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smartpasslib)](https://github.com/smartlegionlab/smartpasslib/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/smartpasslib)](https://pypi.org/project/smartpasslib)

***


Author and developer: ___A.A Suvorov___

[![smartlegiondev@gmail.com](https://img.shields.io/static/v1?label=email:&message=smartlegiondev@gmail.com&color=blue)](mailto:smartlegiondev@gmail.com)

***

## Help the project financially:

- Yandex Money: [https://yoomoney.ru/to/4100115206129186](https://yoomoney.ru/to/4100115206129186)
- PayPal: [https://paypal.me/smartlegionlab](https://paypal.me/smartlegionlab)
- LiberaPay: [https://liberapay.com/smartlegion/donate](https://liberapay.com/smartlegion/donate)
- Visa: 4048 0250 0089 5923

***

## Short Description:
___smartpasslib___ - A cross-platform package of modules for generating, 
secure storage and recovery of complex, cryptographic, smart passwords on the fly.

***

## Supported:

- Linux: All.
- Windows: 7/8/10.
- Termux (Android).

***

## What's new?:

- Fixed bugs.
- Improved security. 

#### Внимание:

smartpasslib is still under development, so I can't promise
backward compatibility with older versions! 

Each new version will likely change passwords when generated. This is due to the very specifics of generation,
with increasing or decreasing complexity, or fixing and adding new levels of security.
Therefore, until the package is stable, specify for your applications the exact version of the package, which
you used during development .

***

## Description:

___smartpasslib___ - A cross-platform package of modules for generating, 
secure storage and recovery of complex, 
cryptographic, smart passwords on the fly.

With this package, you can create complex cryptographic recoverable smart passwords.

***

## Help:

- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip3 install smartpasslib`

or:

- download source code
- unpack
- Go to the project folder
- `python3 -m venv venv`
- `source venv/bin/activate`
- `python3 setup.py install`

For run tests:

- `pip3 install pytest`
- `pytest -v`

For run tests coverage:

- `pip3 install pytest-cov`
- `pytest --cov --cov-report=html`

### Test coverage:

Coverage 100% !!!

***

![coverage img](https://github.com/smartlegionlab/smartpasslib/raw/master/data/images/smartpasslib.png)

***


## Use:

```python
from smartpasslib.generators import PassGen
from smartpasslib.manager import SmartPassMan, SmartPassword
from smartpasslib.generators import Tools
from smartpasslib.factories import GeneratorsFactory

# data to generate
login = 'login'
secret = 'secret'
length = 15

# Passwords generator
pass_gen = PassGen()

# Passwords will always be different
def_password = pass_gen.base.generate()
def_password2 = pass_gen.base.generate()
assert def_password != def_password2

# Passwords will always be the same when using the same passphrase:
norm_password = pass_gen.normal.generate(secret='secret', length=15)
norm_password2 = pass_gen.normal.generate(secret='secret', length=15)
assert norm_password == norm_password2

smart_password = pass_gen.smart.generate(login='login', secret='secret')
smart_password2 = pass_gen.smart.generate(login='login', secret='secret')

assert smart_password == smart_password2

tools = Tools()

key = tools.key_gen.make(login=login, secret=secret)

smart_pass = SmartPassword(login=login, key=key, length=length)
password_manager = SmartPassMan()
password_manager.add(smart_pass)

factory = GeneratorsFactory()
base_pass_gen = factory.get_base_pass_gen()
norm_pass_gen = factory.get_norm_pass_gen()
smart_pass_gen = factory.get_smart_pass_gen()
key_gen = factory.get_key_gen()
hash_gen = factory.get_hash_gen()
urandom_gen = factory.get_urandom_gen()

```

***

## Disclaimer of liability:

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

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2021, A.A Suvorov
    All rights reserved.
    --------------------------------------------------------
