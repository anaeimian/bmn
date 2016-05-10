/**
 * Created by benyamin on 4/15/16.
 */
var cloneMore = function (selector, type) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + type + '-TOTAL_FORMS').val();

    newElement.find(':input').not(":input.cal.btn").each(function () {
        var name = $(this).attr('name').replace('-' + (total - 1) + '-', '-' + total + '-');
        var id = 'id_' + name;
        console.log("var name: " + name + " id: " + id);
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find(':input.cal.btn').each(function () {
        var name = $(this).attr('name').replace('-' + (total - 1) + '-', '-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    total++;
    $("#num_of_forms_hidden").val(total);
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
};