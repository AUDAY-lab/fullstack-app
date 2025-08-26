const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const PORT = 3000;
const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000';

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Home page with form
app.get('/', (req, res) => {
    res.render('index', { message: null, error: null });
});

// Handle form submission
app.post('/submit', async (req, res) => {
    try {
        const { name, email } = req.body;
        
        const response = await axios.post(`${BACKEND_URL}/submit`, {
            name: name,
            email: email
        });
        
        res.render('index', { 
            message: 'Form submitted successfully!', 
            error: null 
        });
    } catch (error) {
        console.error('Error:', error.message);
        res.render('index', { 
            message: null, 
            error: 'Failed to submit form. Please try again.' 
        });
    }
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Frontend running on port ${PORT}`);
});