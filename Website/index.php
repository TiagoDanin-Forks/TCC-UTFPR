<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>▶ Newcomer's Guide to Open Source Projects</title>

  <!-- Bootstrap core CSS -->
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom fonts for this template -->
  <link rel="stylesheet" href="vendor/font-awesome/css/font-awesome.min.css">
  <link rel="stylesheet" href="vendor/simple-line-icons/css/simple-line-icons.css">
  <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Catamaran:100,200,300,400,500,600,700,800,900" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Muli" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="css/new-age.css" rel="stylesheet">
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
      <a class="navbar-brand js-scroll-trigger" href="#page-top">NEWCOMER'S GUIDE <i class="fa fa-map-o" aria-hidden="true"></i></a>
      <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        MAP
        <i class="fa fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link js-scroll-trigger" href="#barriers">Barriers</a>
          </li>
          <li class="nav-item">
            <a class="nav-link js-scroll-trigger" href="#research">Research</a>
          </li>
          <li class="nav-item">
            <a class="nav-link js-scroll-trigger" href="#dataset">Dataset</a>
          </li>
          <li class="nav-item">
            <a class="nav-link js-scroll-trigger" href="#team">Team</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <header class="masthead">
    <div class="container h-100">
      <div class="row h-100">
        <div class="col-lg-7 my-auto">
          <div class="header-content mx-auto">
            <h1 class="mb-5">Newcomers often face barriers when trying to contribute with open source projects. Our mission is to help them in the contribution process.</h1>
            <a href="#barriers" class="btn btn-outline btn-xl js-scroll-trigger">Learn more!</a>
          </div>
        </div>
        <div class="col-lg-5 my-auto">
        </div>
      </div>
    </div>
  </header>

  <section class="barriers text-center" id="barriers">
    <div class="container">
      <div class="row">
        <div class="col-md-8 mx-auto">
          <h2 class="section-heading">Barriers</h2>
          <p>Open source projects usually require outside contributions to stay active in the development process. However, even with this need, new contributors often face barriers when attempting to submit contributions to an open source project.<a href="http://dl.acm.org/citation.cfm?id=2675215" target="__blank" style="color: black;">¹</a><p>
            <p>A barrier in this context may be related to several aspects, such as aspects related to the newcomers knowledge, cultural aspects and related to the receptivity of the project.<a href="http://www.igor.pro.br/publica/papers/OSS2014.pdf" target="__blank" style="color: black">²</a></p>
            <p>Our goal at this moment is to present to newcomers a research of open source projects, presenting an analysis of the receptivity of new contributors in these repositories based on metrics studied by the researchers of this initiative.</p>
            <center><a href="#research" class="btn btn-outline btn-xl js-scroll-trigger" style="background-color: black;">Meet our research!</a></center>
          </div>
        </div>
      </div>
    </section>

    <section class="research text-center" id="research">
      <div class="container">
        <div class="row">
          <div class="col-md-8 mx-auto">
            <div class="section-heading">
             <h2>Our Research</h2>
             <p class="text-muted">An analysis of open source projects receptiveness</p>
           </div>
           <p>Open source projects usually require outside contributions to stay active in the development process. However, even with this need, new contributors often face barriers when attempting to submit contributions to an open source project.<a href="http://dl.acm.org/citation.cfm?id=2675215" target="__blank" style="color: black;">¹</a><p>
           </div>
         </div>
       </div>
     </section>

     <section class="dataset text-center" id="dataset">
      <div class="container">
        <div class="row">
          <div class="col-md-8 mx-auto">
            <div class="section-heading">
             <h2>Dataset</h2>
             <p class="text-muted">And an analysis of open source projects</p>
           </div>
           <p>Open source projects usually require outside contributions to stay active in the development process. However, even with this need, new contributors often face barriers when attempting to submit contributions to an open source project.<a href="http://dl.acm.org/citation.cfm?id=2675215" target="__blank" style="color: black;">¹</a><p>
            <center><a href="#find_a_project" class="btn btn-outline btn-xl" style="background-color: black;">Visualize a project!</a></center>
          </div>
        </div>
      </div>
    </section>

    <section class="team" id="team">
      <div class="container">
        <div class="row">
          <div class="col-md-12 mx-auto">
            <h2 class="text-center">Research Team</h2>
            <div class="container">
              <div class="row">
                <div class="col-md-3">
                  <img src="img/profile_felipe.jpg" alt="..." class="img-responsive" style="width: 150px; height: 150px; border-radius: 5px;">
                  <p class="team-profile-name">Luiz Felipe Fronchetti Dias</p>
                  <p class="team-profile-email">luizdias@alunos.utfpr.edu.br</p>
                  <p class="team-profile-university">Federal University of Technology – Paraná</p>         
                </div>
                <div class="col-md-3">
                  <img src="#" alt="..." class="img-responsive" style="width: 150px; height: 150px; border-radius: 5px;">
                  <p class="team-profile-name">Igor Scaliante Wiese</p>
                  <p class="team-profile-email">igor@utfpr.edu.br</p>
                  <p class="team-profile-university">Federal University of Technology – Paraná</p>         
                </div>  
                <div class="col-md-3">
                  <img src="#" alt="..." class="img-responsive" style="width: 150px; height: 150px; border-radius: 5px;">
                  <p class="team-profile-name">Igor Steinmacher</p>
                  <p class="team-profile-email">igorfs@utfpr.edu.br</p>
                  <p class="team-profile-university">Federal University of Technology – Paraná</p>         
                </div>
                <div class="col-md-3">
                  <img src="#" alt="..." class="img-responsive" style="width: 150px; height: 150px; border-radius: 5px;">
                  <p class="team-profile-name">Gustavo Pinto</p>
                  <p class="team-profile-email">gpinto@ufpa.br</p>
                  <p class="team-profile-university">Federal University of Pará</p>         
                </div>      
              </div>
            </div>
          </div>
        </section>

        <footer>
          <div class="container">
            <p>Our website source code is hosted at <a href="https://github.com/fronchetti/" target="__blank" style="color: white; font-weight: bold; text-decoration: none;"> GitHub ❤</a>.</p>
            <p>Website template developed by <a href="https://startbootstrap.com/template-overviews/new-age/" target="__blank" style="color: white; font-weight: bold; text-decoration: none;">StartBootstrap</a>.</p>
          </div>
        </footer>

        <div id="find_a_project">
          <button type="button" class="close">×</button>
          <form action="project.php" method="get">
            <input type="search" placeholder="Enter the name of the project" required="required" list="project-list" name="name" />
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
