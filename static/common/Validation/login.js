function login(){
    var username=document.getElementById("user_email").value
    var passw=document.getElementById("user_password").value
    
    if(username==""){
        document.getElementById("un1").innerHTML="Please Enter Email"
        document.getElementById("un1").style.color="red"
        document.getElementById("user_email").style.border="1px solid red"
        return false
    }
    else{
        document.getElementById("un1").innerHTML=""
        document.getElementById("un1").style.color=""
        document.getElementById("user_email").style.border=""
    }

    if(passw==""){
        document.getElementById("pw1").innerHTML="Please Enter Password"
        document.getElementById("pw1").style.color="red"
        document.getElementById("user_password").style.border="1px solid red"
        return false
    }
    else{
        document.getElementById("pw1").innerHTML=""
        document.getElementById("pw1").style.color=""
        document.getElementById("user_password").style.border=""
    }
}