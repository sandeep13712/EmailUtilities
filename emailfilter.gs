function deleteAllEmailsFromINBOXorFromALabel() {

// get all email threads from a particular label
var label = GmailApp.getUserLabelByName("emailidstodelete");
var threads = label.getThreads();

// get all email threads from INBOX
//var threads = GmailApp.getInboxThreads();
  
  
for (var i = 0; i < threads.length; i++) {
  
  messages = threads[i].getMessages();
  
  for (var j = 0; j < messages.length; j++) {
    
    fromAdd = messages[j].getFrom();
    
    if(fromAdd.indexOf('mailer-daemon@googlemail.com')>-1){
    //Logger.log(messages[j].getPlainBody());  
      
    messageText = messages[j].getPlainBody()
    precedingText1 = 'delivering your message to ';
    followingText1 = 'Gmail will retry';
    
    precedingText2 = 'wasn\'t delivered to';
    followingText2 = 'because the address';
    
    index1 = messageText.indexOf(precedingText1)
    index2 = messageText.indexOf(precedingText2)
    
    index1End = messageText.indexOf(followingText1)
    index2End = messageText.indexOf(followingText2)
    
    //Logger.log(index1)
    //Logger.log(index2)
    
    if(index1>-1 && index1End>-1){
        
        emailIdToDelete = messageText.substring(index1+precedingText1.length, index1End)
        Logger.log(emailIdToDelete)
      };
      
      if(index2>-1 && index2End>-1){
        
        emailIdToDelete = messageText.substring(index2+precedingText2.length, index2End)
        Logger.log(emailIdToDelete)
      };
      
 
    }
    
    else{
      //Do nothing
    };
    
  };
  
  
  
  
  
}
  
};