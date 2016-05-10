/**
 * Created by benyamin on 10/25/15.
 */
function bothHaveValue() {
    if ($("#id_field option:selected").text() === "---------") {
        return false;
    } else if ($("#id_facility option:selected").text() === "---------") {
        return false;
    }
    return true;
};

function addAssociationsDropdown(assos){
    //console.log(assos);
    //var select1 =  $('#first_choice');
    //for(var i = 0; i <= assos.length; i++) {
    //    var option = document.createElement('option');
    //    option.text = option.value = assos[i];
    //    select1.add(option, 0);
    //}
    //$("#associations-fields").show();
    //console.log("Toolbar was added.");
};

function getProperAssocations() {
    var element = document.createElement("div");

    element.setAttribute("class", "ui active small inline loader");

    $('#assoc-label').append(element);

    var csrftoken = getCookie('csrftoken');

    $.ajax({
        type: "POST",
        url: "/users/getassocs/",
        data: "field=" + $("#id_field option:selected").text() + "&facility=" + $("#id_facility option:selected").text(),
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function (response) {
            console.log(response);
            element.remove();
            //addAssociationsDropdown(response)
            var select1 =  document.getElementById("id_association1");
            for(i=select1.options.length-1;i>0;i--){
                select1.remove(i);
            }
            for(var i = 0; i < response.length; i++) {
                var opt = document.createElement("option");
                opt.value = response[i];
                opt.innerHTML = response[i];
                select1.appendChild(opt);
            }
            var select2 =  document.getElementById("id_association2");
            for(i=select2.options.length-1;i>0;i--){
                select2.remove(i);
            }
            for(var i = 0; i < response.length; i++) {
                var opt = document.createElement('option');
                opt.value = response[i];
                opt.innerHTML = response[i];
                select2.appendChild(opt);
            }
            var select3 =  document.getElementById("id_association3");
            for(i=select3.options.length-1;i>0;i--){
                select3.remove(i);
            }
            for(var i = 0; i < response.length; i++) {
                var opt = document.createElement('option');
                opt.value = response[i];
                opt.innerHTML = response[i];
                select3.appendChild(opt);
            }
            $("#associations-fields").show();
            console.log("Toolbar was added.");

        },
    });
};


$(document).ready(function () {

    $("#associations-fields").hide();

    $("#id_facility").change(function () {
        if (bothHaveValue()) {
            addAssociationsDropdown();
            getProperAssocations();
        }
    });

    $("#id_field").change(function () {
        if (bothHaveValue()) {
            addAssociationsDropdown();
            getProperAssocations();
        }
    });

});