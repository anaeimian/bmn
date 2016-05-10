var ibmn = {};

ibmn.signup = {};

// ready event
ibmn.signup.ready = function () {

    $('.ui.checkbox').checkbox();
    $('.ui.dropdown')
        .dropdown({
            message: {
                noResults: '\u06CC\u0627\u0641\u062A\u0020\u0646\u0634\u062F!'
            }
        });
};
// attach ready event;
$(document).ready(ibmn.signup.ready);
Calendar.setup({
    inputField: 'birth_date_input',
    button: 'birth_date_btn',
    ifFormat: '%Y/%m/%d',
    dateType: 'jalali'
});