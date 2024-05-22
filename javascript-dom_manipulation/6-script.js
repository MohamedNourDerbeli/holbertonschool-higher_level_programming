const fetchCharacter = () => {
  return new Promise(resolve => {
    fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
      .then(response => response.json())
      .then(data => {
        document.getElementById('character').innerHTML = data.name;
        resolve(data);
      });
  });
};

fetchCharacter();
