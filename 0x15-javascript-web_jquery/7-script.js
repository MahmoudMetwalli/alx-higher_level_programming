const characterUri = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const $characterDiv = $('div#character');

$.ajax({
  url: movieUri,
  dataType: 'json'
}).done((data) => {
  $list_movies.text(data.name);
});
