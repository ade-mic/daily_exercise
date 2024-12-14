import Password from '../models/Password.js';

class PasswordController {
  // Save a new password
  static async savePassword(req, res) {
    try {
      const { username, password, url } = req.body;

      // Validate input
      if (!username || !password || !url) {
        return res.status(400).json({ message: 'All fields are required.' });
      }

      // Create and save the password entry
      const newPassword = new Password({ username, password, url });
      await newPassword.save();

      res.status(201).json({ message: 'Password saved successfully!' });
    } catch (error) {
      console.error('Error saving password:', error.message);
      res.status(500).json({ message: 'Server error while saving password.' });
    }
  }

  // Retrieve and decrypt a password by ID
  static async getPassword(req, res) {
    try {
      const { id } = req.params;

      // Find password by ID
      const passwordEntry = await Password.findById(id);
      if (!passwordEntry) {
        return res.status(404).json({ message: 'Password not found.' });
      }

      // Decrypt the password
      const decryptedPassword = passwordEntry.decryptPassword();

      res.status(200).json({
        username: passwordEntry.username,
        url: passwordEntry.url,
        password: decryptedPassword, // Decrypted password
      });
    } catch (error) {
      console.error('Error retrieving password:', error.message);
      res.status(500).json({ message: 'Server error while retrieving password.' });
    }
  }
}

export default PasswordController;
