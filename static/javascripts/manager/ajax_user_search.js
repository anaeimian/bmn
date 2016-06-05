/**
 * Created by Arman on 2016-05-30.
 */



function getApplications() {
    var application = document.getElementById("applications");
    var length = application.options.length;
    for (var i = 0; i < length; i++) {
        application.remove(0);
    }
    $.ajax({
        url: "getApplications/", // the endpoint
        type: "GET", // http method
        data: {the_post: $('#receiver').val()}, // data sent with the post request

        // handle a successful response
        success: function (json) {
            $.each(json, function (id, value) {
                $('#applications').append($('<option>').text(value.value).attr('value', value.value));
                console.log(value)
            });
        }

        //// handle a non-successful response
        //error : function(xhr,errmsg,err) {
        //    $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
        //        " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        //    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        //}
    });
}