<?php  session_start();   // session starts with the help of this function 


if(isset($_SESSION['use']))   // Checking whether the session is already there or not if 
                              // true then header redirect it to the home page directly 
 {
    header("Location:home.php"); 
 }

if(isset($_POST['login']))   // it checks whether the user clicked login button or not 
{
     $user = $_POST['user'];
     $pass = hash('sha256',$_POST['pass']);

      if($user == "admin" && $pass == hash('sha256','Sol7trnk00'))  // username is  set to "Ank"  and Password   
         {                                   // is 1234 by default     

          $_SESSION['use']=$user;


         echo '<script type="text/javascript"> window.open("home.php","_self");</script>';            //  On Successful Login redirects to home.php

        }

        else
        {
            echo "invalid UserName or Password";        
        }
}
 ?>
<html>
<head>
<!-- We recently implemented a super secure SHA256 hashing algorithm on all of our passwords to ensure a "secure" means of storing passwords.-->

<title> Login Page   </title>
</head>
<style><?php include 'style.css'?>
</style>
<body>
<div class="containter">
<form action="" method="post">
    <table width="200" border="0">
  <tr>
    <td>  UserName</td>
    <td> <input type="text" name="user" > </td>
  </tr>
  <tr>
    <td> PassWord  </td>
    <td><input type="password" name="pass"></td>
  </tr>
  <tr>
 <div class="container" style="background-color:#f1f1f1">
    <td> <input type="submit" name="login" value="LOGIN"></td>
    <td></td>
  </tr>
</table>
</form>
</div>
</body>
</html>
