/**
 * Created by lewisgong on 14/05/2017.
 */

$("#puppet").click(function(){
    $("#modules-msg").css("display", "");
    $.ajax({
        url: "/puppet/refresh",
        success: function (result) {
            if (result == "OK"){
                $.ajax({
                   url: "/puppet/list",
                    success: function (result) {
                        var modules = result.replace("[","").replace("]","").split(",");
                        for(var i = 0; i < modules.length; i++){
                            var row = "<tr><td>"+(i+1)+"</td><td>"+modules[i]+"</td></tr>"
                            $("#modules-tab tr:last").after(row)
                        }
                        $("#modules-msg").css("display", "none");
                        $("#modules-tab").css("display", "");
                    }
                });
            }else {
                alert("TODO")
            }
        }
    });
});
