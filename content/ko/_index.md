---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  spacing: '6rem'

sections:
  - block: resume-biography-3
    content:
      username: admin
      text: ""
      button:
        text: 이력서 다운받기
        url: uploads/resume.pdf
    design:
      css_class: dark
      background:
        color: black
        image:
          filename: stacked-peaks.svg
          filters:
            brightness: 1.0
          size: cover
          position: center
          parallax: false
      avatar:
        size: medium
        shape: circle

  - block: markdown
    content:
      title: '📚 Introduce'
      subtitle: ''
      text: |-
        안녕하세요. 웹 개발자를 희망하는 이혜원입니다.  
        이 공간은 저를 소개하는 공간입니다.  
        해당 사이트에서는 저의 기본적인 개인정보 외에도  
        제가 했던 프로젝트와 최근 트렌드 소식까지 만나보실 수 있습니다.  
        편하게 둘러보세요!
    design:
      columns: '1'

  - block: collection
    id: papers
    content:
      title: 관심사
      filters:
        folders:
          - interest
    design:
      view: article-grid 
      columns: 3

  - block: collection
    content:
      title: 뉴스
      filters:
        folders:
          - news     
    design:
      view: article-grid
      columns: 4
          
  - block: collection
    id: jbnu
    content:
      title: 전북대
      count: 5
      filters:
        folders: 
          - jbnu
      offset: 0
      order: desc
    design:
      view: card
      spacing:
        padding: [0, 0, 0, 0]

  - block: cta-card
    demo: false
    content:
      title: 🚀 저의 프로젝트가 궁금하시다면?
      text: |-
        지금까지 작업한 저의 여러 프로젝트들을 포트폴리오에서 만나보실 수 있습니다. 
      button:
        text: 클릭!
        url: projects/
    design:
      card:
        css_class: ""
        css_style: ""
---

---
title: ''
date: 2022-10-24
type: landing
---

<!-- 🎞 직접 넣은 이미지 슬라이드 -->
<div class="slider">
  <div class="slides">
    <div class="slide active">
      <img src="/images/slider1.jpg" alt="슬라이드1">
      <div class="caption">👋 Welcome to My Portfolio</div>
    </div>
    <div class="slide">
      <img src="/images/slider2.jpg" alt="슬라이드2">
      <div class="caption">💡 AI Lunch Menu Recommender</div>
    </div>
    <div class="slide">
      <img src="/images/slider3.jpg" alt="슬라이드3">
      <div class="caption">🧮 Linux Calculator Project</div>
    </div>
    <div class="slide">
      <img src="/images/slider4.jpg" alt="슬라이드4">
      <div class="caption">🌐 Web Publishing & Data Visualization</div>
    </div>
  </div>

  <div class="controls">
    <span class="prev">&#10094;</span>
    <span class="next">&#10095;</span>
  </div>

  <div class="dots">
    <span class="dot active"></span>
    <span class="dot"></span>
    <span class="dot"></span>
    <span class="dot"></span>
  </div>
</div>

<style>
.slider {
  position: relative;
  max-width: 900px;
  margin: 50px auto;
  overflow: hidden;
  border-radius: 20px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}
.slides {
  display: flex;
  transition: transform 0.7s ease-in-out;
}
.slide {
  min-width: 100%;
  position: relative;
  display: none;
}
.slide.active {
  display: block;
}
.slide img {
  width: 100%;
  height: auto;
  display: block;
}
.caption {
  position: absolute;
  bottom: 30px;
  left: 40px;
  font-size: 1.4rem;
  color: white;
  text-shadow: 2px 2px 6px rgba(0,0,0,0.7);
}
.controls span {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  font-size: 2rem;
  color: white;
  cursor: pointer;
  padding: 10px;
  user-select: none;
  transition: opacity 0.2s;
}
.controls span:hover {
  opacity: 0.7;
}
.prev { left: 15px; }
.next { right: 15px; }
.dots {
  position: absolute;
  bottom: 10px;
  width: 100%;
  text-align: center;
}
.dot {
  height: 12px;
  width: 12px;
  margin: 0 4px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  cursor: pointer;
}
.dot.active {
  background-color: white;
}
</style>

<script>
document.addEventListener("DOMContentLoaded", function() {
  const slides = document.querySelectorAll('.slide');
  const dots = document.querySelectorAll('.dot');
  let index = 0;

  function showSlide(n) {
    slides.forEach(s => s.classList.remove('active'));
    dots.forEach(d => d.classList.remove('active'));
    slides[n].classList.add('active');
    dots[n].classList.add('active');
  }

  document.querySelector('.next').addEventListener('click', () => {
    index = (index + 1) % slides.length;
    showSlide(index);
  });

  document.querySelector('.prev').addEventListener('click', () => {
    index = (index - 1 + slides.length) % slides.length;
    showSlide(index);
  });

  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
      index = i;
      showSlide(index);
    });
  });

  setInterval(() => {
    index = (index + 1) % slides.length;
    showSlide(index);
  }, 4000);
});
</script>

