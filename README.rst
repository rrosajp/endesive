.. image:: https://img.shields.io/pypi/v/endesive.svg
        :target: https://pypi.python.org/pypi/endesive

Description
===========

Python library for digital signing and verification of digital signatures in mail,
PDF and XML documents.

The ASN.1 implementation depends on `asn1crypto`_.
Cryptographic routines depends on `cryptography`_ library.

For certificate verification `cryptography`_ library is used.

This library implements S/MIME handler which can encrypt and decrypt S/MIME messages
using a public RSA key, in AES-128/192/256 CBC/OFB modes.
It can also sign and verify S/MIME messages.

This library implements CAdES-B handler for signing and verifying PDF documents in
Adobe.PPKLite/adbe.pkcs7.detached form.
It can sign documents during generation using a modified version of `pyfpdf`_ which is
included in this library. It can also sign documents generated by external programms.

This library implements XADES BES/T  with enveloped and enveloping format for creating
signed xml files.

This library implements CMS handler for signing and verifying plain text files with
detached signature files.


License
=======

This software is licensed under the MIT License. See the LICENSE file in
the top distribution directory for the full license text.


## Requirements

* Python 3.*
* `cryptography`_
* `asn1crypto`_
* `lxml`_
* `pykcs11`_
* `Pillow`_


Examples
========

cert-make.py
    Create required certificates (password is 1234)
cert-make-hsm.py
    Create required certificates for SoftHSM (password is secret1)

pdf-make.py
    Create simple two paged PDF document which is used in pdf-sign-cms.py.
pdf-sign-cms.py
    Create signature in externally created PDF.
pdf-sign-cms-hsm.py
    Create signature in externally created PDF but signed with key stored in SoftHSM.
pdf-sign-fpdf.py
    Create signature while creating PDF.
pdf-verify.py
    Verify prevously generated files (cms/pdf).

plain-make.py
    Create simple UTF-8 text file.
plain-openssl.sh
    Sign, encrypt and decrypt text file with help of openssl executable.
plain-sign-attr.py
    Sign text file with 'extended' CMS attributes.
plain-sign-noattr.py
    Sign text file without 'extended' CMS attributes.
plain-verify.py
    Verify all generated signatures for text file.

smime-make.py
    Create simple UTF-8 text file for use in following examples.
smime-openssl.sh
    Create signed S/MIME file, encrypted S/MIME file and decrypt generated S/MIME file
    with help of openssl executable.
smime-encrypt.py
    Create encrypted S/MIME file.
smime-decrypt.py
    Decrypt encrypted S/MIME file.
smime-sign-attr.py
    Create signed S/MIME file with 'extended' CMS attributes.
smime-sign-noattr.py
    Create signed S/MIME file without 'extended' CMS attributes.
smime-verify.py
    Verify all generated S/MIME files.

xml-make.py
    Create simple xml file for use in following examples.
xml-hsm-certum-enveloped.py
    XADES enveloped mode with real certificate (BES/T).
xml-hsm-certum-enveloping.py
    XADES enveloping mode with real certificate (BES/T).
xml-hsm-softhsm2-enveloped.py
    XADES enveloped mode with SoftHSM certificate (BES).
xml-hsm-softhsm2-enveloping.py
    XADES enveloping mode with SoftHSM certificate (BES).

Tools
=====

Online pdf validator `pdfvalidator`_ or `verapdf`_.
Offline Apache `pdfbox`_ java based validator.

Validate electronic signatures: `ec_europa`_ or `pkitools_net`_.

.. _cryptography: https://github.com/pyca/cryptography
.. _asn1crypto: https://github.com/wbond/asn1crypto
.. _pyfpdf: https://github.com/reingart/pyfpdf
.. _lxml: https://pypi.org/project/lxml/
.. _pykcs11: https://pypi.org/project/pykcs11/
.. _Pillow: https://pypi.org/project/Pillow/
.. _pdfvalidator: https://www.pdf-online.com/osa/validate.aspx
.. _verapdf: https://demo.verapdf.org/
.. _pdfbox: https://pdfbox.apache.org/
.. _ec_europa: https://ec.europa.eu/cefdigital/DSS/webapp-demo/validation
.. _pkitools_net: https://pkitools.net/pages/validator/pdf.html
