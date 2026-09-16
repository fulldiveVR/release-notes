---
layout: default
title: Latest updates
---
{% assign releases = site.releases | sort: "date" | reverse %}
<section class="home-hero">
  <div class="ambient-grid" aria-hidden="true"></div>
  <div class="ambient-orb orb-one" aria-hidden="true"></div>
  <div class="ambient-orb orb-two" aria-hidden="true"></div>
  <div class="shell hero-grid">
    <div class="hero-copy">
      <p class="eyebrow"><span></span>Product release notes</p>
      <h1>See what we’ve been <em>shipping.</em></h1>
      <p class="hero-lede">A clear, chronological record of improvements across Roomcord, Autoworker Hub, and Hermes Hub.</p>
      <div class="hero-actions">
        <a class="button" href="#latest">Browse updates <span aria-hidden="true">↓</span></a>
        <a class="button secondary" href="{{ '/feed.xml' | relative_url }}">Follow the feed</a>
      </div>
    </div>
    <div class="release-console" aria-label="Release notes summary">
      <div class="console-bar"><span></span><span></span><span></span><small>release-stream</small></div>
      <div class="console-grid">
        <a href="{{ '/roomcord/' | relative_url }}"><strong>12</strong><span>Roomcord milestones</span></a>
        <a href="{{ '/autoworker-hub/' | relative_url }}"><strong>14</strong><span>Autoworker updates</span></a>
        <a href="{{ '/hermes-hub/' | relative_url }}"><strong>15</strong><span>Hermes Hub updates</span></a>
        <div><strong>Weekly</strong><span>Reviewed public notes</span></div>
      </div>
    </div>
  </div>
</section>

<section class="product-strip" aria-label="Products">
  <div class="shell product-grid">
    <a href="{{ '/roomcord/' | relative_url }}"><span class="product-icon roomcord-icon">R</span><span><b>Roomcord</b><small>Rooms, calls, messaging, and agents</small></span><i>↗</i></a>
    <a href="{{ '/autoworker-hub/' | relative_url }}"><span class="product-icon autoworker-icon">A</span><span><b>Autoworker Hub</b><small>Hosted multi-tenant AI runtimes</small></span><i>↗</i></a>
    <a href="{{ '/hermes-hub/' | relative_url }}"><span class="product-icon hermes-icon">H</span><span><b>Hermes Hub</b><small>Runtime orchestration and operations</small></span><i>↗</i></a>
  </div>
</section>

<section class="timeline-section" id="latest">
  <div class="shell timeline-layout">
    <header class="timeline-intro">
      <p class="eyebrow"><span></span>Chronological changelog</p>
      <h2>Latest first.</h2>
      <p>Product-level notes drawn from shipped work and reviewed before publication.</p>
      <div class="legend"><span class="dot roomcord-dot"></span> Roomcord <span class="dot autoworker-dot"></span> Autoworker <span class="dot hermes-dot"></span> Hermes</div>
    </header>
    <div class="timeline">
      {% for release in releases %}
      <article class="timeline-entry product-{{ release.product }}">
        <div class="timeline-date"><time datetime="{{ release.date | date_to_xmlschema }}">{{ release.date | date: "%Y-%m-%d" }}</time><span>{{ release.version }}</span></div>
        <a class="release-card" href="{{ release.url | relative_url }}">
          <p class="release-product"><span></span>{{ release.product_name }}</p>
          <h3>{{ release.title }}</h3>
          <p>{{ release.summary }}</p>
          <b>Read release note <span aria-hidden="true">→</span></b>
        </a>
      </article>
      {% endfor %}
    </div>
  </div>
</section>
