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
      backgroud:
        color: black
        image:
          filename: #이미지 나중에 추가하기 stacked-peaks.svg

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

  #슬라이더 블록
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
          
    design:
      view: card
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
        author: ''
        category: ''
        tag: ''
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ''
      offset: 0
      order: desc
    design:
      # Choose a layout view
      view: card
      # Reduce spacing
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
