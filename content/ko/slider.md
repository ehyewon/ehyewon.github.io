<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>이혜원 포트폴리오</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Swiper CSS -->
  <link rel="stylesheet" href="https://unpkg.com/swiper@10/swiper-bundle.min.css"/>

  <style>
    body {
      margin: 0;
      font-family: 'Pretendard', 'Noto Sans KR', sans-serif;
      background: #0b0b0b;
      color: white;
      overflow-x: hidden;
    }

    /* 전체 컨테이너 */
    .slider-section{
      width: 100vw;
      display: flex;
      justify-content: center;
      align-items: center;
      background: #000;
      padding: 40px 0;
    }

    .slider-section .swiper{
      width: 75%;
      aspect-ratio: 16/9;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    .swiper-slide{
      position: relative;
      background: #000;
    }

    .swiper-slide img{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      filter: brightness(0.78);
    }

    /* 캡션 */
    .slide-caption{
      position: absolute;
      bottom: 7%;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(0,0,0,0.5);
      padding: 1rem 1.4rem;
      border-radius: 12px;
      text-align: center;
      width: 75%;
      backdrop-filter: blur(4px);
    }

    .slide-caption h3{
      margin: 0 0 6px 0;
      font-size: 1.6rem;
      font-weight: 600;
      color: #fff;
      letter-spacing: 0.5px;
    }

    .slide-caption p{
      margin: 0;
      font-size: 0.95rem;
      color: #ddd;
      line-height: 1.4;
    }

    /* 네비 버튼 */
    .swiper-button-prev,
    .swiper-button-next{
      color: #fff;
      width: 40px;
      height: 40px;
      background: rgba(0,0,0,0.35);
      border-radius: 50%;
      transition: background .25s;
    }

    .swiper-button-prev:hover,
    .swiper-button-next:hover{
      background: rgba(0,0,0,0.65);
    }

    /* 페이지 점 */
    .swiper-pagination-bullet{
      width: 8px; height: 8px;
      background: #aaa;
      opacity: .9;
    }
    .swiper-pagination-bullet-active{
      background: #fff;
    }

    /* 반응형 */
    @media (max-width: 768px){
      .slider-section .swiper{ width: 95%; aspect-ratio: 4/3; }
      .slide-caption h3{ font-size: 1.25rem; }
      .slide-caption{ padding: .7rem 1rem; }
    }
  </style>
</head>

<body>
  <section class="slider-section">
    <div class="swiper">
      <div class="swiper-wrapper">

        <!-- 프론트엔드 -->
        <div class="swiper-slide">
          <img src="/images/slider1.jpg" alt="Frontend Development">
          <div class="slide-caption">
            <h3>Frontend Development</h3>
            <p>HTML, CSS, JavaScript를 활용한 반응형 웹 인터페이스 설계와 사용자 경험 중심의 UI 구현</p>
          </div>
        </div>

        <!-- 빅데이터 -->
        <div class="swiper-slide">
          <img src="/images/slider2.jpg" alt="Big Data Analysis">
          <div class="slide-caption">
            <h3>Big Data Analysis</h3>
            <p>Python과 Pandas, Spark를 기반으로 한 데이터 수집, 전처리, 시각화 및 트렌드 분석</p>
          </div>
        </div>

        <!-- 데이터베이스 -->
        <div class="swiper-slide">
          <img src="/images/slider3.jpg" alt="Database Management">
          <div class="slide-caption">
            <h3>Database Management</h3>
            <p>SQL과 NoSQL을 활용한 데이터 모델링, 쿼리 최적화, 시스템 아키텍처 설계 경험</p>
          </div>
        </div>

        <!-- 인공지능 -->
        <div class="swiper-slide">
          <img src="/images/slider4.jpg" alt="Artificial Intelligence">
          <div class="slide-caption">
            <h3>Artificial Intelligence</h3>
            <p>딥러닝 기반 이미지 분류 및 자연어 처리 프로젝트를 통한 AI 모델 설계와 구현</p>
          </div>
        </div>

      </div>

      <div class="swiper-button-prev"></div>
      <div class="swiper-button-next"></div>
      <div class="swiper-pagination"></div>
    </div>
  </section>

  <!-- Swiper JS -->
  <script src="https://unpkg.com/swiper@10/swiper-bundle.min.js"></script>
  <script>
  document.addEventListener("DOMContentLoaded", function() {
    new Swiper(".swiper", {
      loop: true,
      autoplay: { delay: 3500, disableOnInteraction: false },
      pagination: { el: ".swiper-pagination", clickable: true },
      navigation: { nextEl: ".swiper-button-next", prevEl: ".swiper-button-prev" },
      effect: "slide",
      speed: 700
    });
  });
  </script>
</body>
</html>