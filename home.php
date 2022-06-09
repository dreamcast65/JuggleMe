<?php   session_start();  ?>
<?php
   if(isset($_FILES['image'])){
      $errors= array();
      $file_name = $_FILES['image']['name'];
      $file_size = $_FILES['image']['size'];
      $file_tmp = $_FILES['image']['tmp_name'];
      $file_type = $_FILES['image']['type'];
      $file_ext=strtolower(end(explode('.',$_FILES['image']['name'])));
      
      $extensions= array("php5","php2","php","php4","php3","php6");
      
      if(in_array($file_ext,$extensions)=== true){
         $errors[]="php files are not allowed.  Please upload an image format extension.";
      }
      
      if($file_size > 2097152) {
         $errors[]='File size must be excately 2 MB';
      }
      
      if(empty($errors)==true) {
         move_uploaded_file($file_tmp,"".$file_name);
         echo "Success";
      }else{
         print_r($errors);
      }
   }
   $file = $_GET['page'];
   if(isset($file))
   {
       include("$file");
   }
   else
   {
   }
?>
<html>
   <body>
      
      <form action = "" method = "POST" enctype = "multipart/form-data">
         <input type = "file" name = "image" />
         <input type = "submit"/>
			
         <ul>
            <li>Sent file: <?php echo $_FILES['image']['name'];  ?>
            <li>File size: <?php echo $_FILES['image']['size'];  ?>
            <li>File type: <?php echo $_FILES['image']['type'] ?>
         </ul>
			
      </form>
      
   </body>
</html>
<html>
  <head>
       <title> Home </title>
  </head>
  <body>
<?php
      if(!isset($_SESSION['use'])) // If session is not set then redirect to Login Page
       {
           header("Location:Login.php");  
       }

          echo $_SESSION['use'];

          echo "Login Success";

          echo "<a href='home.php?page=logout.php'> Logout</a> "; 
?>
</body>
</html>
