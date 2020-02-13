$.get('https://swapi.co/api/films/?format=json', function (data) {
  data.results.forEach(element => {
    $('#list_movies').append('<li>' + element.title + '</li>');
  });
}
);
