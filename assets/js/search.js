import lunr from "lunr";

(async function () {
  const response = await fetch("/index.json");
  const indexJSON = await response.json();

  // lunr 한국어 토큰 분리기
  function koreanTokenizer(obj) {
    if (!arguments.length || obj == null || obj == undefined) return [];
    if (Array.isArray(obj)) return obj.map(koreanTokenizer);
    let str = obj.toString().toLowerCase();
    return str.split(""); // 한 글자 단위로 분리!
  }

  // 기존 lunr 토크나이저 교체
  lunr.tokenizer.separator = /[\s\-]+/;
  lunr.tokenizer = koreanTokenizer;

  // 인덱스 구성
  const index = lunr(function () {
    this.ref("permalink");
    this.field("title");
    this.field("summary");
    this.field("content");

    indexJSON.forEach(function (doc) {
      this.add(doc);
    }, this);
  });

  // 검색 입력 이벤트
  const input = document.querySelector(".search-input");
  const resultsContainer = document.querySelector(".search-results");
  const countDisplay = document.querySelector(".search-results-count");

  input.addEventListener("input", function () {
    const query = input.value.trim();
    resultsContainer.innerHTML = "";
    if (query.length === 0) return;

    const results = index.search(query);

    countDisplay.textContent = `${results.length} results for "${query}"`;

    if (results.length === 0) {
      resultsContainer.innerHTML = "<p>검색 결과가 없습니다.</p>";
    } else {
      results.forEach(function (result) {
        const doc = indexJSON.find((d) => d.permalink === result.ref);
        if (doc) {
          const el = document.createElement("div");
          el.classList.add("search-result");
          el.innerHTML = `
            <h3><a href="${doc.permalink}">${doc.title}</a></h3>
            <p>${doc.summary || ""}</p>
          `;
          resultsContainer.appendChild(el);
        }
      });
    }
  });
})();
