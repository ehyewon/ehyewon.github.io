---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  spacing: '6rem'

sections:

  # 🧍‍♀️ 프로필
  - block: resume-biography-3
    content:
      username: hyewon
      text: ""
      button:
        text: 이력서 다운받기
        url: /uploads/resume.pdf
        css_class: "hover:bg-sky-200 hover:text-sky-700 transition"
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

# 🖼️ 이미지 슬라이드 (홈 메인용)
  - block: markdown
    content:
      title: ""
      subtitle: ""
      text: |-
        <!-- 이미지 슬라이드 (home main용, 텍스트 오버레이 포함) -->
         <div class="relative w-full max-w-7xl mx-auto mt-8 overflow-hidden rounded-2xl shadow-xl">
          <!-- 슬라이드 컨테이너 (❗하나만 존재해야 함) -->
         <div class="flex transition-transform duration-700 ease-in-out" id="slider">
          
          <!-- Slide 1 -->
          <div class="relative w-full flex-shrink-0">
            <img src="/images/slide1.jpg" class="w-full h-[550px] object-cover opacity-70" alt="Slide 1">
            <div class="absolute inset-0 flex flex-col items-center justify-center text-white text-center">
              <h2 class="text-5xl font-extrabold mb-2 drop-shadow-lg">웹 서비스 설계</h2>
              <p class="text-xl font-medium">실용적이고 감각적인</p>
            </div>
          </div>

          <!-- Slide 2 -->
          <div class="relative w-full flex-shrink-0">
            <img src="/images/slide2.jpg" class="w-full h-[550px] object-cover opacity-70" alt="Slide 2">
            <div class="absolute inset-0 flex flex-col items-center justify-center text-white text-center">
              <h2 class="text-5xl font-extrabold mb-2 drop-shadow-lg">빅데이터</h2>
              <p class="text-xl font-medium">데이터를 통해 트렌드를 읽는</p>
            </div>
          </div>

          <!-- Slide 3 -->
          <div class="relative w-full flex-shrink-0">
            <img src="/images/slide3.jpg" class="w-full h-[550px] object-cover opacity-70" alt="Slide 3">
            <div class="absolute inset-0 flex flex-col items-center justify-center text-white text-center">
              <h2 class="text-5xl font-extrabold mb-2 drop-shadow-lg">데이터베이스</h2>
              <p class="text-xl font-medium">데이터를 다루는</p>
            </div>
          </div>

          <!-- Slide 4 -->
          <div class="relative w-full flex-shrink-0">
            <img src="/images/slide4.jpg" class="w-full h-[550px] object-cover opacity-70" alt="Slide 4">
            <div class="absolute inset-0 flex flex-col items-center justify-center text-white text-center">
              <h2 class="text-5xl font-extrabold mb-2 drop-shadow-lg">AI</h2>
              <p class="text-xl font-medium">AI 시대를 이끄는</p>
            </div>
          </div>
        </div>

        <!-- 좌우 버튼 -->
        <button onclick="prevSlide()" class="absolute top-1/2 left-5 transform -translate-y-1/2 bg-black/40 text-white px-4 py-2 rounded-full hover:bg-black/70 text-2xl">‹</button>
        <button onclick="nextSlide()" class="absolute top-1/2 right-5 transform -translate-y-1/2 bg-black/40 text-white px-4 py-2 rounded-full hover:bg-black/70 text-2xl">›</button>

        <!-- 인디케이터 -->
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

        // 인디케이터 색 변경
        document.querySelectorAll('.absolute.bottom-4 button').forEach((dot, i) => {
            dot.classList.toggle('bg-white/80', i === index);
           dot.classList.toggle('bg-white/40', i !==     index);
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
      title: '📚 소개글'
      subtitle: ''
      text: |-  
        이 공간은 저를 소개하는 공간입니다.  
        해당 사이트에서는 저의 기본적인 개인정보 외에도  
        제가 했던 프로젝트와 전북대에 대한 다양한 정보도 만나보실 수 있습니다. 편하게 둘러보세요!!
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
    id: talks
    content:
      title: 동아리
      filters:
        folders:
          - dong  
    design:
      view: article-grid
      columns: 3
          
  - block: collection
    id: jbnu
    content:
      title: 전북대
      filters:
        folders:
          - jbnu
    design:
      view: article-grid
      columns: 4

  - block: cta-card
    demo: false
    content:
      title: 프로젝트 보러가기♬
      text: |-
        지금까지 작업한 저의 여러 프로젝트들을 포트폴리오에서 만나보실 수 있습니다.
      button:
        text: 클릭!
        url: projects/
    design:
      card:
        css_class: "bg-sky-100 text-slate-900 hover:bg-sky-200 dark:bg-gradient-to-br dark:from-[#1e293b] dark:to-[#0f172a] dark:text-gray-100 transition-all duration-500 ease-in-out"
        css_style: "padding: 3rem 2rem;"
        button:
          css_class: "mt-6 px-6 py-3 rounded-lg font-semibold bg-white text-blue-600 hover:bg-blue-600 hover:text-white transition-all duration-300 ease-in-out"


---
