import crypto from 'crypto';

class Secure {
  constructor() {
    this.algorithm = 'aes-256-ctr';
    this.encryptionKey = process.env.ENCRYPTION_KEY;

    if (!this.encryptionKey || this.encryptionKey.length !== 32) {
      throw new Error('Encryption key must be a 32-byte string. Set it in process.env.ENCRYPTION_KEY');
    }
  }

  encrypt(text) {
    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv(
      this.algorithm,
      Buffer.from(this.encryptionKey),
      iv
    );
    const encrypted = Buffer.concat([cipher.update(text), cipher.final()]);
    return `${iv.toString('hex')}:${encrypted.toString('hex')}`;
  }

  decrypt(text) {
    const [ivHex, encryptedHex] = text.split(':');
    const iv = Buffer.from(ivHex, 'hex');
    const encryptedText = Buffer.from(encryptedHex, 'hex');
    const decipher = crypto.createDecipheriv(
      this.algorithm,
      Buffer.from(this.encryptionKey),
      iv
    );
    const decrypted = Buffer.concat([
      decipher.update(encryptedText),
      decipher.final(),
    ]);
    return decrypted.toString();
  }
}

export default Secure;
