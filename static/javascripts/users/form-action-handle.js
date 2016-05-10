$(document).ready(function () {
    $("#save").click(function () {
        $("#action-input").val("save")
        console.log("Set to save");
    });
    $("#preview").click(function () {
        $("#action-input").val("preview")
        console.log("Set to preview");
    });
});