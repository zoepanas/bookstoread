
var edit_review = function(ID, review){
    var data_to_save = {"ID": ID, "review": review}

    $.ajax({
        type: "POST",
        url: "/edit_review",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            var review_ = result["review"]
            $("#current_reviews").append(review_ + "<br><br>")
            $("#new_review").val("")
            $("#add_review").hide()
            $("#add_review_btn").show()
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

}

var edit_rating = function(ID, rating){
    var data_to_save = {"ID": ID, "rating": rating}

    $.ajax({
        type: "POST",
        url: "/edit_rating",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            var rating_ = result["rating"]
            $("#current_rating").empty()
            $("#current_rating").append(rating_)
            $("#edit_rating").hide()
            $("#current_rating").show()
            $("#edit_rating_btn").show()
            $("#new_rating").val($("#current_rating").html())
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

}

var delete_genre = function(book_id, g){
    g_id = $(g).attr("id")
    genre_id_vals = g_id.split(".")
    genre_id = genre_id_vals[0]
    var data_to_save = {"book_id": book_id, "genre_id": genre_id}         
    $.ajax({
        type: "POST",
        url: "/delete_genre",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            var all_genres = result["genres"]
            genres = all_genres

            $(".showing_genres").each(function(index){
                var div_id = $(this).attr("id")
                var div_id_vals = div_id.split(".")
                show_div_id = div_id_vals[0]
                if (show_div_id == genre_id){
                    $(this).hide()
                }
            })
            $(".undo_delete").each(function(index){
                var btn_id = $(this).attr("id")
                var btn_id_vals = btn_id.split(".")
                undo_btn_id = btn_id_vals[0]
                if(undo_btn_id == genre_id){
                    $(this).show()
                }
            })

        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var undo_delete_genre = function(book_id, g){
    g_id = $(g).attr("id")
    genre_id_vals = g_id.split(".")
    genre_id = genre_id_vals[0]
    var data_to_save = {"book_id": book_id, "genre_id": genre_id}         
    $.ajax({
        type: "POST",
        url: "/undo_delete_genre",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            var all_genres = result["genres"]
            genres = all_genres

            $(".showing_genres").each(function(index){
                var div_id = $(this).attr("id")
                var div_id_vals = div_id.split(".")
                show_div_id = div_id_vals[0]
                if (show_div_id == genre_id){
                    $(this).show()
                }
            })
            $(".undo_delete").each(function(index){
                var btn_id = $(this).attr("id")
                var btn_id_vals = btn_id.split(".")
                undo_btn_id = btn_id_vals[0]
                if(undo_btn_id == genre_id){
                    $(this).hide()
                }
            })

        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

$(document).ready(function(){
    $("#add_review").hide()
    $("#edit_rating").hide()
    $(".undo_delete").hide()
    
    $("#new_rating").val($("#current_rating").html())
    $("#add_review_btn").click(function(){
        $("#add_review").show()
        $("#add_review_btn").hide()
    })
    $("#edit_rating_btn").click(function(){
        $("#edit_rating").show()
        $("#edit_rating_btn").hide()
        $("#current_rating").hide()
    })
    $("#review_submit_btn").click(function(){
        edit_review(iden, $("#new_review").val())
    })
    $("#review_discard_btn").click(function(){
        $("#add_review_btn").show()
        $("#new_review").val("")
        $("#add_review").hide()
    })
    $("#rating_submit_btn").click(function(){        
        edit_rating(iden, $("#new_rating").val())
    })
    $("#rating_discard_btn").click(function(){
        $("#edit_rating").hide()
        $("#current_rating").show()
        $("#edit_rating_btn").show()
        $("#new_rating").val($("#current_rating").html())
    })
    $(".del_btn").click(function(){
        delete_genre(iden, $(this))
    })
    $(".undo_delete").click(function(){
        undo_delete_genre(iden, $(this))
    })
})