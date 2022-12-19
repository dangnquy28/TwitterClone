/////////JS for POST 
////////////////////

$(function(){
    $('.js-menu-icon').click(function(){
        //$(this) :self element, name div.js-menu-icon
        //next() : Next to div.js-menu-icon, name div.menu
        
        $(this).next().toggle();
    })
})

//let icon_like= document.getElementById("like")
//icon_like= addEventListener('click', toggleLike)

/////function toggleLike() {
       //alert('hello!')//
///////
