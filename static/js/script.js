

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


function fetchpost() {
  // Get Form Data
  const myForm = document.getElementById('likedata');

  myForm.addEventListener('submit', function (e) {
    e.preventDefault();

    let liked = document.getElementsByClassName('fas');
    let notLiked = document.getElementsByClassName('far');



    const formData = new FormData(this);
    const btnLike = document.getElementsByClassName('btn-like');
    console.log('I saw')

    formData.append('liked', liked);
    formData.append('notLiked', btnlike);

    const request = new Request('{% url "post_like" post.slug %}', {
      method: 'POST',
      body: formData
    });

    request.formData().then(function(data) {
      console.log('end of fetch')
    })
  })}