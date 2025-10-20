---
title: "Ppeumi"
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

### 🐶 Profile  
Name: Ppeumi  
Born: 2016
gender: ♀
Weight: Under 2kg  
Breed: Maltese  
Likes: Sleeping  
Features: Sleeps about 20 hours a day, tiny and adorable, very cute

---

### 📸 Photo Gallery

<div class="ppeumi-grid">
  <img src="p1.jpg" alt="Ppemi Photo 1" class="ppeumi-card" onclick="openModal(this)">
  <img src="p2.jpg" alt="Ppemi Photo 2" class="ppeumi-card" onclick="openModal(this)">
  <img src="p3.jpg" alt="Ppemi Photo 3" class="ppeumi-card" onclick="openModal(this)">
  <img src="p4.jpg" alt="Ppemi Photo 4" class="ppeumi-card" onclick="openModal(this)">
  <img src="p5.jpg" alt="Ppemi Photo 5" class="ppeumi-card" onclick="openModal(this)">
  <img src="p6.jpg" alt="Ppemi Photo 6" class="ppeumi-card" onclick="openModal(this)">
  <img src="p7.jpg" alt="Ppemi Photo 7" class="ppeumi-card" onclick="openModal(this)">
  <img src="p8.jpg" alt="Ppemi Photo 8" class="ppeumi-card" onclick="openModal(this)">
  <img src="p9.jpg" alt="Ppemi Photo 9" class="ppeumi-card" onclick="openModal(this)">
  <img src="p10.jpg" alt="Ppemi Photo 10" class="ppeumi-card" onclick="openModal(this)">
  <img src="p11.jpg" alt="Ppemi Photo 11" class="ppeumi-card" onclick="openModal(this)">
  <img src="p12.jpg" alt="Ppemi Photo 12" class="ppeumi-card" onclick="openModal(this)">
  <img src="p13.jpg" alt="Ppemi Photo 13" class="ppeumi-card" onclick="openModal(this)">
  <img src="p14.jpg" alt="Ppemi Photo 14" class="ppeumi-card" onclick="openModal(this)">
  <img src="p15.jpg" alt="Ppemi Photo 15" class="ppeumi-card" onclick="openModal(this)">
</div>

<!-- Click image to enlarge (Modal) -->
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
