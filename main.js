document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("mainHeader").onclick = function() {
    this.style.color = 'orange'
  }
})

$( document ).ready(function() {
  $( "#fade" ).click(function() {
    $( "#fade" ).fadeOut( "slow", function() {
    });
  });
});

$( document ).ready(function() {
  $( "#badlink" ).click(function() {
    $( "#badlink" ).fadeOut( "slow", function() {
    });
  });


//https://hoboson02.github.io/Earlr-osu-github.io/. 
//https://stackoverflow.com/questions/31368328/how-to-add-functionality-a-bootstrap-search-bar
//https://support.google.com/customsearch/answer/4513903?hl=en 