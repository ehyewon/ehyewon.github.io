---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '6rem'

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
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
      # Avatar customization
      avatar:
        size: medium
        shape: circle

  - block: markdown
    content:
      title: '📚 Introduce'
      subtitle: ''
      text: |-
        안녕하세요. 웹 개발자를 희망하는 이헤원입니다. 이 공간은 저를 소개하는 공간입니다. 해당 사이트에서는 저의 기본적인 개인정보 외에도 제가 했던 포로젝트와 최근 트렌드 소식까지 만나보실 수 있습니다. 편하게 둘러보세요!
    design:
      columns: '1'


        # 🎞 메인 슬라이더 블록
  - block: slide
    content:
      dir: "" 
      height: "420px"
      width: "100%"
      webp: false
      resize:  
      command: "" 
      option: "" 
      zoomable: false
      slides:
        - title: "프론트엔드"
          content: "React와 Next.js로 인터랙티브한 웹 경험을 만듭니다."
          align: "center"
          background:
            image:
              filename: "slide1.jpg"
              filters:
                brightness: 1.0
            position: "center"
            color: "#000"
        - title: "빅데이터"
          content: "Python, Pandas, SQL로 인사이트를 시각화합니다."
          align: "center"
          background:
            image:
              filename: "slide2.jpg"
              filters:
                brightness: 1.0
            position: "center"
            color: "#000"
        - title: "데이터베이스"
          content: "MySQL과 MongoDB로 효율적인 데이터 구조를 설계합니다."
          align: "center"
          background:
            image:
              filename: "slide3.jpg"
              filters:
                brightness: 1.0
            position: "center"
            color: "#000"
        - title: "AI & Web"
          content: "인공지능 모델을 웹 서비스로 구현합니다."
          align: "center"
          background:
            image:
              filename: "slide4.jpg"
              filters:
                brightness: 1.0
            position: "center"
            color: "#000"
    design:
      slide_height: "420px"
      slide_width: "100%"
      loop: true
      interval: 4000


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
    content:
      title: 뉴스
      text: ''
      filters:
        folders:
          - news     
    design:
      view: article-grid
      columns: 4
          
  - block: collection
    id: 
    content:
      title: 전북대
      subtitle: ''
      text: ''
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
