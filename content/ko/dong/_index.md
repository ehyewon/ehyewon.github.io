---
title: "동아리"
type: landing

design:
  spacing: '4rem'

sections:
  - block: collection
    content:
      title: "전북대학교 중앙동아리"
      text: "제가 활동했던 그리고 활동중인 동아리입니다."
      filters:
        folders:
          - dong
    design:
      view: community/custom_card   # 커스텀 카드 뷰 (이미 설정돼 있다면 유지)
      columns: 3                    # 3개의 카드
      fill_image: true
      show_date: false
      show_read_time: false
      show_read_more: false
      css_class: "rounded-2xl shadow-lg hover:shadow-xl transition duration-300"
---