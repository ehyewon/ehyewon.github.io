---
title: "Game"
summary: "The world of fun and competition 🎮"
date: 2025-10-15
type: interest
layout: single
show_author: false

# Representative image for card
image:
  filename: featured.jpg
  caption: "Source: Pinterest"
---

I love playing games.  
I mostly enjoy online games rather than PC single-player ones.  

Some of the games I play include **KartRider**, **Rummikub**, and **Minecraft**.  
If you’d like to play together, feel free to reach out! 😆

---

# **Game Screenshot Collection**

## 🧩 **Rummikub**

A brain-battle board game where you create combinations using numbers and colors.  
It’s a casual yet strategic game that requires focus and logical thinking.

<div class="grid grid-cols-2 md:grid-cols-3 gap-4 mt-4">
  <div>
    <img src="game1.jpg" alt="Rummikub 1" class="zoomable rounded-xl shadow-md hover:scale-105 transition-transform duration-300 cursor-pointer">
  </div>
</div>

---

## 🧱 **Minecraft**

A sandbox game where you can build and survive in a blocky world.  
You can play multiplayer through Xbox or local Wi-Fi, and it’s accessible to players of all ages.  
The only downside — it’s not free. 💸

<div class="grid grid-cols-2 md:grid-cols-3 gap-4 mt-4">
  <div>
    <img src="game2.jpg" alt="Minecraft 1" class="zoomable rounded-xl shadow-md hover:scale-105 transition-transform duration-300 cursor-pointer">
  </div>
</div>

---

## 🎯 **KartRider**

A racing game with various modes such as Speed and Item battles.  
It requires quick reflexes and decision-making, and it’s even more fun with friends.  
And yes — I’m **pretty good at it.** 🏎️

<div class="grid grid-cols-2 md:grid-cols-3 gap-4 mt-4">
  <div>
    <img src="game3.jpg" alt="KartRider 1" class="zoomable rounded-xl shadow-md hover:scale-105 transition-transform duration-300 cursor-pointer">
  </div>

  <div>
    <img src="game4.jpg" alt="KartRider 2" class="zoomable rounded-xl shadow-md hover:scale-105 transition-transform duration-300 cursor-pointer">
  </div>

  <div>
    <img src="game5.jpg" alt="KartRider 3" class="zoomable rounded-xl shadow-md hover:scale-105 transition-transform duration-300 cursor-pointer">
  </div>
</div>

---

![Unsplash Image](https://images.unsplash.com/photo-1493711662062-fa541adb3fc8?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8Z2FtZXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=500)
_Image credit: [Unsplash](https://unsplash.com)_

---

<!-- 🔍 Image Zoom Modal Effect -->
<style>
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

  .modal img {
    max-width: 95%;
    max-height: 95%;
    border-radius: 16px;
    box-shadow: 0 8px 40px rgba(0,0,0,0.5);
    animation: fadeIn 0.25s ease;
  }

  @keyframes fadeIn {
    from {opacity: 0; transform: scale(0.95);}
    to {opacity: 1; transform: scale(1);}
  }

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

<div id="imgModal" class="modal" onclick="this.style.display='none'">
  <span class="modal-close">&times;</span>
  <img id="modalImage" alt="Zoomed Image">
</div>

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
