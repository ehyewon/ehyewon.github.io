---
title: "리눅스 사물함만들기 시스템 프로젝트"
subtitle: "파일 잠금 시스템 구현"
date: 2025-06-10
summary: "C 언어 기반 사물함 시스템 구현 프로젝트"
type: project
layout: single
featured: true
show_author: false

image:
  filename: featured.jpg
  preview_only: false

  # 파일 다운로드 링크 (PDF)
links:
  - icon: file-pdf
    icon_pack: fas
    name: "보고서 다운로드 (PDF)"
    url: /files/locksystem.pdf
---
이 프로젝트는 **리눅스를 활용해 서버-클라이언트 모델로 동작하는 사물함 관리 시스템**을 구현한 것입니다.  

서버는 사물함을 관리하며, 사물함을 제공하
고 비밀번호를 설정하게 합니다.

클라이언트는 사물함 사용자 역할이며 사물함 이용 및 비밀번
호 설정 등을 수행합니다.

- 개발 언어: C  
- OS 환경: Ubuntu  
- 주요 기능: 파일 잠금, 접근 권한 관리, 충돌 처리  
