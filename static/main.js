/**
 * Created by lewisgong on 14/05/2017.
 */
$("#modules").click(function () {
    $("#modules-msg").css("display", "");
    listModules();
    $(this).blur();
});


$("#puppet").click(function(){
    $("#modules-msg").css("display", "");
    $.ajax({
        url: "/puppet/refresh",
        success: function (result) {
            if (result == "OK"){
                listModules();
            }else {
                alert("//TODO")
            }
        }
    });
    $(this).blur();
});

function listModules() {
    $('#modules-tab').unbind('click');
    $('#modules-tab').find("tr:not(:first)").remove();
    $.ajax({
        url: "/puppet/list",
        success: function (result) {
            var modules = result.replace("[","").replace("]","").split(",");
            for(var i = 0; i < modules.length; i++){
                var row = "<tr><td>"+(i+1)+"</td><td class='module-sel'>"+modules[i]+"</td><td>" +
                    "<button type='button' class='btn btn-primary btn-md btn-modules' id="+modules[i]+">" +
                    "Compile this module</button></td></tr>";
                $("#modules-tab tr:last").after(row)
            }
            $("#modules-msg").css("display", "none");
            $("#modules-tab").css("display", "");
            $('#modules-tab').on('click', '.btn-modules', function () {
                var self = $(this).closest("tr");
                var col2_value = self.find('.module-sel').text();
                var module = col2_value.replace(/["']/g, "").replace(" ", "");
                $(this).blur();
                CompileModule(module);
            });
        }
    });
}

function CompileModule(module) {
    $.ajax({
        url: "/puppet/c?module="+module,
        success: function (result) {
            if(result!='Fail to compile.'){
                $('#output-msg').html("");
                msg = lineEscape(result);
                $('#output-msg').html(msg.join('<br>'));
                $('#compilationOutput').modal();
            }else {
                $('#compilationError').modal();
            }
        }
    });
}

function lineEscape(string) {
    var re=/\r\n|\n\r|\n|\r/g;
    return string.replace(re,"\n").split("\n");
}