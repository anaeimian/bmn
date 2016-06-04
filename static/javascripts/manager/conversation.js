/**
 * Created by Arman on 2016-06-03.
 */

var link = document.getElementById("message-title");
var clicked = 1;
link.onclick = function () {
    var container = document.getElementById("container");
    var truncatedText = document.getElementById("truncated");
    var fullText = document.getElementById("fulltext");
    if(clicked){
        truncatedText.style.visibility = "hidden";
        fullText.style.visibility = "visible";
        // container.style.backgroundColor = "white";
        clicked=0;
    }else{
        truncatedText.style.visibility = "visible";
        fullText.style.visibility = "hidden";
        // container.style.backgroundColor = "#dddddd";
        clicked = 1;
    }
}