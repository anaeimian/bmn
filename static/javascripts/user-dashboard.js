var ibmn = {};

ibmn.dashboard = {};

// ready event
ibmn.dashboard.ready = function () {

    var
        $checkBox = $('.ui.checkbox'),
        $sortTable = $('.sortable.table'),
        $dropDown = $('.ui.dropdown'),
        $browseItem = $('.browse.item'),
        $messageClose = $('.message .close')
        ;

    $checkBox
        .checkbox();

    $dropDown
        .dropdown();

    $browseItem
        .popup({
            on: 'click',
            inline: true,
            hoverable: true,
            position: 'bottom center',
            delay: {
                show: 300,
                hide: 80000,
            }
        });

    $messageClose
        .on('click', function () {
            $(this)
                .closest('.message')
                .transition('fade');
        });

    $sortTable
        .tablesort();

};

// attach ready event;
$(document).ready(ibmn.dashboard.ready);