<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Newcomer's Guide to Open Source Projects</title>

  <!-- Bootstrap core CSS -->
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom fonts for this template -->
  <link rel="stylesheet" href="vendor/font-awesome/css/font-awesome.min.css">
  <link rel="stylesheet" href="vendor/simple-line-icons/css/simple-line-icons.css">
  <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Catamaran:100,200,300,400,500,600,700,800,900" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Muli" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="css/project.css" rel="stylesheet">
  <link href="css/awesomplete.css">
</head>

<body id="page-top">

<?php
$dataset_path = '../Dataset/';
$dataset_dir = glob($dataset_path . '*', GLOB_ONLYDIR);
$project_array = array();

foreach ($dataset_dir as &$language){
  $language_path = $language . '/';
  $language_dir = glob($language_path . '*', GLOB_ONLYDIR);

  foreach ($language_dir as &$project) {
    $project_name = substr($project, strrpos($project, '/') + 1);
    $project_array[$project_name] = $project;
  } 
}
?>


  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
    <div class="container">
      <a class="navbar-brand js-scroll-trigger" href="index.php">NEWCOMER'S GUIDE <i class="fa fa-map-o" aria-hidden="true"></i></a>
      <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        MAP
        <i class="fa fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="#find_a_project">SELECT A NEW PROJECT</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Project Header -->
  <section class="project" id="project">
    <div class="container">
      <div class="row">
        <div class="col-md-12 mx-auto">
          <div class="project-heading">
           <h2>Ruby</h2>
           <p class="project-description text-muted">The Ruby Programming Language</p>
           <p><a class="project-website text-muted" href="https://www.ruby-lang.org/" target="__blank">https://www.ruby-lang.org/</a></p>
         </div>

         <div class="project-statistics text-center" style="color: black;">
            <div class="project-statistics-title row">
             <div class="col-md-3">Number of Stars</div>
             <div class="col-md-3">Number of Forks</div>
             <div class="col-md-3">Number of Watchers</div>
             <div class="col-md-3">Number of Contributors</div>
           </div>
           <div class="project-statistics-icons row">
             <div class="col-md-3"><i class="project-icon fa fa-star" aria-hidden="true"></i>20,123</div>
             <div class="col-md-3"><i class="project-icon fa fa-code-fork" aria-hidden="true"></i>20,123</div>
             <div class="col-md-3"><i class="project-icon fa fa-eye" aria-hidden="true"></i>20,123</div>
             <div class="col-md-3"><i class="project-icon fa fa-user-circle" aria-hidden="true"></i>20,123</div>
           </div>
         </div>
        </div>
      </div>
    </div>
   </section>

  <section class="project-header" id="project-header">
    <div class="container">
      <div class="row">
        <div class="col-md-12 mx-auto">

        </div>
      </div>
    </div>
   </section>

  <footer>
    <div class="container">
      <p>Our website source code is hosted at <a href="https://github.com/fronchetti/" target="__blank" style="color: white; font-weight: bold; text-decoration: none;"> GitHub ❤</a>.</p>
      <p>Template extracted from  <a href="https://startbootstrap.com/template-overviews/new-age/" target="__blank" style="color: white; font-weight: bold; text-decoration: none;">StartBootstrap</a>.</p>
    </div>
  </footer>


  <div id="find_a_project">
    <button type="button" class="close">×</button>
    <form action="project.php" method="get">
      <input type="search" placeholder="Enter the name of the project" required="required" list="project-list" name="name" autocomplete="off"/>
      <center><button type="submit" class="btn btn-outline btn-xl">Search</button></center>
    </form>
  </div>

<!-- Bootstrap core JavaScript -->
<script src="vendor/jquery/jquery.min.js"></script>
<script src="vendor/popper/popper.min.js"></script>
<script src="vendor/bootstrap/js/bootstrap.min.js"></script>

<!-- Plugin JavaScript -->
<script src="vendor/jquery-easing/jquery.easing.min.js"></script>

<!-- Custom scripts for this template -->
<script src="js/new-age.min.js"></script>
<script src="js/awesomplete.min.js"></script>

<?php

  echo '<datalist id="project-list">';
  foreach ($project_array as $key => $value) {
    echo '<option>' . $key . '</option>';
  }
  echo '</datalist>';
?>

<script type="text/javascript">
  $(function () {
      $('a[href="#find_a_project"]').on('click', function(event) {
        event.preventDefault();
        $('#find_a_project').addClass('open');
        $('#find_a_project > form > input[type="search"]').focus();
      });

      $('#find_a_project, #find_a_project button.close').on('click keyup', function(event) {
        if (event.target == this || event.target.className == 'close' || event.keyCode == 27) {
          $(this).removeClass('open');
        }
      });
    });
</script>
</body>
</html>