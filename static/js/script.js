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

  