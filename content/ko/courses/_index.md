---
title: Courses
summary: My courses
type: landing

cascade:
  - target:
      path: '{/courses/*/**}'
    type: docs
    params:
      show_breadcrumb: true

sections:
  - block: collection
    id: courses
    content:
      title: Courses
      filters:
        tag: Course
        kinds:
          - section
    design:
      view: article-grid
      show_read_time: false
      show_date: false
      show_read_more: false
      columns: 1
  - block: map
    content:
      title: "📍 전북대학교 위치"
      text: "제가 공부하는 전북대학교의 위치입니다."
      coordinates:
        latitude: 35.8465
        longitude: 127.1293
      zoom: 15
      provider: mapnik
      marker:
        enable: true
        title: "전북대학교 (Jeonbuk National University)"
        description: "전라북도 전주시 덕진구 백제대로 567"
---
