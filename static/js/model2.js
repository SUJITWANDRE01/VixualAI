document.getElementById('hamburger').addEventListener('click', function() {
    document.querySelector('.nav__links').classList.toggle('show');
  });

  // Get all navigation links
const navLinks = document.querySelectorAll('.nav__links li a');

  // Add a click event to each link
navLinks.forEach(link => {
    link.addEventListener('click', function() {
      document.querySelector('.nav__links').classList.remove('show');
    });
  });



document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('qaForm').addEventListener('submit', function (event) {
        event.preventDefault();

        // Serialize form data
        var formData = new FormData(this);
        var data = new URLSearchParams();
        formData.forEach(function(value, key) {
            data.append(key, value);
        });

        // Make the AJAX request
        fetch('/get_answer', {
            method: 'POST',
            body: data
        })
        .then(response => response.text())
        .then(responseText => {
            document.getElementById('answer').textContent = responseText;
        })
        .catch(error => console.error('Error:', error));
    });
});
