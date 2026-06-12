/*!
 * i18n language toggle — English (default) / 中文
 * Usage: add data-i18n="key" to any element whose textContent you want swapped.
 * For attributes: data-i18n-attr="attribute:key"
 * For HTML:       data-i18n-html="key"
 * Nav links read data-nav-en / data-nav-zh attributes set by Jekyll.
 */

(function () {
  'use strict';

  var LANG_KEY = 'site-lang';
  var currentLang = localStorage.getItem(LANG_KEY) || 'en';

  /* ================================================================
   *  Translation dictionaries
   *  ================================================================ */
  var dict = {
    /* ---- shared UI ---- */
    'follow':       { en: 'Follow',       zh: '关注' },
    'sitemap':      { en: 'Sitemap',      zh: '网站地图' },
    'search_placeholder': { en: 'Search', zh: '搜索' },

    /* ---- navigation (fallback, nav preferred via data attributes) ---- */
    'nav.cv':           { en: 'CV',           zh: '简历' },
    'nav.blog':         { en: 'Blog Posts',   zh: '博客文章' },
    'nav.publications': { en: 'Publications', zh: '论文发表' },
    'nav.galleries':    { en: 'Galleries',    zh: '项目展示' },
    'nav.talks':        { en: 'Talks',        zh: '学术报告' },
    'nav.teaching':     { en: 'Teaching',     zh: '教学' },

    /* ---- about page ---- */
    'about.kicker':               { en: 'Associate Professor \u00b7 Sun Yat-sen University', zh: '副教授 \u00b7 中山大学' },
    'about.hero_title':           { en: 'Mathematics, data-driven learning, and interdisciplinary AI.', zh: '数学、数据驱动学习与跨学科人工智能。' },
    'about.lead':                 { en: 'Hello and welcome. I am an Associate Professor in the <a href="https://mathzh.sysu.edu.cn/">Department of Mathematics, Zhuhai</a> at Sun Yat-sen University. This site is where I collect research, talks, and selected projects across applied mathematics, machine learning, and interdisciplinary data analysis.', zh: '欢迎来访。我是中山大学<a href="https://mathzh.sysu.edu.cn/">数学学院（珠海）</a>的副教授。本站汇集了我在应用数学、机器学习和跨学科数据分析方面的研究、报告与精选项目。' },
    'about.pill1':                { en: 'Interpretable machine learning', zh: '可解释机器学习' },
    'about.pill2':                { en: 'AI for health, science, and mathematics', zh: '面向健康、科学与数学的AI' },
    'about.pill3':                { en: 'Mathematical modeling and data analysis', zh: '数学建模与数据分析' },
    'about.cta_publications':     { en: 'Browse publications', zh: '浏览论文' },
    'about.cta_talks':            { en: 'See talks', zh: '查看报告' },
    'about.cta_projects':         { en: 'Explore projects', zh: '探索项目' },
    'about.cta_github':           { en: 'Visit GitHub', zh: '访问GitHub' },

    'about.research.kicker':      { en: 'Research directions', zh: '研究方向' },
    'about.research.heading':     { en: 'Main Research Interests', zh: '主要研究方向' },
    'about.research.desc':        { en: 'My work centers on turning theory-rich problems into practical learning systems: interpretable models, robust training under imperfect data, and AI methods shaped by scientific or mathematical structure rather than raw data alone.', zh: '我的工作致力于将理论深厚的问题转化为实用的学习系统：可解释模型、不完美数据下的鲁棒训练，以及受科学或数学结构启发（而非仅依赖原始数据）的AI方法。' },

    'about.card1.tag':            { en: 'Robust learning', zh: '鲁棒学习' },
    'about.card1.title':          { en: 'Interpretable models under noisy labels', zh: '噪声标签下的可解释模型' },
    'about.card1.desc':           { en: 'I study robust learning strategies for affective computing from EEG data, especially when supervision is noisy and explainability matters.', zh: '我研究基于脑电数据的情感计算鲁棒学习策略，特别关注监督信息存在噪声且可解释性至关重要的场景。' },

    'about.card2.tag':            { en: 'AI4Health', zh: 'AI for Health（智慧医疗）' },
    'about.card2.title':          { en: 'Medical data and image analysis', zh: '医学数据与图像分析' },
    'about.card2.desc':           { en: 'I develop AI methods for clinically meaningful problems, with an emphasis on medical images, registration, and learning from imperfect annotations.', zh: '我开发面向临床问题的AI方法，重点关注医学图像、配准以及从不完美标注中学习。' },

    'about.card3.tag':            { en: 'AI4Science', zh: 'AI for Science（科学智能）' },
    'about.card3.title':          { en: 'Scientific systems guided by domain knowledge', zh: '领域知识驱动的科学系统' },
    'about.card3.desc':           { en: 'I am interested in machine learning pipelines that respect physics, chemistry, and other scientific constraints instead of treating every problem as a black box.', zh: '我关注尊重物理、化学及其他科学约束的机器学习流程，而非将所有问题视为黑箱。' },

    'about.card4.tag':            { en: 'AI4Math', zh: 'AI for Math（数学智能）' },
    'about.card4.title':          { en: 'Learning methods that serve mathematics', zh: '服务数学的学习方法' },
    'about.card4.desc':           { en: 'I also explore how machine learning can support mathematical structures and dynamical systems, including work related to Koopman-inspired modeling.', zh: '我也探索机器学习如何支持数学结构与动力系统，包括与Koopman启发的建模相关工作。' },

    'about.why.kicker':           { en: 'Why this site', zh: '关于本站' },
    'about.why.heading':          { en: 'A place to keep exploring', zh: '一个持续探索的空间' },
    'about.why.desc':             { en: 'If you are visiting for the first time, the best entry points are my <a href="/publications/">publications</a>, <a href="/talks/">talks</a>, and code on <a href="https://github.com/dykuang">GitHub</a>. If your interests overlap with robust learning, AI for scientific or medical problems, or applied mathematics, feel free to get in touch.', zh: '如果你是首次来访，最佳入口是我的<a href="/publications/">论文发表</a>、<a href="/talks/">学术报告</a>以及<a href="https://github.com/dykuang">GitHub</a>上的代码。如果你的兴趣涉及鲁棒学习、面向科学或医学问题的AI，或应用数学，欢迎联系。' },
    'about.quote':                { en: 'I am not an active blogger, but I do try to keep this site useful: a compact record of what I work on, where ideas came from, and where you can dig deeper.', zh: '我并非活跃的博主，但我努力让本站保持实用：记录我在做什么、想法从何而来、以及你可以深入探索的方向。' },

    'about.journey.kicker':       { en: 'Academic journey', zh: '学术历程' },
    'about.journey.heading':      { en: 'From hometown curiosity to interdisciplinary research', zh: '从家乡的好奇心到跨学科研究' },
    'about.journey.desc':         { en: 'The path has moved through mathematics, scientific computing, machine learning, and collaborations across health and industry. These snapshots make that progression easier to read at a glance.', zh: '这条道路贯穿了数学、科学计算、机器学习，以及与健康和工业界的合作。以下片段让这一历程一目了然。' },

    'about.journey1.title':       { en: 'Recent postdoc at the Oden Institute', zh: 'Oden研究所博士后' },
    'about.journey1.desc':        { en: 'My most recent postdoc was at the <a href="https://www.oden.utexas.edu/">Oden Institute for Computational Engineering and Sciences</a>, supervised by <a href="https://users.oden.utexas.edu/~michoski/Michoski.html">Dr. Craig Michoski</a>. I developed data-driven and deep learning methods for interdisciplinary applications, and part of that work later evolved into solutions and services at <a href="https://sophelio.io/">Sophelio</a>.', zh: '我最近的博士后工作是在<a href="https://www.oden.utexas.edu/">Oden计算工程与科学研究所</a>，导师为<a href="https://users.oden.utexas.edu/~michoski/Michoski.html">Craig Michoski博士</a>。我为跨学科应用开发了数据驱动和深度学习方法，部分工作后来发展为<a href="https://sophelio.io/">Sophelio</a>的解决方案与服务。' },

    'about.journey2.title':       { en: 'Ottawa and Southern Utah', zh: '渥太华与南犹他' },
    'about.journey2.desc':        { en: 'Before that, I was a postdoc in the <a href="http://mysite.science.uottawa.ca/dsml/">Data Science and Machine Learning group</a> at the <a href="https://science.uottawa.ca/mathstat/en">Department of Mathematics and Statistics, University of Ottawa</a>, after a year as a visiting assistant professor at <a href="https://www.suu.edu/">Southern Utah University</a>.', zh: '在此之前，我在渥太华大学<a href="https://science.uottawa.ca/mathstat/en">数学与统计系</a>的<a href="http://mysite.science.uottawa.ca/dsml/">数据科学与机器学习小组</a>从事博士后研究，此前在<a href="https://www.suu.edu/">南犹他大学</a>担任了一年访问助理教授。' },

    'about.journey3.title':       { en: 'PhD at the University of Wyoming', zh: '怀俄明大学博士' },
    'about.journey3.desc':        { en: 'I received my PhD in Applied Mathematics from the <a href="http://www.uwyo.edu/">University of Wyoming</a>, working on particle methods for Euler-Poincare equations under <a href="http://www.uwyo.edu/llee/">Prof. Long Lee</a>. Collaborations with <a href="https://math.unc.edu/staff/camassa-roberta/">Prof. Roberto Camassa</a> helped push my interests toward data science and machine learning.', zh: '我在<a href="http://www.uwyo.edu/">怀俄明大学</a>获得应用数学博士学位，在<a href="http://www.uwyo.edu/llee/">Long Lee教授</a>指导下研究Euler-Poincare方程的粒子方法。与<a href="https://math.unc.edu/staff/camassa-roberta/">Roberto Camassa教授</a>的合作推动了我的兴趣转向数据科学与机器学习。' },

    'about.journey4.title':       { en: 'Mathematics training at USTC', zh: '中国科学技术大学数学训练' },
    'about.journey4.desc':        { en: 'I earned my bachelor\'s degree in Mathematics from the <a href="http://en.ustc.edu.cn/">University of Science and Technology of China</a>, where I worked on two-dimensional integration methods with <a href="http://staff.ustc.edu.cn/~dengjs/">Prof. Jiansong Deng</a>.', zh: '我在<a href="http://en.ustc.edu.cn/">中国科学技术大学</a>获得数学学士学位，期间在<a href="http://staff.ustc.edu.cn/~dengjs/">邓建松教授</a>指导下研究二维积分方法。' },

    'about.journey5.title':       { en: 'Early inspiration in Fujian', zh: '福建的早期启蒙' },
    'about.journey5.desc':        { en: 'I was born in a small town called <em>Jiyang</em> in Fujian Province, China. My days in <a href="http://www.fjjoyz.cn/">high school</a>, together with clubs, competitions, and inspiring teachers, shaped my broad curiosity about science and mathematics.', zh: '我出生在福建省一个叫<em>吉阳</em>的小镇。<a href="http://www.fjjoyz.cn/">高中</a>时光、社团活动、竞赛以及启迪人心的老师，塑造了我对科学与数学的广泛好奇心。' },

    'about.journey6.title':       { en: 'A personal note', zh: '一点个人说明' },
    'about.journey6.desc':        { en: 'My name comes from the first characters of my parents\' first job locations. It is a small reminder that even under practical constraints, there is room to shape life with imagination and intention.', zh: '我的名字来源于父母第一份工作地点的首字。这是一个小小的提醒：即使在现实约束之下，仍有空间用想象力与心意塑造生活。' },

    /* ---- CV page ---- */
    'cv.hero_kicker':             { en: 'Academic Profile', zh: '学术履历' },
    'cv.hero_title':              { en: 'A faculty CV shaped for research, teaching, and interdisciplinary impact.', zh: '面向科研、教学与跨学科影响力的教师履历。' },
    'cv.hero_lead':               { en: 'I am currently an Associate Professor in the <a href="https://mathzh.sysu.edu.cn/">Department of Mathematics, Zhuhai</a> at Sun Yat-sen University. My work spans applied mathematics, interpretable machine learning, medical and scientific AI, and collaborations that connect theory with practice.', zh: '我现任中山大学<a href="https://mathzh.sysu.edu.cn/">数学学院（珠海）</a>副教授。我的工作涵盖应用数学、可解释机器学习、医学与科学智能，以及连接理论与实践的跨学科合作。' },
    'cv.pill1':                   { en: 'Applied mathematics', zh: '应用数学' },
    'cv.pill2':                   { en: 'Interpretable machine learning', zh: '可解释机器学习' },
    'cv.pill3':                   { en: 'AI for science and health', zh: '面向科学与健康的人工智能' },
    'cv.link_publications':       { en: 'Selected publications', zh: '代表性论文' },
    'cv.link_talks':              { en: 'Talks and presentations', zh: '报告与演讲' },
    'cv.link_about':              { en: 'About and background', zh: '背景介绍' },
    'cv.education_kicker':        { en: 'Training', zh: '学习经历' },
    'cv.education_heading':       { en: 'Education', zh: '教育背景' },
    'cv.education_desc':          { en: 'A mathematical foundation built across China and the United States, with training that moved from rigorous analysis toward applied and computational mathematics.', zh: '数学训练横跨中国与美国，从严格的理论分析逐步延伸到应用数学与计算方法。' },
    'cv.education_label_bs':      { en: 'Undergraduate', zh: '本科' },
    'cv.education_bs_title':      { en: 'B.S. in Mathematics and Applied Mathematics', zh: '数学与应用数学 理学学士' },
    'cv.education_bs_meta':       { en: '<a href="http://en.ustc.edu.cn/">University of Science and Technology of China</a>, Hefei, China', zh: '<a href="http://en.ustc.edu.cn/">中国科学技术大学</a>，中国合肥' },
    'cv.education_bs_desc':       { en: 'Completed in 2011 with training in core mathematics and early exposure to scientific computing.', zh: '2011年毕业，接受了系统的数学基础训练，并较早接触科学计算。' },
    'cv.education_label_phd':     { en: 'Doctoral', zh: '博士' },
    'cv.education_phd_title':     { en: 'Ph.D. in Applied Mathematics', zh: '应用数学 博士' },
    'cv.education_phd_meta':      { en: '<a href="http://www.uwyo.edu/">University of Wyoming</a>, Laramie, Wyoming, USA', zh: '<a href="http://www.uwyo.edu/">怀俄明大学</a>，美国怀俄明州拉勒米' },
    'cv.education_phd_desc':      { en: 'Completed in 2016 with research on particle methods and mathematically grounded modeling.', zh: '2016年毕业，研究方向为粒子方法与具有数学基础的建模方法。' },
    'cv.work_kicker':             { en: 'Appointments', zh: '任职经历' },
    'cv.work_heading':            { en: 'Academic Positions', zh: '学术职位' },
    'cv.work_desc':               { en: 'Recent roles connect applied mathematics, machine learning, medical imaging, and scientific computing across research-intensive departments and interdisciplinary institutes.', zh: '近年的任职经历贯穿应用数学、机器学习、医学影像与科学计算，覆盖研究型院系与跨学科研究机构。' },
    'cv.work_current_title':      { en: 'Associate Professor', zh: '副教授' },
    'cv.work_current_date':       { en: 'Current', zh: '现任' },
    'cv.work_current_org':        { en: '<a href="https://mathzh.sysu.edu.cn/">Department of Mathematics, Zhuhai, Sun Yat-sen University</a>', zh: '<a href="https://mathzh.sysu.edu.cn/">中山大学数学学院（珠海）</a>' },
    'cv.work_current_desc':       { en: 'Research and teaching in applied mathematics, data-driven learning, and interdisciplinary artificial intelligence.', zh: '从事应用数学、数据驱动学习与跨学科人工智能方向的科研与教学工作。' },
    'cv.work1_title':             { en: 'Postdoctoral Fellow', zh: '博士后研究员' },
    'cv.work1_date':              { en: 'Sep 2019 - Sep 2021', zh: '2019年9月 - 2021年9月' },
    'cv.work1_org':               { en: '<a href="https://www.utexas.edu/">The University of Texas at Austin</a>', zh: '<a href="https://www.utexas.edu/">得克萨斯大学奥斯汀分校</a>' },
    'cv.work1_desc':              { en: 'Worked on database development, data mining, machine and deep learning, and uncertainty quantification for magnetically confined fusion.', zh: '从事面向磁约束聚变的数据库开发、数据挖掘、机器与深度学习，以及不确定性量化研究。' },
    'cv.work2_title':             { en: 'Postdoctoral Fellow', zh: '博士后研究员' },
    'cv.work2_date':              { en: 'Sep 2017 - Jul 2019', zh: '2017年9月 - 2019年7月' },
    'cv.work2_org':               { en: '<a href="https://www.uottawa.ca/en">University of Ottawa</a>', zh: '<a href="https://www.uottawa.ca/en">渥太华大学</a>' },
    'cv.work2_desc':              { en: 'Developed new machine learning and deep learning models for medical image registration and related computer vision problems in the <a href="http://mysite.science.uottawa.ca/dsml/">Data Science and Machine Learning group</a>.', zh: '在<a href="http://mysite.science.uottawa.ca/dsml/">数据科学与机器学习小组</a>开展医学图像配准及相关计算机视觉问题的机器学习与深度学习模型研究。' },
    'cv.work3_title':             { en: 'Visiting Assistant Professor', zh: '访问助理教授' },
    'cv.work3_date':              { en: 'Aug 2016 - May 2017', zh: '2016年8月 - 2017年5月' },
    'cv.work3_org':               { en: '<a href="https://www.suu.edu/">Southern Utah University</a>', zh: '<a href="https://www.suu.edu/">南犹他大学</a>' },
    'cv.work3_desc':              { en: 'Taught mathematics courses and conducted interdisciplinary research during an early faculty appointment.', zh: '在早期教职阶段承担数学课程教学，并开展跨学科研究。' },
    'cv.focus_kicker':            { en: 'Focus', zh: '研究与教学重点' },
    'cv.focus_heading':           { en: 'Research and Teaching Profile', zh: '研究与教学概况' },
    'cv.focus_desc':              { en: 'The work combines mathematical structure, practical learning systems, and domain knowledge from medicine, science, and engineering.', zh: '研究工作结合数学结构、实用学习系统，以及来自医学、科学与工程领域的知识。' },
    'cv.focus1_title':            { en: 'Interpretable learning', zh: '可解释学习' },
    'cv.focus1_desc':             { en: 'Robust and explainable models for imperfect supervision, especially in EEG-based affective computing.', zh: '面向不完美监督的鲁棒可解释模型，尤其关注基于脑电的情感计算。' },
    'cv.focus2_title':            { en: 'Medical and scientific AI', zh: '医学与科学智能' },
    'cv.focus2_desc':             { en: 'Machine learning methods informed by medical imaging, clinical use, and scientific constraints.', zh: '结合医学影像、临床需求与科学约束的机器学习方法。' },
    'cv.focus3_title':            { en: 'Mathematical modeling', zh: '数学建模' },
    'cv.focus3_desc':             { en: 'Learning pipelines grounded in dynamical systems, structure-preserving ideas, and applied mathematics.', zh: '基于动力系统、结构保持思想与应用数学的学习流程。' },
    'cv.focus4_title':            { en: 'University teaching', zh: '大学教学' },
    'cv.focus4_desc':             { en: 'Teaching that bridges theory, computation, and interdisciplinary applications for students in mathematics and adjacent fields.', zh: '面向数学及相关领域学生，连接理论、计算与跨学科应用的教学工作。' },
    'cv.publications_kicker':     { en: 'Output', zh: '科研产出' },
    'cv.publications_heading':    { en: 'Publications', zh: '论文发表' },
    'cv.publications_desc':       { en: 'Selected research output across applied mathematics, scientific computing, machine learning, and interdisciplinary AI.', zh: '涵盖应用数学、科学计算、机器学习与跨学科人工智能的研究成果。' },
    'cv.talks_kicker':            { en: 'Exchange', zh: '学术交流' },
    'cv.talks_heading':           { en: 'Talks', zh: '学术报告' },
    'cv.talks_desc':              { en: 'Invited talks, presentations, and research communication across academic and interdisciplinary settings.', zh: '在学术与跨学科场景中的邀请报告、演讲与研究交流。' },
    'cv.teaching_kicker':         { en: 'Instruction', zh: '教学工作' },
    'cv.teaching_heading':        { en: 'Teaching', zh: '教学' },
    'cv.teaching_desc':           { en: 'Courses and instructional work that reflect a balance of mathematical rigor, clarity, and practical relevance.', zh: '兼顾数学严谨性、表达清晰度与实践相关性的课程与教学工作。' },

    /* ---- author sidebar ---- */
    'author.follow_btn':          { en: 'Follow', zh: '关注' }
  };

  /* ================================================================
   *  Helpers
   *  ================================================================ */
  function t(key) {
    var entry = dict[key];
    if (!entry) {
      console.warn('[i18n] missing key:', key);
      return key;
    }
    return entry[currentLang] || entry.en || key;
  }

  /* translate a single element */
  function translateElement(el) {
    /* data-i18n → textContent */
    var key = el.getAttribute('data-i18n');
    if (key) {
      el.textContent = t(key);
    }

    /* data-i18n-html → innerHTML (use sparingly) */
    var htmlKey = el.getAttribute('data-i18n-html');
    if (htmlKey) {
      el.innerHTML = t(htmlKey);
    }

    /* data-i18n-attr="attrName:key" → setAttribute */
    var attrVal = el.getAttribute('data-i18n-attr');
    if (attrVal) {
      var parts = attrVal.split(':');
      if (parts.length >= 2) {
        var attrName = parts[0];
        var attrKey = parts.slice(1).join(':');
        el.setAttribute(attrName, t(attrKey));
      }
    }

    /* data-i18n-nav → handle navigation links: data-nav-en / data-nav-zh */
    if (el.hasAttribute('data-nav-en') && el.hasAttribute('data-nav-zh')) {
      el.textContent = currentLang === 'zh' ? el.getAttribute('data-nav-zh') : el.getAttribute('data-nav-en');
    }

    /* data-i18n-placeholder → placeholder */
    var phKey = el.getAttribute('data-i18n-placeholder');
    if (phKey) {
      el.setAttribute('placeholder', t(phKey));
    }
  }

  /* translate the whole page */
  function translatePage() {
    var elements = document.querySelectorAll('[data-i18n], [data-i18n-html], [data-i18n-attr], [data-i18n-nav], [data-i18n-placeholder]');
    for (var i = 0; i < elements.length; i++) {
      translateElement(elements[i]);
    }

    /* set html lang attribute */
    document.documentElement.lang = currentLang === 'zh' ? 'zh-CN' : 'en-US';
    document.documentElement.classList.toggle('lang-zh', currentLang === 'zh');
    document.documentElement.classList.toggle('lang-en', currentLang === 'en');
  }

  /* ================================================================
   *  Toggle button logic
   *  ================================================================ */
  function updateToggleButton() {
    var btn = document.getElementById('lang-toggle-btn');
    if (!btn) return;
    var enOpt = btn.querySelector('.lang-opt--en');
    var zhOpt = btn.querySelector('.lang-opt--zh');
    if (enOpt && zhOpt) {
      if (currentLang === 'zh') {
        enOpt.classList.remove('lang-opt--active');
        zhOpt.classList.add('lang-opt--active');
      } else {
        zhOpt.classList.remove('lang-opt--active');
        enOpt.classList.add('lang-opt--active');
      }
    }
    btn.setAttribute('aria-label', currentLang === 'zh' ? 'Switch to English' : '切换到中文');
  }

  function toggleLanguage() {
    currentLang = currentLang === 'zh' ? 'en' : 'zh';
    localStorage.setItem(LANG_KEY, currentLang);
    translatePage();
    updateToggleButton();
  }

  /* ================================================================
   *  Init
   *  ================================================================ */
  function init() {
    translatePage();
    updateToggleButton();

    var btn = document.getElementById('lang-toggle-btn');
    if (btn) {
      btn.addEventListener('click', toggleLanguage);
    }
  }

  /* wait for DOM */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
