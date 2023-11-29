function showForm() {
  document.getElementById('formDiv').style.display = 'block';
  document.getElementById('jsonDiv').style.display = 'none';
}
function showJson() {
  document.getElementById('formDiv').style.display = 'none';
  document.getElementById('jsonDiv').style.display = 'block';
}
function showResult() {
  document.getElementById('formDiv').style.display = 'none';
  document.getElementById('jsonDiv').style.display = 'none';
}

function validateForm() {
  let danceability = document.getElementById('danceability').value;
  let energy = document.getElementById('energy').value;
  let loudness = document.getElementById('loudness').value;
  let speechiness = document.getElementById('speechiness').value;
  let acousticness = document.getElementById('acousticness').value;
  let instrumentalness = document.getElementById('instrumentalness').value;
  let liveness = document.getElementById('liveness').value;
  let valence = document.getElementById('valence').value;

  if (danceability < 0 || danceability > 1) {
    alert('Danceability must be between 0 and 1');
    return false;
  }
}