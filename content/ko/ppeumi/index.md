---
title: "쁘미"
date: 2025-10-20
type: introduce
layout: single
image:
  filename: image.jpg
  focal_point: "center"
  preview_only: false
show_author: false
css_class: ppeumi-gallery
---

### 🐶 프로필  
이름: 쁘미  
나이: 2016년 탄생  
몸무게: 2kg 미만  
품종: 말티즈  
좋아하는 것: 잠  
특징: 하루 20시간 숙면, 작음  

---

### 📸 사진첩

<div class="ppeumi-grid">
  <img src="p1.jpg" alt="쁘미 사진1" class="ppeumi-card" onclick="openModal(this)">
  <img src="p2.jpg" alt="쁘미 사진2" class="ppeumi-card" onclick="openModal(this)">
  <img src="p3.jpg" alt="쁘미 사진3" class="ppeumi-card" onclick="openModal(this)">
  <img src="p4.jpg" alt="쁘미 사진4" class="ppeumi-card" onclick="openModal(this)">
  <img src="p5.jpg" alt="쁘미 사진5" class="ppeumi-card" onclick="openModal(this)">
  <img src="p6.jpg" alt="쁘미 사진6" class="ppeumi-card" onclick="openModal(this)">
  <img src="p7.jpg" alt="쁘미 사진7" class="ppeumi-card" onclick="openModal(this)">
  <img src="p8.jpg" alt="쁘미 사진8" class="ppeumi-card" onclick="openModal(this)">
  <img src="p9.jpg" alt="쁘미 사진9" class="ppeumi-card" onclick="openModal(this)">
  <img src="/p10.jpg" alt="쁘미 사진10" class="ppeumi-card" onclick="openModal(this)">
  <img src="p11.jpg" alt="쁘미 사진11" class="ppeumi-card" onclick="openModal(this)">
  <img src="p12.jpg" alt="쁘미 사진12" class="ppeumi-card" onclick="openModal(this)">
  <img src="p13.jpg" alt="쁘미 사진13" class="ppeumi-card" onclick="openModal(this)">
  <img src="p14.jpg" alt="쁘미 사진14" class="ppeumi-card" onclick="openModal(this)">
  <img src="p15.jpg" alt="쁘미 사진15" class="ppeumi-card" onclick="openModal(this)">
</div>

<!-- 이미지 클릭 시 확대 (모달) -->
<div id="ppeumiModal" class="ppeumi-modal" onclick="closeModal()">
  <img class="ppeumi-modal-content" id="ppeumiModalImg">
</div>

<script>
function openModal(img) {
  document.getElementById("ppeumiModal").style.display = "flex";
  document.getElementById("ppeumiModalImg").src = img.src;
}
function closeModal() {
  document.getElementById("ppeumiModal").style.display = "none";
}
</script>
