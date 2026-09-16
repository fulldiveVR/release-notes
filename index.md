---
layout: default
title: Latest updates
---

# Latest updates

{% assign releases = site.releases | sort: "date" | reverse %}
{% for release in releases %}
<article class="card">
  <p class="product">{{ release.product_name }}</p>
  <h2><a href="{{ release.url | relative_url }}">{{ release.title }}</a></h2>
  <p class="date">{{ release.date | date: "%B %-d, %Y" }}{% if release.version %} · {{ release.version }}{% endif %}</p>
  <p>{{ release.summary }}</p>
</article>
{% endfor %}

