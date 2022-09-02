$(document).ready(function(){
  var loader = $("div.loader");
  var list = $("div.list");
    function fn_loading() {
      loader.css("display","block");
      loader.css("z-index","3");
      list.css("display","none");
    };
    function fn_hiding() {
      loader.css("display","none");
      list.css("display","block");
    };
    $(document).on('submit','#form', function(e){
        e.preventDefault();
        fn_search($('#search').val());
    });
    function fn_search(param){
      $("#comment").empty();
      $(".list").empty();
      fn_loading();
      var subUrl = 'http://192.168.0.20:5555/main'
      console.log(param)
      $.ajax({
          url : subUrl
         ,dataType: 'json'
         ,type: 'POST'
         ,data : {test: param }
         ,success : function(data){
            console.log('most_word : ',data['most_word']);
            console.log('comment : ',data['comment']);
            fn_hiding();
            $("#comment").append("<h1>"+data['comment']+"</h1>");
            var most_word = data['most_word']
            var table="<br><br><br><table><th>키워드</th><th>빈도수</th>"
            $.each(most_word , function(i){
                table += "<tr><td><h1>" + most_word[i][0] + "</h1></td>";
                table += "<td><h3>" + most_word[i][1] + "</h3></td></tr>"
           });
            table+="</table>"
            $("#portable").html(table);
            $("button").button();
         }
         ,error(e){
            console.log(e);
         }
      });
    }
});