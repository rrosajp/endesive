# *-* coding: utf-8 *-*
import hashlib
from OpenSSL import crypto
from asn1crypto import x509, core, pem, cms
from oscrypto import asymmetric

class VerifyData(object):

    def __init__(self,):
        # Create and fill a X509Sore with trusted certs
        trusted_cert_pems = (open('demo2_ca.crt.pem', 'rt').read(),)
        self.store = crypto.X509Store()
        for trusted_cert_pem in trusted_cert_pems:
            trusted_cert = crypto.load_certificate(crypto.FILETYPE_PEM, trusted_cert_pem)
            self.store.add_cert(trusted_cert)

    def add_cert(self, trusted_certs):
        for trusted_cert in trusted_certs:
            self.store.add_cert(trusted_cert)

    def verify_cert(self, cert_pem):
        certificate = crypto.load_certificate(crypto.FILETYPE_PEM, cert_pem)
        # Create a X590StoreContext with the cert and trusted certs
        # and verify the the chain of trust
        store_ctx = crypto.X509StoreContext(self.store, certificate)
        # Returns None if certificate can be validated
        try:
            result = store_ctx.verify_certificate()
        except:
            result = False
        return result is None

    def _load_cert(self, relative_path):
        with open(relative_path, 'rb') as f:
            cert_bytes = f.read()
            if pem.detect(cert_bytes):
                _, _, cert_bytes = pem.unarmor(cert_bytes)
            return x509.Certificate.load(cert_bytes)

    def verify(self, datau, datas):
        signed_data = cms.ContentInfo.load(datas)['content']
        #signed_data.debug()

        signature = signed_data['signer_infos'][0].native['signature']
        algo = signed_data['digest_algorithms'][0]['algorithm'].native
        attrs = signed_data['signer_infos'][0]['signed_attrs']
        mdData = getattr(hashlib, algo)(datau).digest()
        if attrs is not None and not isinstance(attrs, core.Void):
            mdSigned = None
            for attr in attrs:
                if attr['type'].native == 'message_digest':
                    mdSigned = attr['values'].native[0]
            signedData = attrs.dump()
            signedData = b'\x31'+signedData[1:]
        else:
            mdSigned = mdData
            signedData = datau
        hashok = mdData == mdSigned
        serial = signed_data['signer_infos'][0]['sid'].native['serial_number']
        public_key = None
        for cert in signed_data['certificates']:
            if serial == cert.native['tbs_certificate']['serial_number']:
                cert = cert.dump()
                cert = pem.armor(u'CERTIFICATE', cert)
                public_key = asymmetric.load_public_key(cert)
                break
        try:
            asymmetric.rsa_pkcs1v15_verify(public_key, signature, signedData, algo)
            signatureok = True
        except:
            signatureok = False

        # TODO verify certificates
        certok = True
        for cert in signed_data['certificates']:
            scert = pem.armor(u'CERTIFICATE', cert.dump()).decode()
            if not self.verify_cert(scert):
                print('*'*10, 'failed certificate verification')
                print('cert.issuer:', cert.native['tbs_certificate']['issuer'])
                print('cert.subject:', cert.native['tbs_certificate']['subject'])
                certok = False
        return (hashok, signatureok, certok)

def verify(datau, datas):
    cls = VerifyData()
    return cls.verify(datau, datas)