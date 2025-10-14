---
title: "리눅스 사물함시스템 프로젝트"
subtitle: "파일 잠금 시스템 구현"
date: 2025-06-10
summary: "C 언어 기반 파일 잠금 시스템 구현 프로젝트"
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
이 프로젝트는 **리눅스 환경에서의 파일 잠금(lock) 시스템**을 구현한 것입니다.  
`fcntl`, `open`, `close` 시스템 콜을 활용하여 다중 프로세스 간 자원 경합을 제어하는 기능을 포함하고 있습니다.

- 개발 언어: C  
- OS 환경: Ubuntu  
- 주요 기능: 파일 잠금, 접근 권한 관리, 충돌 처리  
