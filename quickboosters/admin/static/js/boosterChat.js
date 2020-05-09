var socket = io.connect('http://127.0.0.1:5000');
      socket.on('connect', function() {
      socket.send('Booster Connected To Chat');
  });

  var form = $('#chat-submit').click(function(){
      console.log("Clicked");

      let user_msg = $('#chat-text').val()
     
       socket.emit('booster_msg', {
           user_name : "{{name}}",
           message : user_msg
       });

      $('#chat-text').val('').focus()
  });

  socket.on('display_to_chat', function(msg){
      $( 'div.message' ).append( '<div><b style="color: #000">'+msg.user_name+'</b> '+msg.message+'</div>' )
      });
