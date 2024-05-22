document.getElementById('toggle_header').addEventListener('click', myFunction);

function myFunction () {
  if (document.querySelector('header').className === 'red') { document.querySelector('header').className = 'green'; } else {
    document.querySelector('header').className = 'red';
  }
}
