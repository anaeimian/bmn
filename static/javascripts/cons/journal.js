/**
 * Created by benyamin on 4/15/16.
 */
$(document).ready(function () {
    $('#add_new_form').click(function (event) {
        console.log("This one was called.");
        cloneMore('#form > div:last', 'form');
    });
});