/* SPDX-License-Identifier: MIT */
(() => {
  'use strict';
  const search = document.querySelector('#search');
  const year = document.querySelector('#year-filter');
  const clear = document.querySelector('#clear');
  const status = document.querySelector('#results-status');
  const empty = document.querySelector('#empty');
  const sections = [...document.querySelectorAll('.year-section')];
  const total = document.querySelectorAll('.paper').length;
  function filter() {
    const terms = search.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let visible = 0;
    for (const section of sections) {
      let count = 0;
      const matchesYear = year.value === 'all' || year.value === section.dataset.year;
      for (const paper of section.querySelectorAll('.paper')) {
        const matches = matchesYear && terms.every(term => paper.dataset.search.includes(term));
        paper.hidden = !matches;
        if (matches) count++;
      }
      section.hidden = count === 0;
      section.querySelector('.section-count').textContent = `${count} reference${count === 1 ? '' : 's'}`;
      visible += count;
    }
    status.textContent = visible === total ? `Showing all ${total} references` : `Showing ${visible} of ${total} references`;
    empty.hidden = visible !== 0;
    clear.hidden = !terms.length && year.value === 'all';
  }
  search.addEventListener('input', filter);
  year.addEventListener('change', filter);
  clear.addEventListener('click', () => { search.value = ''; year.value = 'all'; filter(); search.focus(); });
  document.querySelector('#search-form').addEventListener('submit', event => event.preventDefault());
  for (const link of document.querySelectorAll('[data-year-link]')) {
    link.addEventListener('click', () => { search.value = ''; year.value = 'all'; filter(); });
  }
  // Keep direct reference links visible when users navigate back to a filtered page.
  window.addEventListener('hashchange', () => {
    const target = document.getElementById(location.hash.slice(1));
    if (target && (target.classList.contains('paper') || target.classList.contains('year-section'))) {
      search.value = ''; year.value = 'all'; filter(); target.scrollIntoView();
    }
  });
  document.querySelector('#search-tools').hidden = false;
  filter();
})();
