

window.onscroll = function() {myFunction()};

// Get the navbar
var navbar = document.getElementById("bottom-nav");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}


const myForm = document.getElementById('likedata');
myForm.addEventListener('submit', function (e) {
  e.preventDefault()

  const formData = new FormData;

  fetch("$('#url).attr('data-url)", {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    console.error('Error:', error)
  });

});