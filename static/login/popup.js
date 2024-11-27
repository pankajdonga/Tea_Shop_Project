//

const loginBtn = document.getElementById("login-btn");
const loginpopupContainer = document.getElementById("login-popup-container");
const signupPopupContainer = document.getElementById("signup-popup-container");
const signupLink = document.getElementById("signup-link");

// Add an event listener to the button
loginBtn.addEventListener("click", () => {
  // Show the popup
  loginpopupContainer.style.display = "block";
});

// Add an event listener to the popup container
loginpopupContainer.addEventListener("click", (e) => {
  // If the user clicks outside the popup content, hide the popup
  if (e.target === loginpopupContainer) {
    loginpopupContainer.style.display = "none";
  }
});

// Add an event listener to the signup link
signupLink.addEventListener("click", (e) => {
  // Prevent the default link behavior
  e.preventDefault();

  // Hide the login popup
  loginpopupContainer.style.display = "none";

  // Show the signup popup
  signupPopupContainer.style.display = "block";
});

// Add an event listener to the popup container
signupPopupContainer.addEventListener("click", (e) => {
  // If the user clicks outside the popup content, hide the popup
  if (e.target === signupPopupContainer) {
    signupPopupContainer.style.display = "none";
  }
});
