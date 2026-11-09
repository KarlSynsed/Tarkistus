from io import BytesIO
from pypdf import PdfReader, PdfWriter

def test_roundtrip_and_aes256_default():
    out=BytesIO(); w=PdfWriter(); w.add_blank_page(width=72,height=72); w.encrypt("secret"); w.write(out)
    raw=out.getvalue(); assert b"/AESV3" in raw
    r=PdfReader(BytesIO(raw)); assert r.decrypt("secret"); assert len(r.pages)==1

def test_plain_roundtrip():
    out=BytesIO(); w=PdfWriter(); w.add_blank_page(width=72,height=72); w.write(out)
    assert len(PdfReader(BytesIO(out.getvalue())).pages)==1
