/**
 * Created by benyamin on 10/5/15.
 */
$(document).ready(function(event){
    $('#hidden-input').change(function(){
        if($('#hidden-input').val().indexOf("متخصصان") > -1){
            $("#type-id").val("0");
        } else if($('#hidden-input').val().indexOf("نظام") > -1) {
            $("#type-id").val("1");
        }
    });
});
