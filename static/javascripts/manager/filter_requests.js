/**
 * Created by benyamin on 4/28/16.
 */

$(document).ready(function(){
    Calendar.setup({
        inputField: 'start_date',
        button: 'start_date_btn',
        ifFormat: '%Y/%m/%d',
        dateType: 'jalali'
    });
    Calendar.setup({
        inputField: 'end_date',
        button: 'end_date_btn',
        ifFormat: '%Y/%m/%d',
        dateType: 'jalali'
    });
});