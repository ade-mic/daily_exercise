import mongoose from 'mongoose';
import Secure from '../secure';


const { Schema, model } = mongoose;
const secure = new Secure();

const passwordSchema = new Schema(
  {
    username: {
      type: String,
      required: [true, 'Username is required'],
      trim: true,
    },
    password: {
      type: String,
      required: [true, 'Password is required'],
    },
    url: {
      type: String,
      required: [true, 'URL is required'],
      trim: true,
    },
  },
  {
    timestamps: true,
  }
);

// Middleware to encrypt the password before saving
passwordSchema.pre('save', function (next) {
  if (this.isModified('password')) {
    this.password = secure.encrypt(this.password)
  }
  next();
})

// Instance method to decrypt the password
passwordSchema.methods.decryptPassword = function() {
  return secure.decrypt(this.password);
}

const Password = model('Password', passwordSchema);

export default Password;