---
title: "게임 (Game)"
summary: "즐거움과 경쟁의 세계 🎮"
date: 2025-10-15
type: interest
layout: single
show_author: false

# 카드용 대표 이미지
image:
  filename: featured.jpg
  caption: "출처: Pinterest"
---

저는 게임을 좋아합니다.  
PC보다는 온라인 게임을 주로 합니다.  

제가 하는 게임은 **카트라이더**, **루미큐브**, **마인크래프트** 등이 있습니다.  
같이 하실 분 연락주세요! 😆

---

## **게임 스크린샷 모음**

---

## 🧩 **루미큐브 (Rummikub)**

두뇌 싸움 보드게임으로, 숫자와 색깔을 이용해 조합을 만들어가는 재미가 있습니다.  
가볍게 즐기면서도 집중력을 요하는 전략적인 게임입니다.

<div class="grid grid-cols-2 md:grid-cols-3 gap-4 mt-4">
  <div>
    <img src="game1.jpg" alt="루미큐브1" class="zoomable rounded-xl shadow-md hover:scale-105 transition-transform duration-300 cursor-pointer">
  </div>
</div>

---

## 🧱 **마인크래프트 (Minecraft)**

네모난 세상에서 건축을 하거나 생존을 하는 게임입니다.  
Xbox나 같은 와이파이를 통해 멀티로도 즐길 수 있으며 누구나 쉽게 플레이할 수 있습니다.  
단점은 유료입니다. 💸

<div class="grid grid-cols-2 md:grid-cols-3 gap-4 mt-4">
  <div>
    <img src="game2.jpg" alt="마인크래프트1" class="zoomable rounded-xl shadow-md hover:scale-105 transition-transform duration-300 cursor-pointer">
  </div>
</div>

---

## 🎯 **카트라이더 (KartRider)**

스피드전, 아이템전 등 다양한 모드로 즐길 수 있는 레이싱 게임입니다.  
빠른 손놀림과 판단력이 요구되며 여러 사람들과 같이 플레이할 수 있습니다.  
저 **상당히 잘합니다.** 🏎️

<div class="grid grid-cols-2 md:grid-cols-3 gap-4 mt-4">
  <div>
    <img src="game3.jpg" alt="카트라이더1" class="zoomable rounded-xl shadow-md hover:scale-105 transition-transform duration-300 cursor-pointer">
  </div>

  <div>
    <img src="game4.jpg" alt="카트라이더2" class="zoomable rounded-xl shadow-md hover:scale-105 transition-transform duration-300 cursor-pointer">
  </div>

  <div>
    <img src="game5.jpg" alt="카트라이더3" class="zoomable rounded-xl shadow-md hover:scale-105 transition-transform duration-300 cursor-pointer">
  </div>
</div>

---

![Unsplash Image](https://images.unsplash.com/photo-1493711662062-fa541adb3fc8?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8Z2FtZXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=500)
_Image credit: [Unsplash](https://unsplash.com)_

---

<!-- 🔍 이미지 클릭 확대 (모달) 효과 추가 -->
<style>
  /* 모달 배경 */
  .modal {
    display: none;
    position: fixed;
    z-index: 100;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.9);
    justify-content: center;
    align-items: center;
    transition: opacity 0.3s ease;
  }

  /* 모달 안의 이미지 (✅ 크게 확대됨) */
  .modal img {
    max-width: 95%;
    max-height: 95%;
    border-radius: 16px;
    box-shadow: 0 8px 40px rgba(0,0,0,0.5);
    animation: fadeIn 0.25s ease;
  }

  /* 등장 애니메이션 */
  @keyframes fadeIn {
    from {opacity: 0; transform: scale(0.95);}
    to {opacity: 1; transform: scale(1);}
  }

  /* 닫기 버튼 */
  .modal-close {
    position: absolute;
    top: 25px;
    right: 40px;
    color: #fff;
    font-size: 2.5rem;
    cursor: pointer;
    user-select: none;
  }

  .modal-close:hover {
    color: #ff5252;
  }
</style>

<!-- 모달 구조 -->
<div id="imgModal" class="modal" onclick="this.style.display='none'">
  <span class="modal-close">&times;</span>
  <img id="modalImage" alt="확대 이미지">
</div>

<!-- JS: 이미지 클릭 시 확대 -->
<script>
  const modal = document.getElementById("imgModal");
  const modalImg = document.getElementById("modalImage");
  const closeBtn = document.querySelector(".modal-close");

  document.querySelectorAll(".zoomable").forEach(img => {
    img.addEventListener("click", (e) => {
      e.stopPropagation();
      modalImg.src = img.src;
      modal.style.display = "flex";
    });
  });

  closeBtn.addEventListener("click", () => modal.style.display = "none");
  modal.addEventListener("click", () => modal.style.display = "none");
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") modal.style.display = "none";
  });
</script>
