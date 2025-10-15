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
      username: hyewon
      text: ""
      button:
        text: Download Resume
        url: /uploads/resume.pdf
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

# 🖼️ Image Slider (Main Home)
  - block: markdown
    content:
      title: ""
      subtitle: ""
      text: |-
        <!-- Image Slider (home main with text overlay) -->
         <div class="relative w-full max-w-7xl mx-auto mt-8 overflow-hidden rounded-2xl shadow-xl">
         <div class="flex transition-transform duration-700 ease-in-out" id="slider">
          
          <!-- Slide 1 -->
          <div class="relative w-full flex-shrink-0">
            <img src="/images/slide1.jpg" class="w-full h-[550px] object-cover opacity-70" alt="Slide 1">
            <div class="absolute inset-0 flex flex-col items-center justify-center text-white text-center">
              <h2 class="text-5xl font-extrabold mb-2 drop-shadow-lg">Web Service Design</h2>
              <p class="text-xl font-medium">Practical and stylish</p>
            </div>
          </div>

          <!-- Slide 2 -->
          <div class="relative w-full flex-shrink-0">
            <img src="/images/slide2.jpg" class="w-full h-[550px] object-cover opacity-70" alt="Slide 2">
            <div class="absolute inset-0 flex flex-col items-center justify-center text-white text-center">
              <h2 class="text-5xl font-extrabold mb-2 drop-shadow-lg">Big Data</h2>
              <p class="text-xl font-medium">Reading trends through data</p>
            </div>
          </div>

          <!-- Slide 3 -->
          <div class="relative w-full flex-shrink-0">
            <img src="/images/slide3.jpg" class="w-full h-[550px] object-cover opacity-70" alt="Slide 3">
            <div class="absolute inset-0 flex flex-col items-center justify-center text-white text-center">
              <h2 class="text-5xl font-extrabold mb-2 drop-shadow-lg">Database</h2>
              <p class="text-xl font-medium">Managing and organizing data</p>
            </div>
          </div>

          <!-- Slide 4 -->
          <div class="relative w-full flex-shrink-0">
            <img src="/images/slide4.jpg" class="w-full h-[550px] object-cover opacity-70" alt="Slide 4">
            <div class="absolute inset-0 flex flex-col items-center justify-center text-white text-center">
              <h2 class="text-5xl font-extrabold mb-2 drop-shadow-lg">AI</h2>
              <p class="text-xl font-medium">Leading the era of Artificial Intelligence</p>
            </div>
          </div>
        </div>

        <!-- Navigation Buttons -->
        <button onclick="prevSlide()" class="absolute top-1/2 left-5 transform -translate-y-1/2 bg-black/40 text-white px-4 py-2 rounded-full hover:bg-black/70 text-2xl">‹</button>
        <button onclick="nextSlide()" class="absolute top-1/2 right-5 transform -translate-y-1/2 bg-black/40 text-white px-4 py-2 rounded-full hover:bg-black/70 text-2xl">›</button>

        <!-- Indicators -->
        <div class="absolute bottom-4 left-1/2 -translate-x-1/2 flex gap-2">
          <button class="w-3 h-3 bg-white/80 rounded-full" onclick="goToSlide(0)"></button>
          <button class="w-3 h-3 bg-white/40 rounded-full" onclick="goToSlide(1)"></button>
          <button class="w-3 h-3 bg-white/40 rounded-full" onclick="goToSlide(2)"></button>
          <button class="w-3 h-3 bg-white/40 rounded-full" onclick="goToSlide(3)"></button>
        </div>
        </div>

         <script>
         let currentSlide = 0;
         const totalSlides = 4;

        function showSlide(index) {
          const slider = document.getElementById('slider');
          if (index < 0) index = totalSlides - 1;
          if (index >= totalSlides) index = 0;
          slider.style.transform = `translateX(-${index * 100}%)`;
          currentSlide = index;

          document.querySelectorAll('.absolute.bottom-4 button').forEach((dot, i) => {
            dot.classList.toggle('bg-white/80', i === index);
            dot.classList.toggle('bg-white/40', i !== index);
          });
        }

        function nextSlide() { showSlide(currentSlide + 1); }
        function prevSlide() { showSlide(currentSlide - 1); }
        function goToSlide(i) { showSlide(i); }

        setInterval(() => { nextSlide(); }, 5000);
        </script>
    design:
      columns: '1'

  - block: markdown
    content:
      title: '📚 Introduction'
      subtitle: ''
      text: |-  
        This space is all about me.  
        Here, you can not only find my basic personal information but also explore  
        my past projects and various details about Jeonbuk National University. Feel free to look around!
    design:
      columns: '1'

  - block: collection
    id: papers
    content:
      title: Interests
      filters:
        folders:
          - interest
    design:
      view: article-grid 
      columns: 3

  - block: collection
    id: talks
    content:
      title: Clubs
      filters:
        folders:
          - dong  
    design:
      view: article-grid
      columns: 3
          
  - block: collection
    id: jbnu
    content:
      title: JBNU
      filters:
        folders:
          - jbnu
    design:
      view: article-grid
      columns: 4

  - block: cta-card
    demo: false
    content:
      title: 🚀 Interested in My Projects?
      text: |-
        Check out my portfolio to explore the various projects I’ve worked on so far.
      button:
        text: Click Here!
        url: projects/
    design:
      card:
        css_class: "rounded-3xl shadow-xl text-center bg-gradient-to-r from-blue-500 to-blue-700 hover:from-blue-600 hover:to-blue-800 transition-all duration-300 ease-out"
        css_style: "padding: 3rem 2rem;"
        button:
          css_class: "mt-6 px-6 py-3 rounded-lg font-semibold bg-white text-blue-600 hover:bg-blue-600 hover:text-white transition-all duration-300 ease-in-out"
---
