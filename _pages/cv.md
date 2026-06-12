---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<style>
  #main {
    max-width: min(96vw, 84rem);
  }

  .cv-page {
    --cv-ink: #16303b;
    --cv-muted: #5d7278;
    --cv-line: rgba(22, 48, 59, 0.12);
    --cv-panel: rgba(255, 255, 255, 0.92);
    --cv-accent: #0f7c82;
    --cv-accent-soft: rgba(15, 124, 130, 0.12);
    display: grid;
    gap: clamp(1rem, 2vw, 1.6rem);
  }

  .cv-hero,
  .cv-section,
  .cv-archive-panel {
    border: 1px solid var(--cv-line);
    border-radius: 24px;
    background: var(--cv-panel);
    box-shadow: 0 18px 50px rgba(20, 49, 61, 0.08);
  }

  .cv-hero {
    overflow: hidden;
    padding: clamp(1.25rem, 2.4vw, 2rem);
    background:
      radial-gradient(circle at top right, rgba(15, 124, 130, 0.16), transparent 26%),
      radial-gradient(circle at left center, rgba(212, 158, 76, 0.10), transparent 30%),
      linear-gradient(135deg, rgba(252, 248, 243, 0.98), rgba(242, 248, 249, 0.96));
  }

  .cv-kicker {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    margin: 0 0 0.9rem;
    padding: 0.38rem 0.82rem;
    border-radius: 999px;
    background: rgba(22, 48, 59, 0.08);
    color: var(--cv-muted);
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
  }

  .cv-hero h2,
  .cv-section h2,
  .cv-card h3,
  .cv-timeline-card h3,
  .cv-archive-panel h2 {
    color: var(--cv-ink);
  }

  .cv-hero h2 {
    margin: 0;
    font-size: clamp(2rem, 4vw, 3.1rem);
    line-height: 1.04;
  }

  .cv-lead {
    max-width: 44rem;
    margin: 0.95rem 0 0;
    color: var(--cv-muted);
    font-size: 1.03rem;
    line-height: 1.8;
  }

  .cv-pill-row,
  .cv-link-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
  }

  .cv-pill-row {
    margin-top: 1.3rem;
  }

  .cv-pill {
    display: inline-flex;
    align-items: center;
    padding: 0.48rem 0.82rem;
    border: 1px solid var(--cv-line);
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.82);
    color: var(--cv-muted);
    font-size: 0.92rem;
  }

  .cv-link-row {
    margin-top: 1.3rem;
  }

  .cv-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 42px;
    padding: 0.72rem 1rem;
    border-radius: 999px;
    border: 1px solid var(--cv-line);
    background: #fff;
    color: var(--cv-ink);
    font-weight: 600;
    text-decoration: none;
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
  }

  .cv-link:hover {
    transform: translateY(-1px);
    border-color: rgba(22, 48, 59, 0.24);
    box-shadow: 0 10px 24px rgba(20, 49, 61, 0.1);
    text-decoration: none;
  }

  .cv-link--accent {
    border-color: transparent;
    background: linear-gradient(135deg, #15868d, #0f666b);
    color: #fff;
  }

  .cv-section,
  .cv-archive-panel {
    padding: clamp(1.1rem, 2vw, 1.6rem);
  }

  .cv-section-head {
    display: grid;
    gap: 0.35rem;
    margin-bottom: 1.1rem;
  }

  .cv-section-head p,
  .cv-card p,
  .cv-timeline-card p,
  .cv-archive-panel p {
    margin: 0;
    color: var(--cv-muted);
    line-height: 1.72;
  }

  .cv-section-kicker {
    color: var(--cv-accent);
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
  }

  .cv-grid {
    display: grid;
    gap: 1rem;
  }

  .cv-grid--education {
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  }

  .cv-card,
  .cv-timeline-card {
    padding: 1.15rem;
    border: 1px solid var(--cv-line);
    border-radius: 20px;
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.96), rgba(248, 251, 251, 0.9));
  }

  .cv-card--warm {
    background: linear-gradient(180deg, rgba(244, 232, 217, 0.56), rgba(255, 255, 255, 0.94));
  }

  .cv-card--cool {
    background: linear-gradient(180deg, rgba(220, 234, 240, 0.62), rgba(255, 255, 255, 0.94));
  }

  .cv-label {
    display: inline-flex;
    margin-bottom: 0.75rem;
    padding: 0.35rem 0.7rem;
    border-radius: 999px;
    background: var(--cv-accent-soft);
    color: var(--cv-accent);
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.03em;
  }

  .cv-meta {
    margin-top: 0.25rem;
    color: var(--cv-muted);
    font-size: 0.94rem;
  }

  .cv-timeline {
    display: grid;
    gap: 0.95rem;
  }

  .cv-timeline-card {
    position: relative;
    padding-left: 1.25rem;
  }

  .cv-timeline-card:before {
    content: "";
    position: absolute;
    left: 0;
    top: 1.2rem;
    bottom: 1.2rem;
    width: 4px;
    border-radius: 999px;
    background: linear-gradient(180deg, #15868d, rgba(21, 134, 141, 0.16));
  }

  .cv-timeline-top {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem 1rem;
    align-items: baseline;
    justify-content: space-between;
    margin-bottom: 0.45rem;
  }

  .cv-timeline-top h3 {
    margin: 0;
  }

  .cv-timeline-date {
    color: var(--cv-accent);
    font-size: 0.9rem;
    font-weight: 700;
  }

  .cv-focus-grid {
    display: grid;
    gap: 0.9rem;
    grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
  }

  .cv-focus-item {
    padding: 1rem;
    border: 1px solid var(--cv-line);
    border-radius: 18px;
    background: rgba(255, 255, 255, 0.76);
  }

  .cv-focus-item strong {
    display: block;
    margin-bottom: 0.4rem;
    color: var(--cv-ink);
  }

  .cv-archive-grid {
    display: grid;
    gap: 1rem;
  }

  .cv-archive-list {
    margin: 0.9rem 0 0;
    padding: 0;
    list-style: none;
  }

  .cv-archive-list .list__item,
  .cv-archive-list .archive__item {
    margin: 0;
  }

  .cv-archive-list li {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .cv-archive-list .archive__item {
    padding: 0.95rem 0;
    border-bottom: 1px solid var(--cv-line);
  }

  .cv-archive-list .list__item:last-child .archive__item {
    border-bottom: 0;
    padding-bottom: 0;
  }

  .cv-archive-list .archive__item-title {
    margin-bottom: 0.35rem;
    font-size: 1rem;
  }

  .cv-archive-list .archive__item-excerpt,
  .cv-archive-list .page__meta {
    font-size: 0.92rem;
  }

  @media (max-width: 48em) {
    #main {
      padding-left: 0.75rem;
      padding-right: 0.75rem;
    }

    .cv-hero h2 {
      font-size: clamp(1.75rem, 8vw, 2.45rem);
    }

    .cv-pill-row,
    .cv-link-row,
    .cv-focus-grid {
      display: grid;
      grid-template-columns: 1fr;
    }

    .cv-link,
    .cv-pill {
      width: 100%;
    }
  }

  @media (min-width: 64em) {
    .sidebar {
      width: 16rem;
      margin-right: 1.5rem;
      opacity: 0.92;
    }

    .page {
      float: right;
      width: calc(100% - 17.5rem);
      margin: 0;
      padding: 0;
    }
  }
</style>

<div class="cv-page">
  <section class="cv-hero">
    <p class="cv-kicker" data-i18n="cv.hero_kicker">Academic Profile</p>
    <h2 data-i18n="cv.hero_title">A faculty CV shaped for research, teaching, and interdisciplinary impact.</h2>
    <p class="cv-lead" data-i18n-html="cv.hero_lead">I am currently an Associate Professor in the <a href="https://mathzh.sysu.edu.cn/">Department of Mathematics, Zhuhai</a> at Sun Yat-sen University. My work spans applied mathematics, interpretable machine learning, medical and scientific AI, and collaborations that connect theory with practice.</p>
    <div class="cv-pill-row">
      <span class="cv-pill" data-i18n="cv.pill1">Applied mathematics</span>
      <span class="cv-pill" data-i18n="cv.pill2">Interpretable machine learning</span>
      <span class="cv-pill" data-i18n="cv.pill3">AI for science and health</span>
    </div>
    <div class="cv-link-row">
      <a class="cv-link cv-link--accent" href="/publications/" data-i18n="cv.link_publications">Selected publications</a>
      <a class="cv-link" href="/talks/" data-i18n="cv.link_talks">Talks and presentations</a>
      <a class="cv-link" href="/about/" data-i18n="cv.link_about">About and background</a>
    </div>
  </section>

  <section class="cv-section">
    <div class="cv-section-head">
      <span class="cv-section-kicker" data-i18n="cv.education_kicker">Training</span>
      <h2 data-i18n="cv.education_heading">Education</h2>
      <p data-i18n="cv.education_desc">A mathematical foundation built across China and the United States, with training that moved from rigorous analysis toward applied and computational mathematics.</p>
    </div>
    <div class="cv-grid cv-grid--education">
      <article class="cv-card cv-card--warm">
        <span class="cv-label" data-i18n="cv.education_label_bs">Undergraduate</span>
        <h3 data-i18n="cv.education_bs_title">B.S. in Mathematics and Applied Mathematics</h3>
        <p class="cv-meta" data-i18n-html="cv.education_bs_meta"><a href="http://en.ustc.edu.cn/">University of Science and Technology of China</a>, Hefei, China</p>
        <p data-i18n="cv.education_bs_desc">Completed in 2011 with training in core mathematics and early exposure to scientific computing.</p>
      </article>
      <article class="cv-card cv-card--cool">
        <span class="cv-label" data-i18n="cv.education_label_phd">Doctoral</span>
        <h3 data-i18n="cv.education_phd_title">Ph.D. in Applied Mathematics</h3>
        <p class="cv-meta" data-i18n-html="cv.education_phd_meta"><a href="http://www.uwyo.edu/">University of Wyoming</a>, Laramie, Wyoming, USA</p>
        <p data-i18n="cv.education_phd_desc">Completed in 2016 with research on particle methods and mathematically grounded modeling.</p>
      </article>
    </div>
  </section>

  <section class="cv-section">
    <div class="cv-section-head">
      <span class="cv-section-kicker" data-i18n="cv.work_kicker">Appointments</span>
      <h2 data-i18n="cv.work_heading">Academic Positions</h2>
      <p data-i18n="cv.work_desc">Recent roles connect applied mathematics, machine learning, medical imaging, and scientific computing across research-intensive departments and interdisciplinary institutes.</p>
    </div>
    <div class="cv-timeline">
      <article class="cv-timeline-card">
        <div class="cv-timeline-top">
          <h3 data-i18n="cv.work_current_title">Associate Professor</h3>
          <span class="cv-timeline-date" data-i18n="cv.work_current_date">Current</span>
        </div>
        <p class="cv-meta" data-i18n-html="cv.work_current_org"><a href="https://mathzh.sysu.edu.cn/">Department of Mathematics, Zhuhai, Sun Yat-sen University</a></p>
        <p data-i18n="cv.work_current_desc">Research and teaching in applied mathematics, data-driven learning, and interdisciplinary artificial intelligence.</p>
      </article>
      <article class="cv-timeline-card">
        <div class="cv-timeline-top">
          <h3 data-i18n="cv.work1_title">Postdoctoral Fellow</h3>
          <span class="cv-timeline-date" data-i18n="cv.work1_date">Sep 2019 - Sep 2021</span>
        </div>
        <p class="cv-meta" data-i18n-html="cv.work1_org"><a href="https://www.utexas.edu/">The University of Texas at Austin</a></p>
        <p data-i18n="cv.work1_desc">Worked on database development, data mining, machine and deep learning, and uncertainty quantification for magnetically confined fusion.</p>
      </article>
      <article class="cv-timeline-card">
        <div class="cv-timeline-top">
          <h3 data-i18n="cv.work2_title">Postdoctoral Fellow</h3>
          <span class="cv-timeline-date" data-i18n="cv.work2_date">Sep 2017 - Jul 2019</span>
        </div>
        <p class="cv-meta" data-i18n-html="cv.work2_org"><a href="https://www.uottawa.ca/en">University of Ottawa</a></p>
        <p data-i18n-html="cv.work2_desc">Developed new machine learning and deep learning models for medical image registration and related computer vision problems in the <a href="http://mysite.science.uottawa.ca/dsml/">Data Science and Machine Learning group</a>.</p>
      </article>
      <article class="cv-timeline-card">
        <div class="cv-timeline-top">
          <h3 data-i18n="cv.work3_title">Visiting Assistant Professor</h3>
          <span class="cv-timeline-date" data-i18n="cv.work3_date">Aug 2016 - May 2017</span>
        </div>
        <p class="cv-meta" data-i18n-html="cv.work3_org"><a href="https://www.suu.edu/">Southern Utah University</a></p>
        <p data-i18n="cv.work3_desc">Taught mathematics courses and conducted interdisciplinary research during an early faculty appointment.</p>
      </article>
    </div>
  </section>

  <section class="cv-section">
    <div class="cv-section-head">
      <span class="cv-section-kicker" data-i18n="cv.focus_kicker">Focus</span>
      <h2 data-i18n="cv.focus_heading">Research and Teaching Profile</h2>
      <p data-i18n="cv.focus_desc">The work combines mathematical structure, practical learning systems, and domain knowledge from medicine, science, and engineering.</p>
    </div>
    <div class="cv-focus-grid">
      <div class="cv-focus-item">
        <strong data-i18n="cv.focus1_title">Interpretable learning</strong>
        <span data-i18n="cv.focus1_desc">Robust and explainable models for imperfect supervision, especially in EEG-based affective computing.</span>
      </div>
      <div class="cv-focus-item">
        <strong data-i18n="cv.focus2_title">Medical and scientific AI</strong>
        <span data-i18n="cv.focus2_desc">Machine learning methods informed by medical imaging, clinical use, and scientific constraints.</span>
      </div>
      <div class="cv-focus-item">
        <strong data-i18n="cv.focus3_title">Mathematical modeling</strong>
        <span data-i18n="cv.focus3_desc">Learning pipelines grounded in dynamical systems, structure-preserving ideas, and applied mathematics.</span>
      </div>
      <div class="cv-focus-item">
        <strong data-i18n="cv.focus4_title">University teaching</strong>
        <span data-i18n="cv.focus4_desc">Teaching that bridges theory, computation, and interdisciplinary applications for students in mathematics and adjacent fields.</span>
      </div>
    </div>
  </section>

  <section class="cv-archive-grid">
    <div class="cv-archive-panel">
      <div class="cv-section-head">
        <span class="cv-section-kicker" data-i18n="cv.publications_kicker">Output</span>
        <h2 data-i18n="cv.publications_heading">Publications</h2>
        <p data-i18n="cv.publications_desc">Selected research output across applied mathematics, scientific computing, machine learning, and interdisciplinary AI.</p>
      </div>
      <ul class="cv-archive-list">{% for post in site.publications %}
        {% include archive-single-cv.html %}
      {% endfor %}</ul>
    </div>

    <div class="cv-archive-panel">
      <div class="cv-section-head">
        <span class="cv-section-kicker" data-i18n="cv.talks_kicker">Exchange</span>
        <h2 data-i18n="cv.talks_heading">Talks</h2>
        <p data-i18n="cv.talks_desc">Invited talks, presentations, and research communication across academic and interdisciplinary settings.</p>
      </div>
      <ul class="cv-archive-list">{% for post in site.talks %}
        {% include archive-single-talk-cv.html %}
      {% endfor %}</ul>
    </div>

    <div class="cv-archive-panel">
      <div class="cv-section-head">
        <span class="cv-section-kicker" data-i18n="cv.teaching_kicker">Instruction</span>
        <h2 data-i18n="cv.teaching_heading">Teaching</h2>
        <p data-i18n="cv.teaching_desc">Courses and instructional work that reflect a balance of mathematical rigor, clarity, and practical relevance.</p>
      </div>
      <ul class="cv-archive-list">{% for post in site.teaching %}
        {% include archive-single-cv.html %}
      {% endfor %}</ul>
    </div>
  </section>
</div>
  
