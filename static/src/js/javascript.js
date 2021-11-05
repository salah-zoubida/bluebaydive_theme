
// function openPage(pageName,elmnt,) {
//   var i, tabcontent, tablinks;
//   tabcontent = document.getElementsByClassName("tabcontent");
//   for (i = 0; i < tabcontent.length; i++) {
//     console.log('----------')
//     console.log(tabcontent.length)
//     tabcontent[i].style.display = "none";

//   }
//   tablinks = document.getElementsByClassName("tablink");
//   for (i = 0; i < tablinks.length; i++) {
//     tablinks[i].classList.remove("active");
//   }
//   document.getElementById(pageName).style.display = "block";
//   elmnt.classList.add("active");
//   // elmnt.style.backgroundColor = color;
// }

// // Get the element with id="defaultOpen" and click on it
// document.getElementById("defaultOpen").click();

$('#toggle > li').click(function() {
    var ix = $(this).index();
    console.log('----------')
    console.log(ix)
    $('#itinirary_tab').toggle( ix === 0 );
    $('#iframe_tab').toggle( ix === 1 );
    if (ix === 0){
      document.getElementById("itinerary").add("active");
      document.getElementById("reviews").remove("active");
      }
    if (ix === 1){
      document.getElementById("reviews").add("active");
      document.getElementById("itinerary").remove("active");
    }
});
