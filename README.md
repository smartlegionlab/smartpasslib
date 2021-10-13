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

## Requirements:

- [Python](https://python.org) 3.6+

***

## What's new?:

### ___smartpasslib v0.1.0___

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
from smartpasslib.generators import PasswordsGenerator

# data to generate
login = 'login'
secret = 'secret'
length = 15

# Passwords generator
pass_gen = PasswordsGenerator()

# Passwords will always be different
def_password = pass_gen.get_def_pass()
def_password2 = pass_gen.get_def_pass()
assert def_password != def_password2

# Passwords will always be the same when using the same passphrase:
norm_password = pass_gen.get_norm_pass(secret='secret', length=15)
norm_password2 = pass_gen.get_norm_pass(secret='secret', length=15)
smart_password = pass_gen.get_smart_pass(login='login', secret='secret')
smart_password2 = pass_gen.get_smart_pass(login='login', secret='secret')
assert norm_password == norm_password2
assert smart_password == smart_password2

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
