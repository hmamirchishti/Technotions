/*$(document).ready(function () {
   $.ajax({
            type:'GET',
            url:'http://localhost:8000/blog/get_categories',
            success: function(data){
                var category = document.getElementById('categories');
              $(category).empty();
    for (var i = 0; i < data.length; i++) {
    $(category).append('<option id=' + data[i].pk + ' value=' + data[i].fields.name + '>' + data[i].fields.name + '</option>');
    }
            },
            error: function (textStatus, errorThrown) {
                alert(errorThrown);//doesnt goes here
            }  
        });
});*/