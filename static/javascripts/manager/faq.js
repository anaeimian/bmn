/**
 * Created by benyamin on 9/27/15.
 */
$(document).ready(function(){
    $('.ui.red.button').click(function(event){
        var user_choice = confirm("آیا می‌خواهید این سوال را حذف کنید؟");
        if(!user_choice){
            event.preventDefault();
            return false;
        }
    });
});