/*var display_books_list = function(books){
    $("#log").empty() // empty old data

    if (books.length == 0){
        var row = $("<div class='row mb-2'>")
        $(row).append("No results found :(")
        $("#log").append(row)
    } else {
        $.each(books, function(i, book){
            var col = $("<div class='col-md-3'>")

            var card = $("<div class='card mb-3'>")
            var link = $("<a href='/view/" + book["id"]+ "'>")
            var card_cover = $("<img class='card-img-top'>")
            card_cover.attr({
                
                "src": book["cover"],
                "alt": book["title"] + " cover image"
            })

            $(link).append(card_cover)
            $(card).append(link)

            var card_body = $("<div class='card-body'>")
            var card_title = $("<h5 class='card-title'>" + book["title"] + "</h5>")
            var card_author = $("<span class='card=text'>" + book["author"] + "</span>")
            $(card_body).append(card_title)
            $(card_body).append(card_author)

            $(card).append(card_body)

            $(col).append(card)

            $("#log").prepend(col)
            console.log(card)
        })
    }
}*/

var display_home = function(books){
    $("#log").empty() // empty old data    

    $.each(books, function(i, book){
        if(i >= books.length - 10){

            var col = $("<div class='col-md-3'>")

            var card = $("<div class='card mb-3'>")
            var link = $("<a href='/view/" + book["id"]+ "'>")
            var card_cover = $("<img class='card-img-top'>")
            card_cover.attr({
                
                "src": book["cover"],
                "alt": book["title"] + " cover image"
            })

            $(link).append(card_cover)
            $(card).append(link)

            var card_body = $("<div class='card-body'>")
            var card_title = $("<h5 class='card-title'>" + book["title"] + "</h5>")
            var card_author = $("<span class='card=text'>" + book["author"] + "</span>")
            $(card_body).append(card_title)
            $(card_body).append(card_author)

            $(card).append(card_body)

            $(col).append(card)

            $("#log").prepend(col)
            console.log("home")

        }
    })
    
}

var delete_book = function(id, searched_book){
    var data_to_save = {"id": id}         
    $.ajax({
        type: "POST",
        url: "delete_book",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            var all_books = result["books"]
            books = all_books
            search_title(searched_book)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var search_title = function(title){
    if(title == null){
        title = ""
    }
    window.location.href = '/search?q=' + title
    console.log("searching!!!")
    
}

$(document).ready(function(){
    display_home(books)
    $("#search_btn").click(function(){
        search_title($("#searchbar").val())
    })
    $("#searchbar").keyup(function(event){
        var code = event.keyCode;
        if (code == 13){
            search_title($("#searchbar").val())
        }
    })
})