---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{https://scholar.google.ca/citations?hl=en&user=CdlcSHQAAAAJ&view_op=list_works&gmla=AJsN-F4V1rJfErFaJSSKFspypzDMqu1OTq73jVSZyrCBMmbZDo3bkvGH54ftbmPIDHLggFCGb9yg7jg-gRRUwu_pUahV3SXOrBfc0Xn1_Ql-M0iWJJhxmHg}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
