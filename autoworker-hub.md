---
layout: default
title: Autoworker Hub
permalink: /autoworker-hub/
---

# Autoworker Hub

{% assign releases = site.releases | where: "product", "autoworker-hub" | sort: "date" | reverse %}
{% for release in releases %}
- {{ release.date | date: "%Y-%m-%d" }}: [{{ release.title }}]({{ release.url | relative_url }}){% if release.version %} ({{ release.version }}){% endif %}
{% endfor %}

