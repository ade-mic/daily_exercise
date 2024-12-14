# Secure Password Manager

A **Secure Password Manager** designed to safely store and retrieve user credentials. This project ensures that all sensitive information is encrypted before being stored in the database, prioritizing security and ease of use.

## Features

- **Encryption & Decryption**: Utilizes AES-256-CTR encryption for secure password storage and retrieval.
- **Middleware Integration**: Automatically encrypts passwords before saving them to the database.
- **API Endpoints**: Provides RESTful API routes for saving and retrieving passwords securely.
- **Scalable Design**: Encapsulated logic in modular classes for easier maintenance and scalability.
- **Error Handling**: Handles server-side errors gracefully to ensure a robust application.

## Tech Stack

- **Backend**: Node.js, Express
- **Database**: MongoDB (Mongoose ORM)
- **Encryption**: Crypto module (AES-256-CTR)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/password-manager.git
   cd password-manager
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up the `.env` file with your environment variables:
   ```env
   ENCRYPTION_KEY=your-32-character-encryption-key
   MONGO_URI=your-mongodb-connection-string
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

## Usage

### API Endpoints

#### 1. Save a Password
**POST** `/passwords`

- **Body Parameters:**
  ```json
  {
    "username": "example_user",
    "password": "example_password",
    "url": "https://example.com"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Password saved successfully!"
  }
  ```

#### 2. Retrieve a Password
**GET** `/passwords/:id`

- **Response:**
  ```json
  {
    "username": "example_user",
    "url": "https://example.com",
    "password": "example_password"
  }
  ```

## Folder Structure
```
password-manager/
├── controllers/
│   └── PasswordController.js      # Controller for password-related operations
├── middlewares/
│   └── encryptMiddleware.js       # Middleware for password encryption
├── models/
│   └── Password.js                # Mongoose schema for passwords
├── utils/
│   └── Secure.js                  # Encryption/Decryption utility class
├── routes/
│   └── passwordRoutes.js          # API routes
├── .env                           # Environment variables
├── server.js                      # Entry point for the app
└── README.md                      # Project documentation
```

## Future Enhancements

- Implement user authentication and authorization.
- Add support for multiple encryption algorithms.
- Create a front-end interface for user interaction.
- Add automated tests for controllers and utilities.

## Contributing

1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to reach out if you have suggestions, feedback, or want to collaborate on this project! 🚀
