var create_title = function
(title, author, cover, description, rating, 
genre1, genre2, genre3, review1, review2, review3
){

    var can_create = true

    $(".gen_warn").remove()
    $(".num_warn").remove()

    $(".label").each(function(){
        label_in = $.trim($(this).val())
        if ($(this).attr("id") == "rating"){
            if (label_in == "" || isNaN(label_in)){
                var num_warn = $("<div class=\"alert alert-warning num_warn\" role=\"alert\">" +
                    "Not a number!" +
                    "</div>")
                $("#rating_div").append(num_warn)
                can_create = false
            }
        } else if (label_in == ""){
            var gen_warn = $("<div class=\"gen_warn alert alert-warning\" role=\"alert\">" +
            "Write something!" +
            "</div>")

            div_name = "#" + $(this).attr("id") + "_div"
            $(div_name).append(gen_warn)
            can_create = false
        }
    })

    if (can_create){
        var data_to_save = {
            "title": title, "author": author, "cover": cover, 
            "description": description, "rating": rating, "genre1": genre1, 
            "genre2": genre2, "genre3": genre3, "review1": review1, 
            "review2": review2, "review3": review3
        }
    
        $.ajax({
            type: "POST",
            url: "create_title",
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data_to_save),
            success: function(result){
                var link_id = result["id_"]
                $("#transition_alert").addClass("alert")
                $("#transition_alert").addClass("alert-success")
                $("#transition_alert").attr("role", "alert")
                success = $("<div>Book successfully created. <a href='/view/" + link_id + "' class='alert-link'> View it here. </a></div>")
                $("#transition_alert").append(success)
            },
            error: function(request, status, error){
                $("#new_item").append("Oops! An Error Occurred :(")
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
    
        $(".label").val("")
        $("#title").focus()
    }
    
}

$(document).ready(function(){
    $("#create_btn").click(function(){
        create_title( 
            $("#title").val(), $("#author").val(), $("#cover").val(), 
            $("#description").val(), $("#rating").val(), 
            $("#genre1").val(), $("#genre2").val(), $("#genre3").val(), 
            $("#review1").val(), $("#review2").val(), $("#review3").val()
        )
    })
})