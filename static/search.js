var search_title = function(title){
    if(title == null){
        title = ""
    }
    window.location.href = '/search?q=' + title
    console.log("searching!!!")
    
}

$(document).ready(function(){
    //display_books_list(books, title)
    $("#num_results").text(books.length)
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