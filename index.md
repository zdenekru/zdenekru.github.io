---
layout: default
title: "Home"
---

# Welcome to My Technical Blog

This is where I document my projects, findings, and experiments.

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> — {{ post.date | date: "%Y-%m-%d" }}
    </li>
  {% endfor %}
</ul>
