<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css">
    <title>Django CRUD application!</title>
  </head>
  <body>
    <div class="container">
      <form method="post">{% csrf_token %}
        Are you sure you want to delete "{{ object }}" ?
        <input class="btn btn-primary" type="submit" value="Submit" />
      </form>
    </div>
  </body>
</html>