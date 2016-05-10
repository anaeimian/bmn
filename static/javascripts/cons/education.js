var setupCalendars = function (formNumber) {
    Calendar.setup({
        inputField: 'id_form-' + formNumber + '-begin_date',
        button: 'id_form-' + formNumber + '-period_begin_btn',
        ifFormat: '%Y/%m/%d',
        dateType: 'jalali'
    });
    Calendar.setup({
        inputField: 'id_form-' + formNumber + '-end_date',
        button: 'id_form-' + formNumber + '-period_end_btn',
        ifFormat: '%Y/%m/%d',
        dateType: 'jalali'
    });
}


var addCalendarForms = function () {
    var total = $('#id_form-TOTAL_FORMS').val();
    for (var i = 0; i < total; i++) {
        setupCalendars(i);
    }
}

$(document).ready(function () {
    $('#add_new_form').click(function (event) {
        console.log("This one was called.");
        cloneMore('#form > div:last', 'form');
        addCalendarForms();
    });
    addCalendarForms();
});