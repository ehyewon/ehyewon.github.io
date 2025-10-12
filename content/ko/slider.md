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
<link rel="stylesheet" href="https://unpkg.com/swiper@10/
