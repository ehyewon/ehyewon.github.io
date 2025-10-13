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

  # 🖼️ 이미지 슬라이드 추가
   # 🖼️ 이미지 슬라이드 (수정된 버전)
  - block: markdown
    content:
      title: ""
      subtitle: ""
      text: |-
        <!-- 수정 시작: 슬라이드 전체 크기 확장 및 오버레이/텍스트 추가 -->
        <div class="relative w-full max-w-7xl mx-auto mt-6 overflow-hidden rounded-2xl shadow-lg">
          <div class="flex transition-transform duration-700 ease-in-out" id="slider">
            
            <!-- Slide 1: Front-End -->
            <div class="relative w-full flex-shrink-0">
              <img src="/images/slide1.jpg" class="w-full h-[450px] object-cover opacity-80" alt="Slide 1">
              <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
                <h2 class="text-4xl font-bold text-white drop-shadow-lg">Front-End</h2>
              </div>
            </div>

            <!-- Slide 2: Big Data -->
            <div class="relative w-full flex-shrink-0">
              <img src="/images/slide2.jpg" class="w-full h-[450px] object-cover opacity-80" alt="Slide 2">
              <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
                <h2 class="text-4xl font-bold text-white drop-shadow-lg">Big Data</h2>
              </div>
            </div>

            <!-- Slide 3: Database -->
            <div class="relative w-full flex-shrink-0">
              <img src="/images/slide3.jpg" class="w-full h-[450px] object-cover opacity-80" alt="Slide 3">
              <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
                <h2 class="text-4xl font-bold text-white drop-shadow-lg">Database</h2>
              </div>
            </div>

            <!-- Slide 4: AI -->
            <div class="relative w-full flex-shrink-0">
              <img src="/images/slide4.jpg" class="w-full h-[450px] object-cover opacity-80" alt="Slide 4">
              <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
                <h2 class="text-4xl font-bold text-white drop-shadow-lg">AI</h2>
              </div>
            </div>

          </div>

          <!-- 좌우 버튼 -->
          <button onclick="prevSlide()" class="absolute top-1/2 left-3 transform -translate-y-1/2 bg-black/40 text-white px-3 py-2 rounded-full hover:bg-black/70">‹</button>
          <button onclick="nextSlide()" class="absolute top-1/2 right-3 transform -translate-y-1/2 bg-black/40 text-white px-3 py-2 rounded-full hover:bg-black/70">›</button>

          <!-- 하단 점 버튼 -->
          <div class="absolute bottom-3 left-1/2 -translate-x-1/2 flex gap-2">
            <button class="w-3 h-3 bg-white/70 rounded-full" onclick="goToSlide(0)"></button>
            <button class="w-3 h-3 bg-white/40 rounded-full" onclick="goToSlide(1)"></button>
            <button class="w-3 h-3 bg-white/40 rounded-full" onclick="goToSlide(2)"></button>
            <button class="w-3 h-3 bg-white/40 rounded-full" onclick="goToSlide(3)"></button>
          </div>
        </div>

        <script>
        // 기존 JS 동일
        let currentSlide = 0;
        const totalSlides = 4;
        function showSlide(index) {
          const slider = document.getElementById('slider');
          if (index < 0) index = totalSlides - 1;
          if (index >= totalSlides) index = 0;
          slider.style.transform = `translateX(-${index * 100}%)`;
          currentSlide = index;
          document.querySelectorAll('.absolute.bottom-3 button').forEach((dot, i) => {
            dot.classList.toggle('bg-white/70', i === index);
            dot.classList.toggle('bg-white/40', i !== index);
          });
        }
        function nextSlide() { showSlide(currentSlide + 1); }
        function prevSlide() { showSlide(currentSlide - 1); }
        function goToSlide(i) { showSlide(i); }
        setInterval(() => { nextSlide(); }, 4000);
        </script>
        <!-- 수정 끝 -->
    design:
      columns: '1'

  - block: markdown
    content:
      title: '📚 Introduce'
      subtitle: ''
      text: |-
        안녕하세요. 웹 개발자를 희망하는 이혜원입니다.  
        이 공간은 저를 소개하는 공간입니다.  
        해당 사이트에서는 저의 기본적인 개인정보 외에도  
        제가 했던 프로젝트와 최근 트렌드 소식까지 만나보실 수 있습니다.  
        편하게 둘러보세요!!
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
