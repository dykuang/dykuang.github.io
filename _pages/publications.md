---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
You can also find my recent publications on <span style="color:blue"> [my Google Scholar profile](https://scholar.google.com/citations?user=CdlcSHQAAAAJ&hl=en) </span>

I am also working on an open source book about deep learning in eeg based affective computing: [EEG-Affective-Computing](https://dykuang.github.io/EEG-Affective-Computing/). Welcome to contribute if interested.

{% if author.googlescholar %}
  You can also find my articles on [my Google Scholar profile](https://scholar.google.com/citations?user=CdlcSHQAAAAJ&hl=en)
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
