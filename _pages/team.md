---
title: "Kolachalama laboratory - Team"
layout: gridlay
excerpt: "Kolachalama laboratory: Team members"
sitemap: false
permalink: /team/
---
<script src="https://kit.fontawesome.com/03aee70ce1.js" crossorigin="anonymous"></script>

## Principal Investigator
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if member.group == 0 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4><a href="{{ member.url }}" class="off">{{ member.name }}</a></h4>
  <i>{{ member.info }}</i>

  <h2>{% if member.github %}<a href="{{ member.github }}"><i class='fa fa-github'></i></a>{% endif %}
  {% if member.scholar %}<a href="{{ member.scholar }}"><i class="fa-solid fa-user-graduate"></i></a>{% endif %}
  {% if member.linkedin %}<a href="{{ member.linkedin }}"><i class="fa-brands fa-linkedin-in"></i></a>{% endif %}
  {% if member.twitter %}<a href="{{ member.twitter }}"><i class='fa fa-twitter'></i></a>{% endif %}</h2>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

---

## Postdoctoral scholars
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if member.group == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4><a href="{{ member.url }}" class="off">{{ member.name }}</a></h4>
  <i>{{ member.info }}</i>

  <h2>{% if member.github %}<a href="{{ member.github }}"><i class='fa fa-github'></i></a>{% endif %}
  {% if member.scholar %}<a href="{{ member.scholar }}"><i class="fa-solid fa-user-graduate"></i></a>{% endif %}
  {% if member.linkedin %}<a href="{{ member.linkedin }}"><i class="fa-brands fa-linkedin-in"></i></a>{% endif %}</h2>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

---

## Graduate students
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if member.group == 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4><a href="{{ member.url }}" class="off">{{ member.name }}</a></h4>
  <i>{{ member.info }}</i>

  <h2>{% if member.github %}<a href="{{ member.github }}"><i class='fa fa-github'></i></a>{% endif %}
  {% if member.scholar %}<a href="{{ member.scholar }}"><i class="fa-solid fa-user-graduate"></i></a>{% endif %}
  {% if member.linkedin %}<a href="{{ member.linkedin }}"><i class="fa-brands fa-linkedin-in"></i></a>{% endif %}</h2>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

---

## Research staff
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if member.group == 3 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4><a href="{{ member.url }}" class="off">{{ member.name }}</a></h4>
  <i>{{ member.info }}</i>

  <h2>{% if member.github %}<a href="{{ member.github }}"><i class='fa fa-github'></i></a>{% endif %}
  {% if member.scholar %}<a href="{{ member.scholar }}"><i class="fa-solid fa-user-graduate"></i></a>{% endif %}
  {% if member.linkedin %}<a href="{{ member.linkedin }}"><i class="fa-brands fa-linkedin-in"></i></a>{% endif %}</h2>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

---

## Undergraduate students
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if member.group == 4 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4><a href="{{ member.url }}" class="off">{{ member.name }}</a></h4>
  <i>{{ member.info }}</i>

  <h2>{% if member.github %}<a href="{{ member.github }}"><i class='fa fa-github'></i></a>{% endif %}
  {% if member.scholar %}<a href="{{ member.scholar }}"><i class="fa-solid fa-user-graduate"></i></a>{% endif %}
  {% if member.linkedin %}<a href="{{ member.linkedin }}"><i class="fa-brands fa-linkedin-in"></i></a>{% endif %}</h2>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

---

## Visiting scholars
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if member.group == 5 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4><a href="{{ member.url }}" class="off">{{ member.name }}</a></h4>
  <i>{{ member.info }}</i>

  <h2>{% if member.github %}<a href="{{ member.github }}"><i class='fa fa-github'></i></a>{% endif %}
  {% if member.scholar %}<a href="{{ member.scholar }}"><i class="fa-solid fa-user-graduate"></i></a>{% endif %}
  {% if member.linkedin %}<a href="{{ member.linkedin }}"><i class="fa-brands fa-linkedin-in"></i></a>{% endif %}</h2>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

---

## Alumni

{% for member in site.data.team_members %}
{% if member.group == 8 %}

<i class="alumni1">{{ member.name }}</i><br>
<i class="alumni2">{{ member.info }} {{ member.year }}</i> {% if member.next %} 
<i class="alumni2">Next step: {{ member.next }}</i> {% if member.extlink %} <a class="alumni2" style="padding-left: 0px;" href="{{ member.extlink }}">(Link)</a>
{% endif %}
{% endif %}

{% endif %}
{% endfor %}

---

## Administrative support
Please contact our section administrator, <a href="mailto:kharp@bu.edu">Katie Harper</a>.
