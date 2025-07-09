// script.js

document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const textarea = document.querySelector("textarea");
  const fileInput = document.querySelector("input[type='file']");
  const submitButton = document.querySelector("button[type='submit']");

  // Optional: Prevent empty form submission
  form.addEventListener("submit", function (e) {
    if (!fileInput.value && textarea.value.trim() === "") {
      e.preventDefault();
      alert("Please upload a screenshot or paste a message to analyze.");
    } else {
      submitButton.innerText = "Analyzing...";
      submitButton.disabled = true;
    }
  });

  // Optional: Reset button after submission
  window.addEventListener("pageshow", function () {
    submitButton.innerText = "Analyze";
    submitButton.disabled = false;
  });
});
