---
layout: default
title: Roomcord
permalink: /roomcord/
---
{% assign releases = site.releases | where: "product", "roomcord" | sort: "date" | reverse %}
<section class="product-hero product-roomcord">
  <div class="ambient-grid" aria-hidden="true"></div><div class="shell narrow"><p class="eyebrow"><span></span>Roomcord release notes</p><h1>Rooms where people and agents work together.</h1><p class="hero-lede">Progress across conversations, calls, scheduling, collaboration, and connected agents. Client and API changes appear together as one product.</p><div class="release-meta"><span>{{ releases | size }} milestones</span><span>Client + API</span></div></div>
</section>
<section class="timeline-section"><div class="shell single-timeline"><div class="timeline">
{% for release in releases %}<article class="timeline-entry product-roomcord"><div class="timeline-date"><time>{{ release.date | date: "%Y-%m-%d" }}</time><span>{{ release.version }}</span></div><a class="release-card" href="{{ release.url | relative_url }}"><p class="release-product"><span></span>Roomcord</p><h3>{{ release.title }}</h3><p>{{ release.summary }}</p><b>Read release note <span>→</span></b></a></article>{% endfor %}
</div></div></section>
