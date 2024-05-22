document.getElementById('add_item').addEventListener('click', myFunction);

function myFunction () {
  const ul = document.getElementsByTagName('ul')[0];
  const li = document.createElement('li');
  li.appendChild(document.createTextNode('Item'));
  ul.appendChild(li);
}
