var ibmn = {};

ibmn.login = {};

// ready event
ibmn.login.ready = function () {

    $('.ui.checkbox')
        .checkbox()
    ;

};

// attach ready event;
$(document).ready(ibmn.login.ready);