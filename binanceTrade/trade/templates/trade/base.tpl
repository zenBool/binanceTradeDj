<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    {% load static %}

    <link rel="stylesheet" href="{% static 'trade/css/bootstrap.min.css' %}">

    <title>
        {% block title %}
             Default Django
        {% endblock title %}
    </title>
</head>
<body class="container">
    <H1>Hello, My TPL file</H1>
</body>
</html>