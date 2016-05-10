/**
 * Created by sara on 4/17/16.
 */
$(document).ready(function(){
    $("#form").submit(function(event){
        div = $("#dashboard > div > div.ui.segment > div.ui.grid > div > form > div.two.fields > div > div");
        if(!div.hasClass("checked")){
            document.getElementById("termsagree").style = "color: red;";
            event.preventDefault();
            return false;
        }
    });
})