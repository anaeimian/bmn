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
    inputField: 'in_country_period_end',
    button: 'period_end_btn',
    ifFormat: '%Y/%m/%d',
    dateType: 'jalali'
});
$(document).ready(ibmn.signup.ready);
Calendar.setup({
    inputField: 'in_country_period_start',
    button: 'period_start_btn',
    ifFormat: '%Y/%m/%d',
    dateType: 'jalali'
});