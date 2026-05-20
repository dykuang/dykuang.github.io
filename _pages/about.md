---
permalink: /
title: "Bonjour!"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
  #main {
    max-width: min(96vw, 84rem);
  }

  .about-landing {
    --about-ink: #14313d;
    --about-muted: #546a71;
    --about-line: rgba(20, 49, 61, 0.12);
    --about-panel: rgba(255, 255, 255, 0.86);
    --about-warm: #f3e6d7;
    --about-mint: #dcebe1;
    --about-accent: #bd5a38;
    --about-accent-soft: rgba(189, 90, 56, 0.1);
    display: grid;
    gap: clamp(1.15rem, 2vw, 1.8rem);
  }

  .about-landing h2,
  .about-landing h3 {
    margin-top: 0;
  }

  .about-hero,
  .about-section,
  .about-story {
    border: 1px solid var(--about-line);
    border-radius: 24px;
    background: var(--about-panel);
    box-shadow: 0 18px 50px rgba(20, 49, 61, 0.08);
  }

  .about-hero {
    position: relative;
    overflow: hidden;
    padding: clamp(1.25rem, 2.5vw, 2rem);
    background:
      radial-gradient(circle at top right, rgba(189, 90, 56, 0.18), transparent 28%),
      radial-gradient(circle at left center, rgba(84, 132, 110, 0.14), transparent 30%),
      linear-gradient(135deg, rgba(255, 248, 240, 0.98), rgba(244, 248, 244, 0.96));
  }

  .about-kicker {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    margin: 0 0 0.9rem;
    padding: 0.4rem 0.8rem;
    border-radius: 999px;
    background: rgba(20, 49, 61, 0.08);
    color: var(--about-muted);
    font-size: 0.82rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
  }

  .about-hero-title {
    margin: 0;
    color: var(--about-ink);
    font-size: clamp(2rem, 4vw, 3.35rem);
    line-height: 1.02;
  }

  .about-lead {
    max-width: 42rem;
    margin: 1rem 0 0;
    color: var(--about-muted);
    font-size: 1.05rem;
    line-height: 1.75;
  }

  .about-cta-row,
  .about-pill-row,
  .about-link-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
  }

  .about-cta-row {
    margin-top: 1.3rem;
  }

  .about-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 42px;
    padding: 0.7rem 1rem;
    border-radius: 999px;
    border: 1px solid var(--about-line);
    background: #fff;
    color: var(--about-ink);
    font-weight: 600;
    text-decoration: none;
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
  }

  .about-link:hover {
    transform: translateY(-1px);
    border-color: rgba(20, 49, 61, 0.24);
    box-shadow: 0 10px 24px rgba(20, 49, 61, 0.1);
    text-decoration: none;
  }

  .about-link--accent {
    border-color: transparent;
    background: linear-gradient(135deg, #c86441, #a8472a);
    color: #fff;
  }

  .about-pill-row {
    margin-top: 1.4rem;
  }

  .about-pill {
    display: inline-flex;
    align-items: center;
    padding: 0.48rem 0.8rem;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.76);
    border: 1px solid var(--about-line);
    color: var(--about-muted);
    font-size: 0.92rem;
  }

  .about-section {
    padding: clamp(1.15rem, 2.2vw, 1.7rem);
  }

  .about-section-head {
    display: grid;
    gap: 0.35rem;
    margin-bottom: 1.15rem;
  }

  .about-section-kicker {
    color: var(--about-accent);
    font-size: 0.78rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    font-weight: 700;
  }

  .about-section-head p {
    margin: 0;
    color: var(--about-muted);
    line-height: 1.7;
  }

  .about-grid {
    display: grid;
    gap: clamp(0.9rem, 1.8vw, 1.15rem);
  }

  .about-grid--research {
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  }

  .about-grid--journey {
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  }

  .about-card {
    height: 100%;
    padding: 1.2rem;
    border: 1px solid var(--about-line);
    border-radius: 20px;
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.95), rgba(250, 252, 251, 0.88));
  }

  .about-card--warm {
    background: linear-gradient(180deg, rgba(243, 230, 215, 0.52), rgba(255, 255, 255, 0.92));
  }

  .about-card--mint {
    background: linear-gradient(180deg, rgba(220, 235, 225, 0.6), rgba(255, 255, 255, 0.92));
  }

  .about-card--soft {
    background: linear-gradient(180deg, rgba(232, 240, 244, 0.65), rgba(255, 255, 255, 0.94));
  }

  .about-card h3,
  .about-card h4 {
    margin-bottom: 0.55rem;
    color: var(--about-ink);
  }

  .about-card p {
    margin: 0;
    color: var(--about-muted);
    line-height: 1.68;
  }

  .about-tag {
    display: inline-flex;
    margin-bottom: 0.8rem;
    padding: 0.38rem 0.7rem;
    border-radius: 999px;
    background: var(--about-accent-soft);
    color: var(--about-accent);
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 0.03em;
  }

  .about-story {
    display: grid;
    grid-template-columns: minmax(120px, 180px) minmax(0, 1fr);
    gap: 1.1rem;
    align-items: center;
    padding: clamp(0.9rem, 1.5vw, 1rem);
  }

  .about-story-media,
  .about-story-media--split {
    display: grid;
    gap: 0.6rem;
  }

  .about-story-media img,
  .about-story-media--split img {
    width: 100%;
    border-radius: 16px;
    display: block;
    object-fit: cover;
    box-shadow: 0 10px 24px rgba(20, 49, 61, 0.12);
  }

  .about-story-media--split {
    grid-template-columns: 1fr 1fr;
  }

  .about-story-copy h3 {
    margin-bottom: 0.45rem;
  }

  .about-story-copy p {
    margin: 0;
    color: var(--about-muted);
    line-height: 1.72;
  }

  .about-quote {
    padding: 1.2rem 1.3rem;
    border-left: 4px solid var(--about-accent);
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(189, 90, 56, 0.08), rgba(255, 255, 255, 0.92));
    color: var(--about-ink);
    font-size: 1.02rem;
    line-height: 1.75;
  }

  .about-quote p:last-child,
  .about-story-copy p:last-child,
  .about-card p:last-child {
    margin-bottom: 0;
  }

  @media (max-width: 48em) {
    #main {
      padding-left: 0.75rem;
      padding-right: 0.75rem;
    }

    .about-hero-title {
      font-size: clamp(1.7rem, 8vw, 2.45rem);
    }

    .about-lead,
    .about-section-head p,
    .about-card p,
    .about-story-copy p,
    .about-quote {
      font-size: 0.98rem;
    }

    .about-story {
      grid-template-columns: 1fr;
    }

    .about-story-media--split {
      grid-template-columns: 1fr;
    }

    .about-pill-row,
    .about-cta-row,
    .about-link-row {
      display: grid;
      grid-template-columns: 1fr;
    }

    .about-link,
    .about-pill {
      width: 100%;
    }
  }

  @media (min-width: 48.0625em) and (max-width: 63.9375em) {
    #main {
      max-width: min(96vw, 72rem);
    }

    .about-pill-row,
    .about-cta-row,
    .about-link-row {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      align-items: stretch;
    }

    .about-link,
    .about-pill {
      width: 100%;
    }

    .about-grid--journey {
      grid-template-columns: 1fr;
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

    .about-grid--journey {
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    }
  }

  @media (min-width: 90em) {
    #main {
      max-width: min(94vw, 88rem);
    }
  }
