# pypdf local hardened build

Base: installed pypdf 6.19.0. Local version: 6.19.0+local.sec1.

Changes:
- Replaced dynamic `locals()[visitor]` lookup with an explicit callback mapping.
- Changed `PdfWriter.encrypt()` default from RC4 to AES-256.
- Requires `cryptography>=46.0.3`.
- Image extra requires `Pillow>=12.2.0`; test extra requires `pytest>=9.0.3`.
- Legacy RC4/MD5 code is retained only for reading/decrypting older PDF formats and explicit compatibility requests. Removing it would break valid legacy PDFs; it is not used by the hardened default writer path.
- CI/release-only urllib findings from the upstream repository are absent because this distributable contains the runtime package only.

This is a local derivative, not an upstream py-pdf release. Rebase onto a newer upstream version before production adoption and run your organization's SCA/SAST tools on the produced artifact.
