

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

// function getCookie(name) {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== '') {
//       const cookies = document.cookie.split(';');
//       for (let i = 0; i < cookies.length; i++) {
//           const cookie = cookies[i].trim();
//           // Does this cookie string begin with the name we want?
//           if (cookie.substring(0, name.length + 1) === (name + '=')) {
//               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//               break;
//           }
//       }
//   }
//   return cookieValue;
// }

// const likeButton = document.getElementById('btnLike');
// if (likeButton) {
//   likeButton.addEventListener('click', () => {
//     const csrftoken = getCookie('csrftoken');
//     const request = new Request(
//       likeButton.dataset.url,
//       {
//           method: 'POST',
//           headers: {'X-CSRFToken': csrftoken},
//           mode: 'same-origin', // Do not send CSRF token to another domain.
//           body: JSON.stringify({"slug": likeButton.value})
//       }
//     );
//     fetch(request).then((response) => {
//       response.json().then((data) => {
//         console.log(data);
//         if (data.like) {
//           likeButton.firstChild.classList.add('fas');
//           likeButton.firstChild.classList.remove('far');
//         } else {
//           likeButton.firstChild.classList.add('far');
//           likeButton.firstChild.classList.remove('fas');
//         }
//       });
//     });
//   });
// }

// const likeButton = document.getElementById('btnLike');
// if (likeButton) {
//   likeButton.addEventListener('click', () => {
//     const request = new Request(
//       likeButton.dataset.url,
//       {
//         method: 'POST',
//         body: JSON.stringify({'slug': likeButton.value})
//       }
//     );
//     fetch(request).then((response) => {
//       console.log(data);
//       if (data.like) {
//         likeButton.firstChild.classList.add('fas');
//         likeButton.firstChild.classList.remove('far');
//       } else {
//         likeButton.firstChild.classList.add('far');
//         likeButton.firstChild.classList.remove('fas');
//       }
//     });
//   });
// }
