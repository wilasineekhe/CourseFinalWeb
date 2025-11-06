let slideIndex = 0;
const slides = document.getElementsByClassName("slide");
showSlides(slideIndex);

// Function to change slide
function changeSlide(n) {
    showSlides(slideIndex += n);
}

// Function to show slides
function showSlides(n) {
    if (n >= slides.length) { 
        slideIndex = 0; // Loop back to the first slide
    }
    if (n < 0) { 
        slideIndex = slides.length - 1; // Go to the last slide
    }
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; // Hide all slides
    }
    slides[slideIndex].style.display = "block"; // Show the current slide
}

// Automatic slideshow
setInterval(() => {
    changeSlide(1); // Move to the next slide every 3 seconds
}, 3000);

// Open the modal
function openModal() {
    document.getElementById('authModal').style.display = 'block';
}

// Close the modal
function closeModal() {
    document.getElementById('authModal').style.display = 'none';
}

// Toggle between login and registration forms
function toggleForms(formId) {
    document.getElementById('loginForm').style.display = formId === 'loginForm' ? 'block' : 'none';
    document.getElementById('registerForm').style.display = formId === 'registerForm' ? 'block' : 'none';
}

// Placeholder function for login logic
function login() {
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;
    alert(`Logging in with username: ${username} and password: ${password}`);
    // Implement your actual login logic here
}

// Placeholder function for registration logic
function register() {
    const username = document.getElementById('register-username').value;
    const email = document.getElementById('register-email').value;
    const password = document.getElementById('register-password').value;
    const confirmPassword = document.getElementById('register-confirm-password').value;
    alert(`Registering with username: ${username}, email: ${email}`);
    // Implement your actual registration logic here
}