---
widget: blank
headless: true
active: true
weight: 5
title: ""
---

<!-- =============================
     이미지 슬라이더 (Swiper 기반)
     ============================= -->

<!-- ✅ 임시 hover 스타일 (필요 없으면 삭제 가능) -->
<style>
  a:hover, button:hover, .btn:hover, .btn-primary:hover, .btn-slide:hover {
    transform: translateY(-2px) scale(1.04) !important;
    box-shadow: 0 12px 32px rgba(0,0,0,.2) !important;
    transition: transform .12s ease, box-shadow .12s ease !important;
  }
  [class*="card"]:hover,
  .article-card:hover,
  .project-card:hover,
  .publication-card:hover {
    transform: translateY(-6px) !important;
    box-shadow: 0 16px 40px rgba(0,0,0,.18) !important;
  }
</style>

<!-- ✅ 메뉴 hover 효과 -->
<style>
header .navbar .nav-link {
  transition: color .15s ease, background-color .15s ease, box-shadow .15s ease;
}
header .navbar .nav-link:hover {
  color: #ff6b00 !important;
  background: rgba(255, 107, 0, .12) !important;
  border-radius: .5rem;
  box-shadow: 0 4px 14px rgba(0,0,0,.08);
}
header .navbar .nav-link.active,
header .navbar .nav-link[aria-current="page"] {
  color: #ff6b00 !important;
}
header .navbar .nav-link:focus-visible {
  outline: 2px solid #ff6b00 !important;
  outline-offset: 2px;
  border-radius: .5rem;
}
.dark header .navbar .nav-link:hover,
[data-theme="dark"] header .navbar .nav-link:hover {
  color: #ffd166 !important;
  background: rgba(255, 209, 102, .12) !important;
  box-shadow: 0 4px 14px rgba(0,0,0,.25);
}
header .navbar .navbar-nav .nav-link:hover {
  color: #ff6b00 !important;
}
</style>

<!-- ✅ Swiper 스타일 -->
<link rel="stylesheet" href="https://unpkg.com/swiper@10/swiper-bundle.min.css"/>

<!-- ✅ 슬라이더 섹션 -->
<section class="slider-section">
  <div class="swiper">
    <div class="swiper-wrapper">

      <div class="swiper-slide">
        <img src="/media/slide1.jpg" alt="AI Game Development" class="slide-img">
        <div class="slide-caption">
          <h3>AI Game Development</h3>
        </div>
      </div>

      <div class="swiper-slide">
        <img src="/media/slide-2.jpg" alt="AI Image Generation" class="slide-img">
        <div class="slide-caption">
          <h3>AI Image Generation</h3>
        </div>
      </div>

      <div class="swiper-slide">
        <img src="/media/slide-3.jpg" alt="Fake Review Detection" class="slide-img">
        <div class="slide-caption">
          <h3>Fake Review Detection</h3>
        </div>
      </div>

      <div class="swiper-slide">
        <img src="/media/slide-4.jpg" alt="Data" class="slide-img">
        <div class="slide-caption">
          <h3>Data</h3>
        </div>
      </div>

    </div>

    <!-- 좌우 네비게이션 + 페이지네이션 -->
    <div class="swiper-button-prev"></div>
    <div class="swiper-button-next"></div>
    <div class="swiper-pagination"></div>
  </div>
</section>

<!-- ✅ 스타일 정의 -->
<style>
.slider-section{
  position: relative;
  width: 100vw;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  background-color: #000;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}
.slider-section .swiper{
  width: 70%;
  aspect-ratio: 16/9;
  background: #111;
  display: flex;
  justify-content: center;
  align-items: center;
}
.slider-section .swiper-slide{
  display: flex;
  justify-content: center;
  align-items: center;
  background: #000;
}
.slider-section .slide-img{
  max-width: 100%;
  max-height: 100%;
  width: auto;
  height: 100%;
  object-fit: contain;
  display: block;
  margin: 0 auto;
  background-color: #000;
}
.slider-section .slide-caption{
  position: absolute;
  left: 50%;
  bottom: 8%;
  transform: translateX(-50%);
  background: rgba(0,0,0,0.55);
  padding: 1rem 1.25rem;
  border-radius: 10px;
  color: white;
  text-align: center;
}
.slider-section .slide-caption h3{
  margin: 0;
  font-size: 1.5rem;
}
.slider-section .btn-slide{
  display: inline-block;
  margin-top: 10px;
  background: #4ea1f3;
  color: white;
  padding: 6px 14px;
  border-radius: 6px;
  text-decoration: none;
  font-size: .9rem;
}
.slider-section .btn-slide:hover{ background: #1f78d1; }
.slider-section .swiper{ --swiper-navigation-size: 18px; }
.slider-section .swiper-button-prev,
.slider-section .swiper-button-next{
  width: 34px; height: 34px;
  background: rgba(0,0,0,0.35);
  border-radius: 50%;
  color: white;
  transition: background .2s;
}
.slider-section .swiper-button-prev:hover,
.slider-section .swiper-button-next:hover{
  background: rgba(0,0,0,0.65);
}
.slider-section .swiper-pagination-bullet{
  width: 7px; height: 7px;
  background: #ccc;
  opacity: .9;
}
.slider-section .swiper-pagination-bullet-active{ background: #fff; }
@media (max-width: 640px){
  .slider-section .swiper{ width: 95%; aspect-ratio: 4/3; }
  .slider-section .slide-caption{ font-size:.85rem; bottom:6%; padding:.7rem 1rem; }
}
</style>

<!-- ✅ Swiper JS -->
<script src="https://unpkg.com/swiper@10/swiper-bundle.min.js"></script>
<script>
document.addEventListener("DOMContentLoaded", function() {
  new Swiper(".swiper", {
    loop: true,
    autoplay: { delay: 3000, disableOnInteraction: false },
    pagination: { el: ".swiper-pagination", clickable: true },
    navigation: { nextEl: ".swiper-button-next", prevEl: ".swiper-button-prev" },
    effect: "slide",
    speed: 700
  });
});
</script>
