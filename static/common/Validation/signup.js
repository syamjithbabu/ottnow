function sign(){
    var txtname1=document.getElementById("name1").value
    var txtname2=document.getElementById("name2").value
    var ages=document.getElementById("age1").value
    var mail1=document.getElementById("mail1").value
    var passw=document.getElementById("pw").value

    if(txtname1==""){
        document.getElementById("name_err1").innerHTML="Please Enter Your Name"
        document.getElementById("name_err1").style.color="red"
        document.getElementById("name1").style.border="1px solid red"
        return false

    }
    else{
        document.getElementById("name_err1").innerHTML=""
        document.getElementById("name_err1").style.color=""
        document.getElementById("name1").style.border=""
        
    }
    if(txtname2==""){
        document.getElementById("name_err2").innerHTML="Please Enter Your Name"
        document.getElementById("name_err2").style.color="red"
        document.getElementById("name2").style.border="1px solid red"
        return false
    }
    else{
      document.getElementById("name_err2").innerHTML=""
      document.getElementById("name_err2").style.color=""
      document.getElementById("name2").style.border=""
    }

    if(ages==""){
        document.getElementById("age_err").innerHTML="Please Enter Your Age"
        document.getElementById("age_err").style.color="red"
        document.getElementById("age1").style.border="1px solid red"
        return false
    }
    else{
      document.getElementById("age_err").innerHTML=""
      document.getElementById("name_err2").style.color=""
      document.getElementById("age1").style.border=""
    }
    if(mail1==""){
      document.getElementById("mail_err").innerHTML="Please Enter Your Email"
      document.getElementById("mail_err").style.color="red"
      document.getElementById("mail1").style.border="1px solid red"
      return false
    }
    else{
      document.getElementById("mail_err").innerHTML=""
      document.getElementById("mail_err").style.color=""
      document.getElementById("mail1").style.border=""
    }
    if(passw==""){
      document.getElementById("pw_err").innerHTML="Please Enter Password"
      document.getElementById("pw_err").style.color="red"
      document.getElementById("pw").style.border="1px solid red"
      return false
    }
    else{
      document.getElementById("pw_err").innerHTML=""
      document.getElementById("pw_err").style.color=""
      document.getElementById("pw").style.border=""
    }
}