</style>

<div class="about-landing">
  <section class="about-hero">
    <p class="about-kicker">Associate Professor · Sun Yat-sen University</p>
    <h2 class="about-hero-title">Mathematics, data-driven learning, and interdisciplinary AI.</h2>
    <p class="about-lead">
      Hello and welcome. I am an Associate Professor in the <a href="https://mathzh.sysu.edu.cn/">Department of Mathematics, Zhuhai</a> at Sun Yat-sen University. This site is where I collect research, talks, and selected projects across applied mathematics, machine learning, and interdisciplinary data analysis.
    </p>
    <div class="about-pill-row">
      <span class="about-pill">Interpretable machine learning</span>
      <span class="about-pill">AI for health, science, and mathematics</span>
      <span class="about-pill">Mathematical modeling and data analysis</span>
    </div>
    <div class="about-cta-row">
      <a class="about-link about-link--accent" href="/publications/">Browse publications</a>
      <a class="about-link" href="/talks/">See talks</a>
      <a class="about-link" href="/portfolio/">Explore projects</a>
      <a class="about-link" href="https://github.com/dykuang">Visit GitHub</a>
    </div>
  </section>

  <section class="about-section">
    <div class="about-section-head">
      <span class="about-section-kicker">Research directions</span>
      <h2>Main Research Interests</h2>
      <p>
        My work centers on turning theory-rich problems into practical learning systems: interpretable models, robust training under imperfect data, and AI methods shaped by scientific or mathematical structure rather than raw data alone.
      </p>
    </div>

    <div class="about-grid about-grid--research">
      <article class="about-card about-card--warm">
        <span class="about-tag">Robust learning</span>
        <h3>Interpretable models under noisy labels</h3>
        <p>
          I study robust learning strategies for affective computing from EEG data, especially when supervision is noisy and explainability matters.
        </p>
        <div class="about-link-row" style="margin-top: 1rem;">
          <a class="about-link" href="https://github.com/dykuang/BCI-Attention">BCI-Attention</a>
          <a class="about-link" href="https://github.com/dykuang/EEG-based-affective-computing">EEG affective computing</a>
          <a class="about-link" href="https://github.com/dykuang/SEER">SEER</a>
          <a class="about-link" href="https://github.com/dykuang/EEG-classification">EEG classification</a>
        </div>
      </article>

      <article class="about-card about-card--mint">
        <span class="about-tag">AI4Health</span>
        <h3>Medical data and image analysis</h3>
        <p>
          I develop AI methods for clinically meaningful problems, with an emphasis on medical images, registration, and learning from imperfect annotations.
        </p>
        <div class="about-link-row" style="margin-top: 1rem;">
          <a class="about-link" href="https://github.com/dykuang/Medical-image-registration">Medical image registration</a>
          <a class="about-link" href="https://github.com/dykuang/Unsupervised-brain-leision-segmentation">Brain lesion segmentation</a>
        </div>
      </article>

      <article class="about-card about-card--soft">
        <span class="about-tag">AI4Science</span>
        <h3>Scientific systems guided by domain knowledge</h3>
        <p>
          I am interested in machine learning pipelines that respect physics, chemistry, and other scientific constraints instead of treating every problem as a black box.
        </p>
        <div class="about-link-row" style="margin-top: 1rem;">
          <a class="about-link" href="https://github.com/dykuang/DL4EOS">DL4EOS</a>
          <a class="about-link" href="https://github.com/dykuang/Pyro-thermal-kinetic">Pyro-thermal-kinetic</a>
        </div>
      </article>

      <article class="about-card">
        <span class="about-tag">AI4Math</span>
        <h3>Learning methods that serve mathematics</h3>
        <p>
          I also explore how machine learning can support mathematical structures and dynamical systems, including work related to Koopman-inspired modeling.
        </p>
        <div class="about-link-row" style="margin-top: 1rem;">
          <a class="about-link" href="https://github.com/dykuang/Deep----Koopman">Deep Koopman</a>
        </div>
      </article>
    </div>
  </section>

  <section class="about-section">
    <div class="about-section-head">
      <span class="about-section-kicker">Why this site</span>
      <h2>A place to keep exploring</h2>
      <p>
        If you are visiting for the first time, the best entry points are my <a href="/publications/">publications</a>, <a href="/talks/">talks</a>, and code on <a href="https://github.com/dykuang">GitHub</a>. If your interests overlap with robust learning, AI for scientific or medical problems, or applied mathematics, feel free to get in touch.
      </p>
    </div>
    <div class="about-quote">
      <p>
        I am not an active blogger, but I do try to keep this site useful: a compact record of what I work on, where ideas came from, and where you can dig deeper.
      </p>
    </div>
  </section>

  <section class="about-section">
    <div class="about-section-head">
      <span class="about-section-kicker">Academic journey</span>
      <h2>From hometown curiosity to interdisciplinary research</h2>
      <p>
        The path has moved through mathematics, scientific computing, machine learning, and collaborations across health and industry. These snapshots make that progression easier to read at a glance.
      </p>
    </div>

    <div class="about-grid about-grid--journey">
      <article class="about-story">
        <div class="about-story-media">
          <img src="/images/UT.jpg" alt="Oden Institute at UT Austin">
        </div>
        <div class="about-story-copy">
          <h3>Recent postdoc at the Oden Institute</h3>
          <p>
            My most recent postdoc was at the <a href="https://www.oden.utexas.edu/">Oden Institute for Computational Engineering and Sciences</a>, supervised by <a href="https://users.oden.utexas.edu/~michoski/Michoski.html">Dr. Craig Michoski</a>. I developed data-driven and deep learning methods for interdisciplinary applications, and part of that work later evolved into solutions and services at <a href="https://sophelio.io/">Sophelio</a>.
          </p>
        </div>
      </article>

      <article class="about-story">
        <div class="about-story-media about-story-media--split">
          <img src="/images/ott.jpg" alt="University of Ottawa">
          <img src="/images/SUU.jpg" alt="Southern Utah University">
        </div>
        <div class="about-story-copy">
          <h3>Ottawa and Southern Utah</h3>
          <p>
            Before that, I was a postdoc in the <a href="http://mysite.science.uottawa.ca/dsml/">Data Science and Machine Learning group</a> at the <a href="https://science.uottawa.ca/mathstat/en">Department of Mathematics and Statistics, University of Ottawa</a>, after a year as a visiting assistant professor at <a href="https://www.suu.edu/">Southern Utah University</a>.
          </p>
        </div>
      </article>

      <article class="about-story">
        <div class="about-story-media">
          <img src="/images/UWsnow.jpg" alt="University of Wyoming campus in winter">
        </div>
        <div class="about-story-copy">
          <h3>PhD at the University of Wyoming</h3>
          <p>
            I received my PhD in Applied Mathematics from the <a href="http://www.uwyo.edu/">University of Wyoming</a>, working on particle methods for Euler-Poincare equations under <a href="http://www.uwyo.edu/llee/">Prof. Long Lee</a>. Collaborations with <a href="https://math.unc.edu/staff/camassa-roberta/">Prof. Roberto Camassa</a> helped push my interests toward data science and machine learning.
          </p>
        </div>
      </article>

      <article class="about-story">
        <div class="about-story-media">
          <img src="/images/ustc.jpg" alt="University of Science and Technology of China">
        </div>
        <div class="about-story-copy">
          <h3>Mathematics training at USTC</h3>
          <p>
            I earned my bachelor's degree in Mathematics from the <a href="http://en.ustc.edu.cn/">University of Science and Technology of China</a>, where I worked on two-dimensional integration methods with <a href="http://staff.ustc.edu.cn/~dengjs/">Prof. Jiansong Deng</a>.
          </p>
        </div>
      </article>

      <article class="about-story">
        <div class="about-story-media">
          <img src="/images/jianou.jpg" alt="Jian'ou in Fujian Province">
        </div>
        <div class="about-story-copy">
          <h3>Early inspiration in Fujian</h3>
          <p>
            I was born in a small town called <em>Jiyang</em> in Fujian Province, China. My days in <a href="http://www.fjjoyz.cn/">high school</a>, together with clubs, competitions, and inspiring teachers, shaped my broad curiosity about science and mathematics.
          </p>
        </div>
      </article>

      <article class="about-story">
        <div class="about-story-media">
          <img src="/images/jiyang.jpg" alt="Jiyang hometown">
        </div>
        <div class="about-story-copy">
          <h3>A personal note</h3>
          <p>
            My name comes from the first characters of my parents' first job locations. It is a small reminder that even under practical constraints, there is room to shape life with imagination and intention.
          </p>
        </div>
      </article>
    </div>
  </section>
</div>

