# SEC-06 Public Key Infrastructure
A public key infrastructure (PKI) is a system for the creation, storage, and distribution of digital certificates which are used to verify that a particular public key belongs to a certain entity. The PKI creates digital certificates which map public keys to entities, securely stores these certificates in a central repository and revokes them if needed.
  
X.509 is the standard which defines the process in which a PKI should function. There are many ways of implementing a PKI, not all of them comply with the X.509 standard.  

An X.509 certificate binds an identity to a public key using a digital signature. A certificate contains an identity (a hostname, or an organization, or an individual) and a public key (RSA, DSA, ECDSA, ed25519, etc.), and is either signed by a certificate authority or is self-signed. When a certificate is signed by a trusted certificate authority, or validated by other means, someone holding that certificate can use the public key it contains to establish secure communications with another party, or validate documents digitally signed by the corresponding private key.  

In the X.509 system, there are two types of certificates. The first is a CA certificate. The second is an end-entity certificate. A CA certificate can issue other certificates. The top level, self-signed CA certificate is sometimes called the Root CA certificate. Other CA certificates are called intermediate CA or subordinate CA certificates. An end-entity certificate identifies the user, like a person, organization or business. An end-entity certificate cannot issue other certificates. An end-entity certificate is sometimes called a leaf certificate since no other certificates can be issued below it.  
  
An organization that wants a signed certificate requests one from a CA using a protocol like Certificate Signing Request (CSR), Simple Certificate Enrollment Protocol (SCEP) or Certificate Management Protocol (CMP). The organization first generates a key pair, keeping the private key secret and using it to sign the CSR. The CSR contains information identifying the applicant and the applicant's public key that is used to verify the signature of the CSR - and the Distinguished Name (DN) that is unique for the person, organization or business. The CSR may be accompanied by other credentials or proofs of identity required by the certificate authority.  
  
Browsers such as Internet Explorer, Firefox, Opera, Safari and Chrome come with a predetermined set of root certificates pre-installed, so SSL certificates from major certificate authorities will work instantly; in effect the browsers' developers determine which CAs are trusted third parties for the browsers' users. For example, Firefox provides a CSV and/or HTML file containing a list of Included CAs.


## Key terminology
- CA: Certificate Authority - Stores, issues and signs the digital certificates
- TTP: Trusted third part (another name for CA's)
- RA: Registration Authority - Verifies the identity of entities requesting their digital certificates to be stored at the CA
- CSR:  Certificate Signing Request - in PKI's a CSR is a message from an applicant to a registration authority to apply for a digital identity certificate.

## Exercise
### Sources
- https://en.wikipedia.org/wiki/Public_key_infrastructure
- https://en.wikipedia.org/wiki/X.509
- https://en.wikipedia.org/wiki/Certificate_signing_request

### Overcome challenges
[Give a short description of your challanges you encountered, and how you solved them.]

### Results
[Describe here the result of the exercise. An image can speak more than a thousand words, include one when this wisdom applies.]
