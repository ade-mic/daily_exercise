import express from 'express';
import PasswordController from './controllers/PasswordController.js';

const router = express.Router();

// Routes for password operations
router.post('/passwords', PasswordController.savePassword);
router.get('/passwords/:id', PasswordController.getPassword);

export default router;
