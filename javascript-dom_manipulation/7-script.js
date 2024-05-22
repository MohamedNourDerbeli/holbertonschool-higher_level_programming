document.addEventListener('DOMContentLoaded', function () {
  fetchMoviesList();
});

function fetchMoviesList () {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
      return response.json();
    })
    .then(data => {
      const ul = document.getElementById('list_movies');
      data.results.forEach(movie => {
        const li = document.createElement('li');
        li.textContent = movie.title;
        ul.appendChild(li);
      });
    });
}
