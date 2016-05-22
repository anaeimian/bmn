/**
 * Created by Arman on 5/18/2016.
 */


window.onload = function(){
    var url = window.location.href;
    var pageNumber = url.charAt(url.length-2);
    var btn = document.getElementById("btn"+pageNumber);
    btn.setAttribute("class","active item");
}

function changePage(i,appsPagesNumber) {
    window.location.href='/association/requests/'+ i;

    //for (var i = 0; i < temp.length; i++)
    //    temp[i].value = '1'
}

function decreasePage() {
    var url = window.location.href;
    var pageNumber = url.charAt(url.length-2);
    if( pageNumber != 1 ){
        window.location.href = '/association/requests/'+ (pageNumber-1);
    }
    //for (var i = 0; i < temp.length; i++)
    //    temp[i].value = '1'
}

function increasePage(appsPagesNumber) {

    var url = window.location.href;
    var pageNumber = url.charAt(url.length-2);
     //window.location.href = '/association/requests/'+ (pageNumber-(-1));
    if( pageNumber != appsPagesNumber ){
        window.location.href = '/association/requests/'+ (pageNumber-(-1));
    }

    //for (var i = 0; i < temp.length; i++)
    //    temp[i].value = '1'
}