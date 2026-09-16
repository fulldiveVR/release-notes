---
layout: default
title: Hermes Hub
permalink: /hermes-hub/
---
{% assign releases = site.releases | where: "product", "hermes-hub" | sort: "date" | reverse %}
<section class="product-hero product-hermes-hub">
  <div class="ambient-grid" aria-hidden="true"></div><div class="shell narrow"><p class="eyebrow"><span></span>Hermes Hub release notes</p><h1>The control plane behind hosted agents.</h1><p class="hero-lede">Runtime orchestration, tenant lifecycle, peer protocols, scheduling, policy, storage, and operator workflows.</p><div class="release-meta"><span>{{ releases | size }} milestones</span><span>Weekly digest</span></div></div>
</section>
<section class="timeline-section"><div class="shell single-timeline"><div class="timeline">
{% for release in releases %}<article class="timeline-entry product-hermes-hub"><div class="timeline-date"><time>{{ release.date | date: "%Y-%m-%d" }}</time><span>{{ release.version }}</span></div><a class="release-card" href="{{ release.url | relative_url }}"><p class="release-product"><span></span>Hermes Hub</p><h3>{{ release.title }}</h3><p>{{ release.summary }}</p><b>Read release note <span>→</span></b></a></article>{% endfor %}
</div></div></section>
