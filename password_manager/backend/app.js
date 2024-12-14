import express from 'express';
import crypto from 'crypto';
import { json } from 'body-parser';
import mongoose from 'mongoose';
import dotenv from 'dotenv'

dotenv.config()

const app = express();
app.use(express.json());



app.listen(port, () => {
  console.log(`Server is running on port: ${port}`);
});
